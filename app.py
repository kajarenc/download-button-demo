import streamlit as st

with st.echo():
    st.title("Download button filepath experiment")

    x = st.slider("label for slider", 0, 100, 28)
    st.write(x)

    st.download_button(
        "39 MB file",
        data=None,
        filepath="lalala.csv"
    )

    st.download_button(
        "39 mb file nested in directory",
        data=None,
        filepath="mmm/international-migration.csv"
    )
