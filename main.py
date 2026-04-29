import os
from google import genai
from openai import OpenAI

# 1. Configuration dyal les APIs
gemini_client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
nvidia_client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.environ["NVIDIA_API_KEY"]
)

# 2. Gemini: Kifker f projet kbir w professionnel (Product Manager)
print("🧠 1/3: Gemini kay-smmem l-projet l-kbir...")
gemini_prompt = """
Act as a Senior Product Manager. Propose a highly complex, professional-grade web application that can be built in a single file (HTML/CSS/JS). 
Examples: A comprehensive Kanban Task Manager, an Interactive Analytics Dashboard, a Personal Finance Tracker, or an advanced Simulator Game.
Provide:
1. App Name
2. Core Concept & Value Proposition
3. Advanced Features (e.g., Local Storage saving, complex animations, data visualization, drag-and-drop)
4. UI/UX Design System (Modern, Glassmorphism, Dark/Light mode, etc.)
"""

gemini_response = gemini_client.models.generate_content(
    model='gemini-2.5-flash',
    contents=gemini_prompt,
)
project_architecture = gemini_response.text
print("✅ L-Fikra w l-Architecture wajdin!\n")

# 3. DeepSeek: Kaykteb l-code l-kbir (Senior Developer)
print("💻 2/3: DeepSeek (NVIDIA) kay-développi l-code...")
deepseek_prompt = f"""
Act as an Expert Full-Stack Developer. Write the complete, production-ready code (HTML, CSS, and JavaScript all combined in one file) for this application architecture:

{project_architecture}

Requirements:
- Ensure the UI is stunning, highly responsive, and uses modern CSS (Flexbox/Grid, transitions, variables).
- Write robust JavaScript (ES6+) with error handling and modular functions.
- If it needs data, use Window.localStorage to save the user's state.
- Output ONLY the raw code. Do not include markdown formatting like ```html or ```javascript.
"""

completion = nvidia_client.chat.completions.create(
    model="deepseek-ai/deepseek-v4-pro",
    messages=[{"role": "user", "content": deepseek_prompt}],
    temperature=0.7,
    top_p=0.95,
    max_tokens=16384, # Max tokens bash ykder ykteb projet kbir
    stream=True
)

code_final = ""
for chunk in completion:
    if not getattr(chunk, "choices", None):
        continue
    if chunk.choices and chunk.choices[0].delta.content is not None:
        code_final += chunk.choices[0].delta.content

# Nn9iw l-code mn markdown bash ykhdem directement
code_final = code_final.replace("```html", "").replace("```", "").strip()

with open("index.html", "w", encoding="utf-8") as f:
    f.write(code_final)
print("✅ L-Code (index.html) wajed!")

# 4. N-génériw README.md professionnel
print("📄 3/3: Tansaybo README professionnel...")
readme_content = f"""# 🚀 AI-Generated Professional Project

This repository contains a professional web application completely designed and coded by AI.

## 🧠 Architecture (by Google Gemini)
{project_architecture}

## 💻 Development
- **Code Generation:** NVIDIA DeepSeek-V4-Pro
- **Automation:** GitHub Actions
- **Format:** Single-file architecture (HTML/CSS/JS)

*Enjoy exploring the code!*
"""
with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme_content)
print("✅ README wajed!")
