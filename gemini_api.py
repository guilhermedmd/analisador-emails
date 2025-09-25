import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

# Configure sua chave de API
genai.configure(api_key="AIzaSyAMHrScaPh62gjr-Fy0bQQVM0O1P3MMVOk")

def teste():
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content("Me explique um pouco sobre a f1")
    print(response.text)

