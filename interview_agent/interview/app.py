import streamlit as st
from utils.pdf_parser import extract_text_from_pdf
from utils.audio import text_to_speech, listen_live
from utils.state import init_session_state

# Initialize session state
init_session_state()

# Streamlit UI
st.set_page_config(page_title="AI Interview Agent", layout="centered")
st.title("🎙 Voice-Enabled Interview Agent")
st.markdown("Upload Resume and JD, then have a voice/text interview with AI.")

resume_file = st.file_uploader("Upload Candidate Resume (PDF)", type="pdf")
jd_file = st.file_uploader("Upload Job Description (PDF)", type="pdf")

if resume_file and jd_file and not st.session_state['interview_started']:
    resume_text = extract_text_from_pdf(resume_file)
    jd_text = extract_text_from_pdf(jd_file)
    st.success("Files uploaded and parsed successfully!")

    if st.button("Start Interview"):
        prompt = f"""You are an AI recruiter...
        Resume:
        {resume_text[:1000]}

        Job Description:
        {jd_text[:1000]}
        Start by asking your first technical question..."""
        response = st.session_state['conversation'].predict(input=prompt)
        st.session_state['chat_history'].append(("AI", response))
        st.session_state['interview_started'] = True
        st.session_state['rounds'] = 1
        st.chat_message("AI").write(response)
        text_to_speech(response)

if st.session_state['interview_started']:
    st.markdown("### 🎤 Respond with your voice (mic) or type your response")
    col1, col2 = st.columns([2, 1])
    with col1:
        text_response = st.text_input("Type your response")
    with col2:
        if st.button("🎙 Speak Now"):
            voice_input = listen_live()
            st.session_state['last_voice_input'] = voice_input
        else:
            voice_input = st.session_state.get('last_voice_input', "")

    user_input = text_response or voice_input

    if user_input and st.session_state['rounds'] <= 6:
        st.chat_message("Human").write(user_input)
        st.session_state['chat_history'].append(("Human", user_input))
        prompt = f"""The candidate just responded:
        "{user_input}"
        Ask the next relevant question."""
        response = st.session_state['conversation'].predict(input=prompt)
        st.chat_message("AI").write(response)
        text_to_speech(response)
        st.session_state['chat_history'].append(("AI", response))
        st.session_state['rounds'] += 1

    if st.session_state['rounds'] > 6:
        if st.button("📝 Generate Interview Summary"):
            history = "\n".join([f"{role}: {msg}" for role, msg in st.session_state['chat_history']])
            summary_prompt = f"""Create a structured interview summary with:
            - Name
            - Skills Match
            - Traits
            - Improvements
            - Fit Score
            Chat Transcript:
            {history}
            """
            summary = st.session_state['conversation'].predict(input=summary_prompt)
            st.markdown("### 📄 Interview Summary")
            st.write(summary)
            st.download_button("📥 Download Summary", summary, file_name="interview_summary.txt")
