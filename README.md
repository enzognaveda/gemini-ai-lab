# 🚀 AI Growth & Marketing Copilot

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://enzonaveda-growth-copilot.streamlit.app/)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Google Gemini API](https://img.shields.io/badge/Google%20GenAI-Gemini%20API-orange)](https://aistudio.google.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An enterprise-grade autonomous marketing copilot that engineers viral video hooks, high-converting copy, and audience-targeted acquisition funnels in seconds. Powered by **Google Gemini** multimodal models and deployed on **Streamlit Cloud**.

🔗 **Live Production App:** [https://enzonaveda-growth-copilot.streamlit.app/](https://enzonaveda-growth-copilot.streamlit.app/)

---

## 🌟 Key Features

- **⚡ Multi-Model Resilient Fallback Architecture:** Engineered an automatic failover mechanism between `gemini-3.5-flash` and `gemini-3.8-flash` to mitigate server latency and handle quota spikes with zero downtime.
- **🎯 0-3s Hook Engineering:** Generates high-retention video hooks specifically tailored for short-form video algorithms (TikTok, Instagram Reels, YouTube Shorts).
- **💡 Actionable Growth Blueprints:** Delivers end-to-end campaign concepts, storytelling pacing, dynamic caption styling, and direct-response CTAs.
- **🔒 Enterprise Security Standards:** Complete environment isolation with decoupled credentials using `.env` local protection and Streamlit Cloud encrypted secrets.

---

## 🛠️ Tech Stack & Architecture

- **Backend & Logic:** Python, `google-genai` SDK
- **Frontend / Cloud Deployment:** Streamlit Community Cloud
- **LLM Engine:** Google Gemini (`gemini-3.5-flash` / `gemini-3.8-flash`)
- **Version Control & CI/CD:** Git, GitHub Desktop

```text
[ User Input (Brand, Niche, Goal) ]
                │
                ▼
[ Streamlit Client UI ] ───► [ Environment Variables (.env / Secrets) ]
                │
                ▼
[ Resilient AI Router ]
        ├──► Try: Gemini 3.5 Flash (Primary)
        └──► Fallback: Gemini 3.8 Flash (Auto-failover)
                │
                ▼
[ Structured Growth Strategy & Viral Hooks Output ]
```

---

## 🚀 Local Installation & Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/enzognaveda/gemini-ai-lab.git
   cd gemini-ai-lab
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables:** Create a `.env` file in the root directory:

   ```env
   GEMINI_API_KEY=your_google_gemini_api_key_here
   ```

4. **Launch Application:**

   ```bash
   streamlit run app.py
   ```

---

## 👨‍💻 Author

**Enzo G. Naveda**

- **LinkedIn:** Enzo Mateo Garcia Naveda
- **GitHub:** [@enzognaveda](https://github.com/enzognaveda)
- **Credly Badges:** Verified Google Cloud Credentials
- **Location:** Ancash, Peru (Available for Global Remote Opportunities)