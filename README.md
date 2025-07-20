# nebula9.ai

❓ **Problem Statement**  
Traditional hiring processes often rely on manual, time-consuming screening interviews that can be inconsistent and biased. Recruiters spend a significant amount of time reviewing resumes, comparing them with job descriptions, and conducting initial interviews — often without a standardized structure.  

The challenge is to automate and streamline the early-stage interview process using AI, ensuring:

Efficient candidate screening

Context-aware, adaptive questioning

Consistent evaluation based on resume and job description

Support for both voice and text interactions for accessibility and realism

This project aims to build an intelligent AI interview agent that can simulate real-time interviews using voice and text, evaluate candidate responses in context, and generate structured summaries — saving time and increasing the efficiency of recruitment workflows. 



<img width="747" height="336" alt="image" src="https://github.com/user-attachments/assets/d1236e00-00b5-4502-8c06-9fd6ea2a5d25" />


---


# 🎙️ AI-Powered Interview Agent 

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


  ---
  
❓❓**sample questions**

![WhatsApp Image 2025-07-20 at 12 34 56_c7cafff4](https://github.com/user-attachments/assets/3296047d-e73f-4421-9838-e0a9de8e4224)

![WhatsApp Image 2025-07-20 at 12 35 29_6b699a9a](https://github.com/user-attachments/assets/0300ad44-cd19-4585-bc58-1b4826892264)

![WhatsApp Image 2025-07-20 at 12 37 45_3327f3b5](https://github.com/user-attachments/assets/3ee3335e-d4d1-488b-9971-3a96fd18f953)

---

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
│ └── interviewer.py  #Gemini model loading and conversation logic  
├── utils/  
│ ├── audio.py  #Speech recognition & text-to-speech  
│ ├── pdf_parser.py   #PDF text extraction  
│ └── state.py  #Session state management  
└── requirements.txt  #Project dependencies  


---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/interview-agent.git
cd interview-agent
**### 2. Create and Activate Virtual Environment (Recommended)**
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
2. Install Dependencies
Make sure Python 3.8+ is installed. Then:

```bash
pip install -r requirements.txt
```

3. Set Your Google Gemini API Key
Replace "YOUR_API_KEY" in agents/interviewer.py with your actual API key from Google AI Studio

4. Run the App
```bash
streamlit run app.py
```
Then open the app in your browser: http://localhost:8501

---

📦 Future Improvements  
📼 Video-based candidate feedback

💾 Database to store results

🧑‍🏫 AI rating rubric per skill

📊 Analytics Dashboard

---



