import streamlit as st

with st.echo:
    st.title("Camera image demo!")

    image_file = st.camera_image_input()

    if image_file:
        st.image(image_file.getvalue())

    with st.form(key="key1"):
        x = st.slider("Slider X:", 0, 100, 33)
        image_file_inside_form = st.camera_image_input()
        form_submitted = st.form_submit_button("Submit")

    if form_submitted:
        st.write(f"Slider value X=: {x}")

        if image_file_inside_form:
            st.image(image_file_inside_form.getvalue())

    with st.form(key="key2", clear_on_submit=True):
        y = st.slider("Slider Y:", 0, 100, 42)
        image_file_inside_clear_on_submit_form = st.camera_image_input()
        clear_on_submit_form_submitted = st.form_submit_button("Submit, clear form on submit")

    if clear_on_submit_form_submitted:
        st.write(f"Slider value Y=: {y}")

        if image_file_inside_clear_on_submit_form:
            st.image(image_file_inside_clear_on_submit_form.getvalue())

