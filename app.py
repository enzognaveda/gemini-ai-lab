import os
import streamlit as st
from google import genai
from dotenv import load_dotenv

# Configuración visual de la página
st.set_page_config(page_title="AI Growth Copilot", page_icon="🚀", layout="centered")

# Cargar API Key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Si no está en .env (para cuando esté en la nube), buscar en los secretos de Streamlit
if not api_key and "GEMINI_API_KEY" in st.secrets:
    api_key = st.secrets["GEMINI_API_KEY"]

st.title("🚀 AI Growth & Marketing Copilot")
st.markdown("Genera estrategias de contenido viral y ganchos publicitarios con **Google Gemini**.")

# Formulario de entrada
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        business_name = st.text_input("Nombre de la Marca / Negocio:", placeholder="Ej: VetCare Rancagua")
    with col2:
        niche = st.text_input("Rubro / Industria:", placeholder="Ej: Clínica Veterinaria, E-commerce")
    
    target_audience = st.text_input("Público Objetivo:", placeholder="Ej: Dueños de mascotas jóvenes de 20 a 35 años")
    goal = st.selectbox("Objetivo principal:", [
        "Captar nuevos clientes por WhatsApp",
        "Videos virales para TikTok / Reels",
        "Estrategia de anuncios en Meta Ads"
    ])

generate_btn = st.button("🔥 Generar Estrategia con IA", use_container_width=True)

# Lógica del Agente
if generate_btn:
    if not api_key:
        st.error("❌ Falta la GEMINI_API_KEY. Configúrala en el archivo .env")
    elif not business_name or not niche:
        st.warning("⚠️ Por favor completa al menos el nombre y el rubro de la empresa.")
    else:
        with st.spinner("🤖 El agente de Gemini está analizando tu mercado y creando la estrategia..."):
            try:
                client = genai.Client(api_key=api_key)
                prompt = f"""
                Eres un Growth Marketer experto de clase mundial y estratega de contenido viral.
                Diseña un plan de choque ultra-específico para:
                - Negocio: {business_name}
                - Rubro: {niche}
                - Audiencia: {target_audience}
                - Meta: {goal}

                Entrega:
                1. 💡 Concepto central de la campaña (El ángulo persuasivo).
                2. 🎬 3 Ideas de videos cortos con ganchos (Hooks) de alta retención para los primeros 3 segundos.
                3. 🎯 Llamado a la acción (CTA) directo para convertir prospectos en ventas.
                
                Usa un formato limpio con emojis, negritas y viñetas ejecutivas.
                """
                
                # Lista de modelos con fallback en caso de saturación
                models_to_try = ["gemini-3.5-flash", "gemini-3.8-flash"]
                response = None
                last_error = None

                for model_name in models_to_try:
                    try:
                        response = client.models.generate_content(
                            model=model_name,
                            contents=prompt
                        )
                        if response and response.text:
                            break
                    except Exception as err:
                        last_error = err
                        continue

                if response and response.text:
                    st.success("✅ ¡Estrategia generada con éxito!")
                    st.markdown(response.text)
                else:
                    st.error(f"Error temporal con los servidores de Google: {last_error}")
                
            except Exception as e:
                st.error(f"Error general: {e}")