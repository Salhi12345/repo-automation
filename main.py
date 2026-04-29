import os
from google import genai

# 1. Kan-connectew m3a Gemini
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

print("🧠 Jari tasnim w kitabat l-projet b Gemini...")

# 2. Kan-tlbou mno ysawb site web kamel
prompt = """
Act as an expert web developer. Create a complete, creative, and fully functional web application (like a modern To-Do list, a beautiful Calculator, or a simple interactive game) in a SINGLE file.
Requirements:
- Combine HTML, CSS, and JavaScript in one file.
- Use a beautiful, modern UI design with nice colors and hover effects.
- Make sure the JavaScript logic works perfectly.
- Output ONLY the raw HTML code without markdown formatting like ```html.
"""

response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=prompt,
)

# 3. Kan-n9iw l-code w n-sayvoh f index.html
code = response.text.replace("```html", "").replace("```", "").strip()

with open("index.html", "w", encoding="utf-8") as f:
    f.write(code)

# 4. Kan-sawbo README.md dyal l-projet
with open("README.md", "w", encoding="utf-8") as f:
    f.write("# 🚀 AI Web App\n\nThis complete web application was generated automatically in seconds using Google Gemini API!\n\nSimply open `index.html` in your browser to see the result.")

print("✅ Fichiers wajdin: index.html w README.md")
