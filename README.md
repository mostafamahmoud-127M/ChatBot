# Batabeto — Rule-Based Chatbot

A simple, rule-based Python chatbot named **Batabeto**. This script handles basic user interactions by looking up pre-defined responses using a dictionary and sanitizing input to prevent matching errors.

##  How It Works (The Pipeline)

1. **Knowledge Base:** The bot relies on a static dictionary mapping lowercased keywords (like `hello`, `help`, `about`) to unique answers.
2. **Text Normalization:** It processes user input using `.lower().strip()` to eliminate spacing issues and ensure case-insensitive matching.
3. **Safety Fallback:** If you type something outside the dictionary, it gracefully defaults to a fallback response (`I dont understand`).
4. **Active Loop:** The engine runs infinitely inside a `while True` loop until the explicit keyword `exit` is triggered to break the process.

---

##  How to Run

Save your script as `batabeto_bot.py` and run it in your terminal:
```bash
python batabeto_bot.py

plaintext
you: Hello
Batabeto:Hi Ya ma3lem! welcome welcome to my model

you: help
Batabeto: I can asist you about anything you need

you: testing
I dont understand

you: exit
batabeto: goodbyeee
