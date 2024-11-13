import streamlit as st

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Detailed Funnel Analysis", "Demographic Analysis"])

# Content for Home Page
if page == "Home":
    st.title("Mosh Hair Loss Funnel Analysis")
    st.write("This is the landing page of the dashboard. Use the sidebar to navigate to detailed analyses.")
    
    # Adjust iframe for figure 6 with reduced white space and zoomed out
    html_file_url1 = "https://joelb-ps.github.io/mosh-streamlit/figure_6.html"
    st.markdown(f'''
        <iframe src="{html_file_url1}" width="90%" height="400px" 
            style="border:none; transform: scale(0.8); transform-origin: 0 0;"></iframe>
        ''', unsafe_allow_html=True)
    
    # Adjust iframe for figure 1 (make it scrollable horizontally and zoomed out)
    html_file_url2 = "https://joelb-ps.github.io/mosh-streamlit/figure_1.html"
    st.markdown(f'''
        <iframe src="{html_file_url2}" width="120%" height="600px" 
            style="border:none; transform: scale(0.8); transform-origin: 0 0;">
        </iframe>
        ''', unsafe_allow_html=True)
    
    # Adjust iframe for mock_1 (make it scrollable horizontally and zoomed out)
    html_file_url3 = "https://joelb-ps.github.io/mosh-streamlit/mock_1.html"
    st.markdown(f'''
        <iframe src="{html_file_url3}" width="120%" height="600px" 
            style="border:none; transform: scale(0.6); transform-origin: 0 0;">
        </iframe>
        ''', unsafe_allow_html=True)

# Content for Detailed Funnel Analysis
elif page == "Detailed Funnel Analysis":
    st.title("Funnel Analysis Dashboard")
    # Adjust iframe for funnel analysis (same as before)
    html_file_url4 = "https://joelb-ps.github.io/mosh-streamlit/funnel_analysis.html"
    st.markdown(f'''
        <iframe src="{html_file_url4}" width="120%" height="600px" 
            style="border:none; transform: scale(0.6); transform-origin: 0 0;">
        </iframe>
        ''', unsafe_allow_html=True)

    # Adjust iframe for time_at_step_1 (same as previous iframe)
    html_file_url5 = "https://joelb-ps.github.io/mosh-streamlit/time_at_step_1.html"
    st.markdown(f'''
        <iframe src="{html_file_url5}" width="120%" height="600px" 
            style="border:none; transform: scale(0.6); transform-origin: 0 0;">
        </iframe>
        ''', unsafe_allow_html=True)

# Content for Demographic Analysis
elif page == "Demographic Analysis":
    st.title("Demographic Analysis")
    # Add content or visualizations related to demographic analysis here
     # Adjust iframe for time_at_step_1 (same as previous iframe)
    html_file_url6 = "https://joelb-ps.github.io/mosh-streamlit/figure_2.html"
    st.markdown(f'''
        <iframe src="{html_file_url6}" width="140%" height="800px" 
            style="border:none; transform: scale(0.6); transform-origin: 0 0;">
        </iframe>
        ''', unsafe_allow_html=True)
