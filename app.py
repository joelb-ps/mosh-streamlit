import streamlit as st

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Detailed Funnel Analysis", "Demographic Analysis"])

# Content for Home Page
if page == "Home":
    st.title("Mosh Hair Loss Funnel Analysis")
    st.write("This is the landing page of the dashboard. Use the sidebar to navigate to detailed analyses.
             ")

# Content for Detailed Funnel Analysis
elif page == "Detailed Funnel Analysis":
    st.title("Funnel Analysis Dashboard")
    html_file_url = "https://joelb-ps.github.io/mosh-streamlit/funnel_analysis.html"
    st.markdown(f'<iframe src="{html_file_url}" width="100%" height="800"></iframe>', unsafe_allow_html=True)

# Content for Demographic Analysis
elif page == "Demographic Analysis":
    st.title("Demographic Analysis")
    # Add content or visualizations related to demographic analysis here
    st.write("This page will show demographic analysis. You can add charts, tables, or any analysis here.")
