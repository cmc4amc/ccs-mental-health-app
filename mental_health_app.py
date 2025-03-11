import streamlit as st
import firebase_admin
from firebase_admin import auth, credentials, firestore
import datetime

# Initialize Firebase
if not firebase_admin._apps:
    cred = credentials.Certificate("ccs-wellness-app-firebase-adminsdk-fbsvc-e6536a365c.json")
    firebase_admin.initialize_app(cred)

db = firestore.client()

# Streamlit App UI
st.title("Clay Counseling Mental Health App")

# User Authentication
st.sidebar.header("User Authentication")
choice = st.sidebar.selectbox("Login/Signup", ["Login", "Signup"])
email = st.sidebar.text_input("Email")
password = st.sidebar.text_input("Password", type="password")

if st.sidebar.button("Submit"):
    try:
        if choice == "Signup":
            user = auth.create_user(email=email, password=password)
            st.sidebar.success("Account created! Please log in.")
        else:
            user = auth.get_user_by_email(email)
            st.sidebar.success("Logged in successfully!")
    except Exception as e:
        st.sidebar.error(f"Error: {e}")

# Mood Tracker
st.header("How are you feeling today?")
mood = st.radio("Select your mood:", ["😊 Happy", "😐 Neutral", "😟 Anxious", "😢 Sad"])
if st.button("Save Mood"):
    db.collection("users").document(email).collection("mood_logs").add({
        "mood": mood,
        "timestamp": datetime.datetime.now()
    })
    st.success("Mood saved!")

# Therapy Notes
st.header("Therapy Journal")
therapy_note = st.text_area("Write your thoughts:")
if st.button("Save Note"):
    db.collection("users").document(email).collection("therapy_notes").add({
        "note": therapy_note,
        "timestamp": datetime.datetime.now()
    })
    st.success("Note saved!")

# AI Chatbot
st.header("AI Chatbot for Mental Health Support")
user_input = st.text_input("Ask the chatbot anything about mental health:")
if st.button("Get Response"):
    response = f"I understand that you're feeling {mood}. Try a breathing exercise or journaling to help!"
    st.write(response)

st.sidebar.button("Logout")
