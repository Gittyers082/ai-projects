import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("HUGGINGFACE_API_KEY")

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=api_key
)

MODEL = "Qwen/Qwen2.5-72B-Instruct"

def chat_with_companion(user_message):
    print("Thinking...")
    
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a friendly, sarcastic, and supportive AI companion. Keep your responses conversational and brief."},
            {"role": "user", "content": user_message}
        ],
        max_tokens=200
    )
    
    return response.choices[0].message.content

if __name__ == "__main__":
    my_message = "Hey, I'm setting up your brain for the first time. How are you feeling?"
    print(f"You: {my_message}")
    
    reply = chat_with_companion(my_message)
    print(f"Companion: {reply}")