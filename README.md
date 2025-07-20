# nebula9.ai
Automated Candidate Interview Agent
<img width="747" height="336" alt="image" src="https://github.com/user-attachments/assets/d1236e00-00b5-4502-8c06-9fd6ea2a5d25" />




# 🎙️ AI-Powered Interview Agent (Gemini + Real-Time Voice Input)

This is a voice-enabled AI Interview Agent built using **Google Gemini**, **Streamlit**, and **SpeechRecognition**, capable of conducting real-time screening interviews using both **text and voice input**.

It analyzes the candidate's **resume** and the **job description**, asks personalized questions (technical, behavioral, situational), and gives a structured **summary** at the end — all in a friendly, dynamic chat interface.

---

## 🚀 Features

✅ Upload **Resume + JD (PDF)**  
✅ Real-time **Voice or Text Input**  
✅ **AI-generated Questions** tailored to the candidate  
✅ AI replies in **text + voice (TTS)**  
✅ Automatic **follow-up** Q&A for 6 rounds  
✅ Generates a **summary report** at the end  

## 🖼️ Demo
<img width="876" height="641" alt="image" src="https://github.com/user-attachments/assets/163cc2c7-a59b-46fa-bfd4-30022ebc611f" />
❓❓**sample questions**
![WhatsApp Image 2025-07-20 at 12 34 56_c7cafff4](https://github.com/user-attachments/assets/3296047d-e73f-4421-9838-e0a9de8e4224)
![WhatsApp Image 2025-07-20 at 12 35 29_6b699a9a](https://github.com/user-attachments/assets/0300ad44-cd19-4585-bc58-1b4826892264)

![WhatsApp Image 2025-07-20 at 12 37 45_3327f3b5](https://github.com/user-attachments/assets/3ee3335e-d4d1-488b-9971-3a96fd18f953)

**Interview report**
![WhatsApp Image 2025-07-20 at 12 38 48_63bbb3f1](https://github.com/user-attachments/assets/ea5a1bd3-3a6b-4dc5-b5af-c55e9f029958)






---

## 🧠 Tech Stack

- 🌐 [Streamlit](https://streamlit.io/) — UI
- 🧠 [Gemini Pro](https://ai.google.dev/) via LangChain — LLM
- 🗣️ [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) — Live mic input
- 🔊 [pyttsx3](https://pypi.org/project/pyttsx3/) — Text-to-speech (offline)

---

## 📂 Project Files
interview_agent/
├── app.py # Main Streamlit app
├── agents/
│ └── interviewer.py # Gemini model loading and conversation logic
├── utils/
│ ├── audio.py # Speech recognition & text-to-speech
│ ├── pdf_parser.py # PDF text extraction
│ └── state.py # Session state management
└── requirements.txt # Project dependencies


---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/interview-agent.git
cd interview-agent
**### 2. Create and Activate Virtual Environment (Recommended)**
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
###**3. Install Dependencies**
pip install -r requirements.txt

**🔐 Google Gemini API Setup**
Go to Google AI Studio
https://aistudio.google.com/apikey
Create and copy your Gemini API key

Use one of the following options:

**Option 1:** Add to Code (quick)
In agents/interviewer.py, replace:
google_api_key="YOUR_API_KEY"
**Option 2:** Use Environment Variable (secure)
export GOOGLE_API_KEY="your-api-key"
Then in your code:
import os
google_api_key = os.getenv("GOOGLE_API_KEY")

**▶️ Run the App**
streamlit run app.py
The app will open in your browser at: http://localhost:8501

**🎯 How It Works**
1.Upload your resume and job description (PDF)
2.Click "Start Interview"
3.AI will begin asking questions
4.Respond by typing or clicking "Speak Now"
5.After 6 rounds, click "Generate Interview Summary"

**🛠️ Tech Stack**
1.Frontend: Streamlit
2.Backend: Python
3.LLM: Google Gemini via LangChain
4.Speech: SpeechRecognition + pyttsx3
5.Parsing: PyPDF2
**
📌 Requirements**
streamlit
PyPDF2
langchain
langchain-google-genai
speechrecognition
pyttsx3


