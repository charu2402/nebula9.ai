from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

def load_conversation():
    memory = ConversationBufferMemory()
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        temperature=0,
        google_api_key="AIzaSyC6Wi9Wx6_1NVnuHX8mu2S4qPkoJwkweQw"  # Replace with environment variable or config
    )
    conversation = ConversationChain(llm=llm, memory=memory, verbose=False)
    return conversation
