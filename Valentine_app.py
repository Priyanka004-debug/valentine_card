import streamlit as st
from PIL import Image
#1.Page configuration
st.set_page_config(page_title="For my Wonderful Husband", page_icon="❤️")
#2.Main title
st.title("Happy Valentine's Day My Love! ❤️")
#3.Add some balloons
st.audio("music.mp3.mpeg")
#4.Introduction
st.write("To my dearest husband, on this special day, I want to remind you how much you mean to me. You are my rock, my best friend, and the love of my life.")
#5.Special message
st.header("To the Love of My Life")
# 1. Open and Rotate (Keep this as is)
img = Image.open("RJ109494.JPG")
rotated_image = img.rotate(90, expand=True) 
st.image(rotated_image,caption="Our Special Moment (28-09-2025)",use_container_width=True)
#An interactive button
if st.button("Click Me for a Surprise!"):
    st.write("You are my everything! ❤️❤️❤️")
    
    st.markdown("### You are my favourite 'True'in the universe of Booleans!")

    st.write("I Love You more than Python loves indentation! 🐍❤️")






