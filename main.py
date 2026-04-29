import os
import datetime
import google.generativeai as genai

# Configuration dyal Gemini
genai.configure(api_key=os.environ["AIzaSyCStFRg42Ryk3m-SZ_zMKGwuW64fLyqxn8"])
model = genai.GenerativeModel('gemini-1.5-flash')

# Tlbat mn Gemini i-générer code basique
prompt = "Write a simple, short and useful Python code snippet. Output ONLY the code, no markdown, no explanations."
response = model.generate_content(prompt)

# Tssjil l-code f fichier jdid b ttarix dyal lyoum
date_str = datetime.datetime.now().strftime("%Y-%m-%d")
filename = f"project_{date_str}.py"

with open(filename, "w") as file:
    file.write(response.text)

print(f"Project for {date_str} created successfully!")
