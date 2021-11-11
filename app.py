import streamlit as st

with st.echo():
    st.title("Camera image input demo!")

    image_file = st.camera_image_input()

    if image_file:
        st.image(image_file.getvalue())


