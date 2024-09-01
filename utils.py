from openai import OpenAI
import requests
from PIL import Image
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
llm = "gpt-4o-mini"
im_gen = "dall-e-2"

def generate_backstory(prompt) -> str:
        
    messages = [{"role": "system", "content": prompt},
    {"role": "user", "content": "Create the backstory"}]

    llm_response = client.chat.completions.create(
        model=llm,
        messages=messages,
        temperature=0,
        # max_tokens=500
    )
    
    backstory = llm_response.choices[0].message.content
    return backstory


def generate_image(prompt):
    response = client.images.generate(
        model=im_gen,
        prompt=prompt,
        n=1,
        size="512x512"  
    )
    image_url = response.data[0].url
    image = Image.open(requests.get(image_url, stream=True).raw)
    return image, image_url