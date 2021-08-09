import streamlit as st

with st.echo():

    def click_handler():
        st.download_button(
            "This download button will not be rendered",
            data="Hello world!",
            file_name="justtext.txt",
            autodownload=True
        )

    st.title("Download button filepath experiment")
    st.button("REGULAR BUTTON", on_click=click_handler)

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

    st.download_button(
        "80 mb file",
        data=None,
        filepath="2mSalesRecords.zip"
    )
