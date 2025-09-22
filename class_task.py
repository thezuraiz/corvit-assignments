import streamlit as st


st.title("For H1 Purpose")
st.text("For Paragraphs Purpose")
st.write("Also For Paragraphs Purpose")
st.header("For H2 Purpose")
st.subheader("For H3 Paragraphs Purpose")

st.markdown("# H1") # - space after # is compulsory
st.markdown("## H2")
st.markdown("### H3")
st.markdown("#### H4")
st.markdown("##### H5")

# 22-Sep-2025
# To run a file, use `streamlit run (fileName).py`.
# To run the demo template, use `streamlit hello`.

from PIL import Image
st.success("This is an success message")
st.warning("This is an warning message")
st.error("This is an error message")

# to use Image we have to install pillow
# `pip install pillow`
img = Image.open("8-SEAT-PIPE-NEW-MODEL-70CC.webp") # To Load Image (Recommended)
# img = ("8-SEAT-PIPE-NEW-MODEL-70CC.webp") # Jugari Method
st.image(img) # To print image

# Check Boxes
if(st.checkbox("Show/Hide Image")):
    st.image(img)
else:
    st.warning("Click Check to show Image")

status =st.radio("Select Gender:", ["Male", "Female","Shemale"])
if status == "Male":
    st.success("Male")
elif status == "Female":
    st.error("Women ☕️")
else:
    st.warning("Something went wrong!")

# Select Box
st.selectbox("Options:",["Haha","Hehe","Hoho"])

# Multi Select
hubbies = st.multiselect("Hobbies",["Dancing","Sport","Development"])

# Button
isDisabled =False
b = st.button("Login" ,disabled=isDisabled,type="secondary",help="You're mouse on Login Button",icon="❤️‍🩹")
if b:
    isDisabled = True
    st.success(f"You are logged in..! {isDisabled}")
else:
    st.warning("Authentication Required")

# Slides
st.write("Slides") # for paragraph
s = st.slider("Slides",0,100)

#input Box
msg = st.text_input("Enter Degress");
st.text(f"msg: {msg}")

msg = st.chat_input("Enter degress"); #for chat
st.text(f"msg: {msg}")

age = st.number_input("Enter Age");
st.text(f"msg: {age}")

dob = st.date_input("Enter Date of Birth");
st.text(f"msg: {dob}")

# Camera
# iAm =st.camera_input("Image: ");
# st.image(iAm)

# to add video
st.video("https://youtu.be/O73WrKQy2Tg?si=-B9dH1Rax_lFFmW2");

# Assignment
# Developer Temp Calculator
# Radio Input => Select Units for Temperature
# Input => Enter Temperature in (selected unit (C/F))
# Convert Button
# Output
# => Temperature in Cel
# => Temperature in Kelvin
