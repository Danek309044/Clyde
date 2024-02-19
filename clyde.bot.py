import os
import asyncio
import secrets

import discord
from discord.ext import commands

import httpx
from dotenv import load_dotenv

# prevent leaking any tokens to cause bans or blocks
load_dotenv()

owner = 603635602809946113
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = commands.Bot(
    command_prefix=secrets.token_urlsafe(8),
    help_command=None,
    intents=intents,
    owner_id=owner,
)


@client.event
async def on_connect():
    print("Clyde has connected to Discord.")


@client.event
async def on_ready():
    print("Clyde ready!")


@client.event
async def on_message(message):
    # specify user ids forbidden from using clyde, eg. 691187099570929684
    forbidden = []

    if message.author.id in forbidden:
        print("Ignoring message")
        return

    if message.author == client.user:
        print("Ignoring self message")
        return

    if message.author.bot:
        print("Ignoring bot message")
        return

    if (
        client.user.mentioned_in(message)
        or not message.guild
        or message.channel.type == discord.ChannelType.public_thread
    ):
        ms = await message.reply("\u200b:clock3:", mention_author=False)
        async with message.channel.typing():
            prompt = message.content.replace(client.user.mention, "\u200b").strip()

            async with httpx.AsyncClient(timeout=None) as web:
                try:
                    # run ai externally via an attached api
                    response = await web.post(
                        "http://127.0.0.1:8001/gpt",
                        json={"prompt": prompt, "type": "g4f"},
                    )
                except httpx.ConnectError:
                    # server offline error response
                    await ms.edit(content="\u200b:earth_africa::x:")
                    user = client.get_user(owner)
                    await user.send(
                        "# Oh shit!\nError 2 has occurred: The API server is offline.\n\n"
                        "Please restart the API server before trying to use ChatGPT."
                    )
                    await asyncio.sleep(30)
                    return await ms.delete()

                if response.status_code == 200:
                    # correct response
                    gpt_message = response.json()["message"]
                    if len(gpt_message) <= 2000:
                        return await ms.edit(gpt_message)
                    # too large response
                    await ms.edit(content="\u200b:scroll::warning:")
                    await asyncio.sleep(30)
                    return await ms.delete()

                # error response
                user = client.get_user(owner)
                newline = "\n"
                await ms.edit(content="\u200b:scroll::x:")
                await user.send(
                    f"# Oh shit!\n"
                    f"Error {response.json()['code']} has occurred: {response.json()['error']}\n"
                    f"The following errors were caught:\n{newline.join(response.json()['errors'])}\n\n"
                    f"If someone else got this error, tell them to retry their request."
                )  # only the owner id will get this
                await asyncio.sleep(30)
                return await ms.delete()


client.run(os.getenv("TOKEN"))