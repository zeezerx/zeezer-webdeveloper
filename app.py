#---------- D3vsxnpai ----------
# - Importing required dependencies -
from PIL import Image
import requests
import streamlit as st

#        Page Config        

st.set_page_config(page_title="Zeezer - Web Developer", page_icon=":star_struck:", layout="centered")

#        Local CSS

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")


#        Assets

img_sticker1 = Image.open("Images/sticker1.png")

#        Header section

with st.container():
    st.subheader("Don't have a website for your Content ?")
    st.title("Well I can solve that")
    st.write("I can make you a light-weight website ASAP at a very LOW COST")
    st.write("Contace me on my [Instagram](https://www.instagram.com/zeezer.x/) for more Info or you can contact me through the contact form below ;)")

#        About myself

st.write("---")
left_column, right_column = st.columns(2)
with left_column:
    st.header("What I do ")
    st.write("##")
    st.write(
        """I am a part-time webdeveloper & a student.
        I can make you a light-weight website like this one
        at a very low cost. If you run a small company or you are a 
        youtuber, fell free to contact me.
        As a student I try to keep the cost as low as possible.
        ^_^
        """
    )

#        sticker1
st.image(img_sticker1, width=500)

#        Contact form

st.write("---")
st.header("Contact me !")
st.write("##")
contact_form = """
     <input type="hidden" name="_captcha" vlue="false">
     <form action="https://formsubmit.co/zeezersucks@gmail.com" method="POST">
     <input type="text" name="name" placeholder="Your Name"required>
     <input type="email" name="email" placeholder="Your Email" required>
     <textarea name="message" placeholder="Your message here" requited></textarea>
     <button type="submit">Send</button>
</form>
"""
left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()

#        Background Image

hide_streamlit_style = """
            <style>
            [data-testid="stToolbar"] {visibility: hidden !important;}
            footer {visibility: hidden !important;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)






