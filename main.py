import os
import datetime
from google import genai

# Configuration b l-package jdid dyal Google
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

# Tlbat mn Gemini
prompt = "Write a simple, short and useful Python code snippet. Output ONLY the code, no markdown, no explanations."

# Génération dyal l-code b l-modèle jdid
response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=prompt,
)

# Tssjil l-code f fichier jdid b ttarix dyal lyoum
date_str = datetime.datetime.now().strftime("%Y-%m-%d")
filename = f"project_{date_str}.py"

with open(filename, "w") as file:
    file.write(response.text)

print(f"Project for {date_str} created successfully!")
