
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu


st.set_page_config(page_title="Our Services", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()



# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_Twpva09nPz.json")
lottie_flexible = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_kkubbllp.json")
lottie_personalised = load_lottieurl("https://assets1.lottiefiles.com/private_files/lf30_by9lgy8q.json")
lottie_convenient = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_zsrpgica.json")
lottie_email = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_q2Q6BVY6eB.json")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Our Services")
    st.write(
        "Our services are very reasonably priced and precisely tailored towards your needs to ensure you get the best value for money")

# ---- Cost ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Our Mission")
        st.write("##")
        st.write(
            """
            We believe that every student should have access to quality 
            tutoring, which is why we offer a range of pricing options to 
            meet the needs of all our clients. Our team is dedicated to 
            helping students achieve academic success, and we are committed 
            to providing the highest level of service at a fair price.
            """
        )

    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st_lottie(lottie_personalised,height=300)
    with text_column:
        st.subheader("Our Rates")
        st.write(
            """
            Our rate is typically 50 euros per hour, making it affordable for 
            students to get the support they need to succeed in their 
            studies. Our pricing has been calculated based on the capabilities
            of our tutors and the value we expect to bring to our customers through
            our sessions.
            """
        )
with st.container():
    st.write("---")
    st.write("##")
    text_column,image_column = st.columns((2, 1))
    
    with text_column:
        st.subheader("Video Calling")
        st.write(
            """
            We use Microsoft Teams for our video call sessions to ensure 
            a smooth and reliable learning experience for our students. 
            Microsoft Teams is a powerful platform that provides high-quality 
            video and audio, screen sharing, and real-time collaboration tools. 
            It is also easy to use and accessible from any device, making it 
            convenient for both students and tutors.
            """
        )
        
    with image_column:
        st_lottie(lottie_flexible,height=300)
        
with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st_lottie(lottie_convenient,height=300)
    with text_column:
        st.subheader("Limited Time Offer!")
        st.write(
            """
             At Fledge Grinds, we are excited to announce an exclusive offer 
             for a free half-hour tutoring session. This offer is available 
             until the 31st of January and is a great opportunity for students 
             to try our services and see the benefits firsthand. Our tutors 
             offer personalized support in a variety of subjects, and 
             this free session is a chance for students to get a taste of 
             what we have to offer.

             To take advantage of this offer, simply book a session on our
             website and mention the promo code "FREE30" in the comment box. 
             This offer is limited to one session per student and is only 
             available until the 31st of January, so don't miss out on this 
             opportunity to get a free half-hour of tutoring with Fledge Grinds.
            """
        )
