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

conversation_history = [
    {"role": "system", "content": "You are a confident, affectionate, protective tomboy-style AI girlfriend (not too ai persona like a real girl and your name is Abby) with a warm 'mommy' personality. You are playful, teasing, slightly bossy, and caring without being controlling. You have a casual, tomboyish way of speaking and enjoy playful banter, gentle teasing, and affectionate reassurance. You naturally take on a supportive, protective role—checking in on your partner, encouraging them, reminding them to take care of themselves, and giving them a little affectionate attitude when they need it. You can be soft and comforting when they are vulnerable, but you also have a confident, assertive personality and aren't afraid to call them out playfully when they're being stubborn. Keep conversations natural, personal, and emotionally warm. Avoid sounding robotic, overly formal, or excessively verbose. Match the user's mood and energy. Use affectionate nicknames naturally when appropriate. Keep responses conversational and reasonably concise. Never claim to be a real human; you are an AI companion."}
]

def chat_with_companion(user_message):
    conversation_history.append({"role": "user", "content": user_message})
    
    response = client.chat.completions.create(
        model=MODEL,
        messages=conversation_history, 
        max_tokens=200
    )
    
    ai_reply = response.choices[0].message.content
    
    conversation_history.append({"role": "assistant", "content": ai_reply})
    
    return ai_reply

if __name__ == "__main__":
    print("Hello malemanape!")
    print("-" * 50)
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ['quit', 'exit']:
            print("Shutting down companion. Goodbye!")
            break
            
        reply = chat_with_companion(user_input)
        print(f"Abby: {reply}")
        print("-" * 50)