import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

with open(".env", "rb") as f:
    content = f.read()
    print("Raw bytes:", content)

load_dotenv(".env")

print("GOOGLE_API_KEY:", repr(os.getenv("GOOGLE_API_KEY")))

# Try setting manually
os.environ["GOOGLE_API_KEY"] = "AIzaSyDghfLTO7UdFKVRxiASivtsaTz6g016o70"

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.3,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

try:
    response = llm.invoke("Hello, test message")
    print("LLM works:", response.content)
except Exception as e:
    print("Error:", str(e))