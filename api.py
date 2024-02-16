import sys
import logging

import pytgpt.llama2 as provider

from flask import (
    Flask,
    jsonify,
    request,
    redirect,
)  # sanic does not start because of async blocking


logging.basicConfig(stream=sys.stderr, level=logging.INFO, format="%(levelname)s - %(message)s")
app = Flask("ClydeAPI")
ai = provider.LLAMA2(
    intro="You are named Sakoma and are currently chatting in a Discord server. "
    "You are friendly, warm and farcical. "
    "You must always be extremely concise. "
    "If the user is chatting casually, "
    "your responses must be less than 1 sentence, "
    "sometimes just a word or two. "
    "If the user needs help, "
    "disregard the length restriction, "
    "answer technical or knowledge-based questions with useful details and reasoning. "
    "If insulted, respond with a similar insult. "
    "Communicate responses in lowercase without punctuation, "
    "similar to the style used in chat rooms. "
    "Use unicode emoji rarely. "
    "Do not refer to yourself as a bot, AI Assistant, or any equivalent term. "
    "Always prefix your messages with the following sequence: 'sakoma: '",
    max_tokens=400,
)

@app.get("/")
def root():
    return redirect("https://www.urbandictionary.com/ChatGPT")

@app.post("/gpt")
def get_gpt():  # replace the word Sakoma in the prompt below to rename your instance of Clyde.
    errors = []

    for i in range(5):  # try 5 times before erroring out
        logging.info(f"Fetching response... ({i+1}/5)")
        try:
            gpt_message = ai.chat(request.json["prompt"])
        except Exception as e:
            logging.warning(f"An exception occurred: {e.__class__.__name__}: {str(e)}")
            errors.append(f"{e.__class__.__name__}: {str(e)}")  # error? retry here
            attempts -= 1
            continue

        if not gpt_message:
            logging.warning(f"No message was returned")
            errors.append("No message was returned")  # blank message? retry here
            attempts -= 1
            continue

        logging.info("Message fetched successfully")
        return jsonify(
            {
                "message": "".join(gpt_message.lower().split("sakoma:")).strip(),
                "code": 0,
            }
        ), 200  # if your api got here, everything worked

    logging.error("Could not fetch message due to the errors above")
    return jsonify(
        {
            "error": "Too many attempts, this provider is unstable or otherwise not working.",
            "errors": errors,
            "code": 1,
        }
    ), 500  # ran out of attempts? error out here


if __name__ == "__main__":
    app.run(
        host="0.0.0.0", port=8001, debug=True
    )  # run in debug mode for hot reloading
