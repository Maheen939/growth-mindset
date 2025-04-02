#streamlit
import streamlit as st

st.set_page_config(page_title= "growth mindset project" , page_icon ="⭐")
st.title("Growth mindset Challenge: Web App with streamlit")

st.header("Welcome to your Growth Journey")
st.write("Embrace challennge, learn from mistakes, and unlock your full potential. This AI-powered app help")

#quote section
st.header("Todays Growth Mindset quote")
st.write('"Success is not final, failure is not fatal : it is the courage to continue that counts." - Wintson Churchill"')

st.header("What's your challange today?")
user_input = st.text_input("Describe a challenge you're facing") 

#condition
if user_input:
    st.success(f"you're facing: {user_input}. Keep pushing forward towards your goal!")
else:
    st.warning("Tell us about challenge to get started!")

#reflexing
st.header("Reflect on your learning")
reflection = st.text_area("Write your reflections here:")

if reflection:
    st.success(f"Great insight! Your reflection: {reflection} ")
else:
    st.info("Reflection on past experience help you grow! Share your difficulties")

#achievements
st.header("Celebrate your win!")
acheivment = st.text_input("Share something you've recently accomplished:")




if acheivment:
    st.success(f"Amazing! You achieved: {acheivment}")
else:
    st.info("Big or small, every acheivement counts! Share one now")


    #footer
    st.write("- - -")
    st.write("Keep beliving in yourself. Growth is a journey, not a destination! 🌟")
    st.write(" created by Maheen Ashraf")
    