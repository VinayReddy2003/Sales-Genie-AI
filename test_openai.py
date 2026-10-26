import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

try:
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents="Say hello",
    )
    print("✅ Gemini API working!")
    print(response.text)
except Exception as e:
    print(f"❌ Gemini API failed: {e}")