import os
from google import genai
from openai import OpenAI

# 1. Kayjib les APIs mn GitHub Secrets
gemini_client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
nvidia_client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.environ["NVIDIA_API_KEY"]
)

# 2. Gemini kaysayb l-Fikra
print("🧠 1/3: Gemini kay-fker f projet kbir...")
gemini_prompt = """
Act as a Senior Product Manager. Propose a highly complex, professional-grade web application that can be built in a single file (HTML/CSS/JS). 
Provide: 
1. App Name 
2. Core Concept 
3. Advanced Features (like LocalStorage)
4. UI/UX Design System (Modern, responsive).
"""
gemini_response = gemini_client.models.generate_content(
    model='gemini-2.5-flash',
    contents=gemini_prompt,
)
project_architecture = gemini_response.text
print("✅ L-Fikra wajda!")

# 3. DeepSeek kaykteb l-Code
print("💻 2/3: DeepSeek kay-développi l-code...")
deepseek_prompt = f"""
Act as an Expert Full-Stack Developer. Write the complete, production-ready code (HTML, CSS, and JavaScript all combined in one file) for this application architecture:
{project_architecture}
Output ONLY the raw code. Do not include markdown formatting like ```html or ```javascript.
"""
completion = nvidia_client.chat.completions.create(
    model="deepseek-ai/deepseek-v4-pro",
    messages=[{"role": "user", "content": deepseek_prompt}],
    temperature=0.7,
    top_p=0.95,
    max_tokens=8000,
    stream=False # Khlinaha False bash yjme3 l-code kaml d9a we7da
)

# Kanjbdo l-code w kan7iydo mno zwaq dyal Markdown
code_final = completion.choices[0].message.content
code_final = code_final.replace("```html", "").replace("```", "").strip()

with open("index.html", "w", encoding="utf-8") as f:
    f.write(code_final)
print("✅ index.html wajed!")

# 4. Kan-génériw fichier README
print("📄 3/3: Tansaybo README...")
readme_content = f"""# 🚀 AI-Generated Professional Project

This repository contains a professional web application completely designed and coded by AI.

## 🧠 Architecture (by Google Gemini)
{project_architecture}

## 💻 Development
- **Code Generation:** NVIDIA DeepSeek-V4-Pro
- **Automation:** GitHub Actions
"""
with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme_content)
print("✅ Kolshi m-gadd!")
