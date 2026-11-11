import os
from google import genai
from dotenv import load_dotenv

# Cargar la clave desde el .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("❌ Error: No se encontró la GEMINI_API_KEY")
    exit()

client = genai.Client(api_key=api_key)

print("🚀 Conectando con Gemini...")
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Escribe un hook publicitario de 10 palabras para vender un servicio de IA a empresas.",
)

print("\n--- RESPUESTA DE LA IA ---")
print(response.text)