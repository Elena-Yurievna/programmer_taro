from flask import Flask, render_template, request
from cards import draw_cards
import os
import google.generativeai as genai
from dotenv import load_dotenv
from prompts import ORACLE_PROMPT_TEMPLATE, SUPPORT_PROMPT

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        question = request.form.get("question")
        cards = draw_cards()

        card_text = ""
        for card in cards:
            card_text += f"- {card['title']}: {card['description']}\n"

        prompt = ORACLE_PROMPT_TEMPLATE.format(question=question, cards=card_text)

        model = genai.GenerativeModel(model_name="models/gemini-2.0-flash-001")
        response = model.generate_content([prompt])
        oracle_message = response.text

        return render_template("index.html", question=question, cards=cards, oracle=oracle_message)

    return render_template("index.html", cards=None)

@app.route("/support", methods=["GET", "POST"])
def support():
    model = genai.GenerativeModel(model_name="models/gemini-2.0-flash-001")
    response = model.generate_content([SUPPORT_PROMPT])
    oracle_message = response.text.strip()

    return render_template("support.html", oracle=oracle_message)


if __name__ == "__main__":
    app.run(debug=True)
