# Clyde
A recreation of Discord's cancelled AI chatbot: Clyde.

# Story
On March 2nd 2023, Discord introduced Clyde, an AI chatbot based on OpenAI's ChatGPT, however it had many flaws, and all people hated it, mostly from NTTS' (No Text To Speech) audience, and Discord killed Clyde on December 1st 2023, as it would cost Discord a lot of money and so they decided to shut it down, the EOL date was announced on November 5th 2023 and all of @debarkak's friends and everyone in the Chomu Paradise Club panicked and was very sad (infact Bohdan threw his A30s and cracked the screen even more than it was), however Luna knew that this would happen, and already started working on a backup.

# Information
### Name
The name for this bot should be Clyde, but you can rename it. The pre-deployed bot's name was Sakoma, we moved a to proper Clyde bot account.

### Programming Languages
Clyde uses Python for the bot/API and Shell for launching it.

### AI model
Clyde tries to use the best providers from [python-tgpt](https://github.com/Simatwa/python-tgpt) and [gpt4free](https://github.com/xtekky/gpt4free), these are subject to change depending on what providers are online.

We would recommend to use one of the following providers for your instance of Clyde:
- gpt4free: Bing¹, GeminiProChat², Llama2⁵, Phind⁴
- python-tgpt: Llama2⁵, Phind³

<sub><sup>¹May give CAPTCHAs after a while or when providing the wrong values.</sub></sup><br>
<sub><sup>²If using the vendored provider file; check the [Providers](https://github.com/ClydeReborn/Providers).</sub></sup><br>
<sub><sup>³Has the tendency to say something unrelated if it didn't understand your prompt.</sub></sup><br>
<sub><sup>⁴May give errors or blank responses, use the `python-tgpt` implementation.</sub></sup><br>
<sub><sup>⁵May work abnormally slow or not return any responses.</sub></sup>

# How to run?
1. Clone this repo.
```sh
git clone https://github.com/ClydeReborn/Clyde
```

2. Install Python and required modules.
```sh
pip install -U -r requirements.txt
```

3. Open one of the `clyde.*.py` files, and make sure you have put your token in the `.env` file.
```
TOKEN=<TOKEN_GOES_HERE>
```

4. Replace `<TOKEN_GOES_HERE>` with your account token.<br>
Use a bot token for the bot version, or a user token for the selfbot version.*

<sub><sup>*Be careful when running Clyde as a selfbot, as it violates Discord ToS if you do so.</sub></sup>

### Testing Providers
To check working providers, run `python test_clyde_full.py` for a comprehensive test, or run `python test_clyde_quick.py` for a quick test.<br>
The comprehensive test may take a longer time to finish!

# Required OS
* Clyde can only run on Linux. We recommend using Arch Linux, Fedora or Debian for this.<br>
If you're using Windows, you may be able to run Clyde on WSL.

Enjoy!
