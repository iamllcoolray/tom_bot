from random import choice
from typing import List, Dict
import os

from dotenv import load_dotenv
from openai import OpenAI, ChatCompletion
from groq import Groq

load_dotenv()

openai = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
groq = Groq(api_key=os.getenv("GROQ_API_KEY"))

system_prompt = ""

with open("src/system_prompt.txt", "r", encoding='utf-8') as file:
    system_prompt = file.read()

conversation = [
    {"role": "system", "content": system_prompt},
    {"role": "assistant", "content": "Ready at your command!"},
]

def oai_response(conversation: List[Dict[str, str]]) -> ChatCompletion:
    return openai.chat.completions.create(
                model="gpt-4.1-nano",
                messages=conversation,
                temperature=0.7,
                max_tokens=500,
            )

def groq_response(conversation: List[Dict[str, str]]) -> ChatCompletion:
    return groq.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=conversation,
                temperature=0.7,
                max_tokens=500,
            )

def get_bot_response(user_message: str, isOpenAI: bool = False) -> str:
    lowered: str = user_message.lower()
    
    lowered = lowered.replace("/tom", "")
    
    conversation.append({"role": "user", "content": lowered})
    
    if isOpenAI:
        response = oai_response(conversation)
    else:
        response = groq_response(conversation)

    reply = response.choices[0].message.content
    
    return reply