import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
from datetime import date
import datetime



st.set_page_config(page_title="Book service", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_booking = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_uMjybUoeGN.json")

# ---- HEADER SECTION ----
with st.container():
    image_column, text_column = st.columns((1, 2))
    with text_column:
        st.subheader("Book Your Slot")
        st.write(
        "Welcome to the booking page for Fledge Grinds! Here, you can easily schedule your one-on-one tutoring sessions with our experienced tutors. Simply select your subject, choose your level, and select your desired time and date. You can also choose to book multiple sessions at once. We offer flexible scheduling to fit your busy schedule, and our online platform makes it easy to communicate with your tutor and reschedule or cancel sessions as needed. We look forward to helping you achieve academic success with Fledge Grinds.")
    with image_column:
        st_lottie(lottie_booking,height=300)

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style.css")


with st.container():
    st.write("---")
    st.header("Booking Selection:")
    st.write("##")


    contact_form = """
    <form action="https://formsubmit.co/7272fc785a51c2d5ae0c8c761e91e8aa" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <input type="text" name="subject" placeholder="Subject" required>
        <input type="text" name="level" placeholder="Subject level" required>
        <input type="date" name="date" placeholder="Date" required>
        <input type="time" name="time" placeholder="Time" required>
        <textarea name="message" placeholder="Your code here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)
    
