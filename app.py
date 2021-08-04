import streamlit as st
st.title("🥑 Avocado Analytics!")


def generate_file_name(region, avocado_type, start_date, end_date):
    return f"avocado_{region}_{avocado_type}_{str(start_date)}_{str(end_date)}.csv"


x = st.slider("label for slider", 0, 100, 28)
st.write(x)

st.download_button(
    "LALALEND",
    data=None,
    filepath="lalala.csv"
)

st.download_button(
    "TADADA",
    data=None,
    filepath="mmm/international-migration.csv"
)
