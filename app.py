import streamlit as st


st.title("Camera image demo!")

image_file = st.camera_image_input()

if image_file:
    st.image(image_file.getvalue())

