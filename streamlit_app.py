import streamlit as st
import os

# Configure Streamlit Page
st.set_page_config(
    page_title="Beesma Sai Varma Keerthipati | AI & ML Engineer",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS to eliminate Streamlit padding/margins for seamless full-page display
st.markdown(
    """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .stDeployButton {display: none;}
        .block-container {
            padding: 0 !important;
            margin: 0 !important;
            max-width: 100% !important;
        }
        iframe {
            border: none !important;
            width: 100% !important;
            min-height: 100vh !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

def get_portfolio_html():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    html_path = os.path.join(base_dir, "index.html")
    css_path = os.path.join(base_dir, "css", "styles.css")
    data_js_path = os.path.join(base_dir, "js", "projects-data.js")
    main_js_path = os.path.join(base_dir, "js", "main.js")
    
    with open(html_path, "r", encoding="utf-8") as f:
        html_content = f.read()
        
    with open(css_path, "r", encoding="utf-8") as f:
        css_content = f.read()
        
    with open(data_js_path, "r", encoding="utf-8") as f:
        data_js_content = f.read()
        
    with open(main_js_path, "r", encoding="utf-8") as f:
        main_js_content = f.read()
        
    # Embed CSS & JS directly into HTML
    html_content = html_content.replace(
        '<link rel="stylesheet" href="css/styles.css">',
        f'<style>{css_content}</style>'
    )
    
    html_content = html_content.replace(
        '<script src="js/projects-data.js"></script>',
        f'<script>{data_js_content}</script>'
    )
    
    html_content = html_content.replace(
        '<script src="js/main.js"></script>',
        f'<script>{main_js_content}</script>'
    )
    
    return html_content

# Render the complete interactive portfolio
portfolio_html = get_portfolio_html()
st.components.v1.html(portfolio_html, height=4800, scrolling=True)
