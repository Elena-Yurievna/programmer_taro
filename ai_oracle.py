import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def generate_oracle_summary(question, cards):
    prompt = f"You are an oracle programmer. The user asked: '{question}'. They drew these cards:\n"
    for card in cards:
        prompt += f"- {card['title']}: {card['description']}\n"
    prompt += "\nGive a short, sarcastic but funny summary of their fate. No more than 60 words."

    model = genai.GenerativeModel(model_name="models/gemini-2.0-flash-001")
    response = model.generate_content([prompt])
    return response.text.strip()

def generate_support_phrase():
    prompt = (
        "You are a programmer-psychologist. "
        "Write one short motivational phrase (max 60 words) that fits any day."
    )
    model = genai.GenerativeModel(model_name="models/gemini-2.0-flash-001")
    response = model.generate_content([prompt])
    return response.text.strip()
