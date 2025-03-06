import streamlit as st

# App Title
st.title("Clay Counseling Mental Health App")

# Home Screen - Mood Tracker & Navigation
st.header("How are you feeling today?")
mood = st.radio("Select your mood:", ["😊 Happy", "😐 Neutral", "😟 Anxious", "😢 Sad"])

st.subheader("Quick Actions")
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Therapy"):
        st.session_state.page = "therapy"
with col2:
    if st.button("Meditation"):
        st.session_state.page = "meditation"
with col3:
    if st.button("Teletherapy"):
        st.session_state.page = "teletherapy"

# Therapy Section - CBT Exercises & Tips
if st.session_state.get("page") == "therapy":
    st.header("Guided Therapy Exercises")
    st.text_area("Write about what's on your mind:")
    st.write("💡 Therapy Tip: Take deep breaths and focus on the present moment.")
    st.button("Back to Home", on_click=lambda: st.session_state.update(page="home"))

# Meditation & Relaxation
if st.session_state.get("page") == "meditation":
    st.header("Meditation & Relaxation")
    st.write("🌿 Choose a relaxation exercise:")
    st.selectbox("Select Exercise", ["Breathing Exercise", "Mindfulness Meditation", "Progressive Muscle Relaxation"])
    st.button("Start Exercise")
    st.button("Back to Home", on_click=lambda: st.session_state.update(page="home"))

# Teletherapy Booking
if st.session_state.get("page") == "teletherapy":
    st.header("Book a Teletherapy Session")
    st.selectbox("Select a Therapist", ["Dr. April Clay", "John Doe", "Jane Smith"])
    st.date_input("Choose Date")
    st.time_input("Choose Time")
    st.button("Confirm Booking")
    st.button("Back to Home", on_click=lambda: st.session_state.update(page="home"))

# Display the prototype
st.write("🚀 This is an interactive prototype. Future versions will include full authentication & AI chatbot.")
