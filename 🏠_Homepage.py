
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
from streamlit_option_menu import option_menu


st.set_page_config(page_title="Fledge Grinds", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_rke9huuf.json")
lottie_flexible = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_i7ooqm2q.json")
lottie_personalised = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_fq7pwzey.json")
lottie_convenient = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_ketv1eqz.json")
lottie_email = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_q2Q6BVY6eB.json")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Fledge Grinds Academy")
    st.title("Giving you the edge over your peers!")
    st.write(
        "We offer personalized, expert tutoring in a variety of subjects to help students achieve their academic goals. Each of our tutors in each subject has achieved a H1 in the subject at leaving cert level, to ensure you receive the best possible service.")

# ---- WHAT WE DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What We do")
        st.write("##")
        st.write(
            """
            We are a tutoring service that helps students 
            excel in their studies. Our experienced tutors offer one-on-one 
            support in a variety of subjects, including Maths, Technology, Programming, 
            and more. We tailor our lessons to meet the unique needs and goals of 
            each student and offer flexible scheduling to fit busy schedules. 
            With Fledge Grinds, you'll get the individualized attention you need 
            to succeed in your Leaving cert.
            """
        )
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- Why Us ----
with st.container():
    st.write("---")
    st.header("Why Choose Us?")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st_lottie(lottie_personalised,height=300)
    with text_column:
        st.subheader("Personalised Attention")
        st.write(
            """
            Fledge Grinds offers one-on-one support, allowing our tutors to 
            tailor their lessons to meet the unique needs and goals of 
            each student.
            """
        )
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st_lottie(lottie_flexible,height=300)
    with text_column:
        st.subheader("Flexible scheduling:")
        st.write(
            """
            We understand that students have busy schedules with 
            school, extracurricular activities, and other commitments. 
            That's why we offer flexible scheduling to fit their needs. 
            Whether students prefer early morning, late evening, or 
            weekend sessions, we can accommodate their schedule.
            """
        )
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st_lottie(lottie_convenient,height=300)
    with text_column:
        st.subheader("Convenient learning environment:")
        st.write(
            """
             With Fledge Grinds Academy, students have the ability to learn from the comfort of their own home. 
             This makes it easier for students to fit tutoring into their busy schedules and eliminates 
             the need for transportation. Additionally, our online platform 
             allows for easy communication and scheduling with tutors, 
             making the learning process convenient and hassle-free.
            """
        )

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Us!")
    st.write("##")

    
    contact_form = """
    <form action="https://formsubmit.co/7272fc785a51c2d5ae0c8c761e91e8aa" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st_lottie(lottie_email,height= 300)
        
