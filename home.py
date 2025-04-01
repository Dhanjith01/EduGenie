import streamlit as st
import subprocess

def main():
    st.set_page_config(page_title="AI Study Assistant", layout="centered")
    
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://img.freepik.com/premium-vector/beautiful-mountains-vector-illustration-design_825609-284.jpg");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    
    # Bold Welcome Message
    st.title("📚 Welcome to Your AI Study Assistant! 🎓")
    
    # Description
    st.write("""
    This AI-powered assistant helps you stay on top of your studies and manage stress effectively.
    Whether you need help with your coursework or just need someone to talk to, we've got you covered!
    """)
    
    # Buttons
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Start Study Session 🚀"):
            subprocess.Popen(["streamlit", "run", "chatpdf1.py"])
    
    with col2:
        if st.button("Need Help with Stress or Anxiety? 💙"):
            subprocess.Popen(["streamlit", "run", "mentalhealth_chatbot.py"])

if __name__ == "__main__":
    main()
