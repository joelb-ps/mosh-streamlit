import streamlit as st

# URL of your hosted HTML file on GitHub
html_file_url = "https://joelb-ps.github.io/mosh-streamlit/funnel_analysis.html"

# Embed the HTML file in Streamlit using an iframe
st.title("Funnel Analysis Dashboard")

st.markdown(f'<iframe src="{html_file_url}" width="100%" height="800"></iframe>', unsafe_allow_html=True)
