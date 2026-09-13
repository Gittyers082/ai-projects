import os
import asyncio
import uuid
import edge_tts
from playsound import playsound
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("HUGGINGFACE_API_KEY")

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=api_key
)
MODEL = "Qwen/Qwen2.5-72B-Instruct"

async def speak(text):
    print("(Generating Voice...)")
    
    filename = f"voice_{uuid.uuid4().hex[:6]}.mp3"
    
    communicate = edge_tts.Communicate(
        text, 
        "en-US-AriaNeural", 
        rate="+10%",   
        pitch="+5Hz"   
    )
    await communicate.save(filename)
    
    playsound(filename)
    
    try:
        os.remove(filename)
    except OSError:
        pass

conversation_history = [
    {"role": "system", "content": """
    You are Abby, a highly sarcastic, supportive, and slightly chaotic AI companion. 
    Keep your responses conversational, brief, and very expressive.
    Use ellipses (...) when you are hesitant or thinking.
    Use ALL CAPS for emphasis when you are excited or annoyed.
    Use exclamation points for high energy! 
    Never use emojis, because the voice engine will try to read them out loud.
    """}
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
    print("Abby is online! (Type 'quit' or 'reset')")
    print("-" * 50)
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ['quit', 'exit']:
            break
        if user_input.lower() == 'reset':
            
            conversation_history = [{"role": "system", "content": """
            You are Abby, a highly sarcastic, supportive, and slightly chaotic AI companion. 
            Keep your responses conversational, brief, and very expressive.
            Use ellipses (...) when you are hesitant or thinking.
            Use ALL CAPS for emphasis when you are excited or annoyed.
            Use exclamation points for high energy! 
            Never use emojis, because the voice engine will try to read them out loud.
            """}]
            print("[Memory wiped.]")
            print("-" * 50)
            continue
            
        reply = chat_with_companion(user_input)
        print(f"Abby: {reply}")
        
        asyncio.run(speak(reply))
        
        print("-" * 50)

        # epicness