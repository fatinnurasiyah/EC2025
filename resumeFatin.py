import streamlit as st

# ============ PAGE SETTINGS ============
st.set_page_config(page_title="Resume - Fatin Nurasiyah", layout="wide")

# ============ CUSTOM CSS ============
st.markdown("""
    <style>
    .main {
        background-color: #fafafa;
        padding: 2rem;
    }

    /* Header styles */
    h1 {
        font-size: 2rem !important;
        color: #2c3e50;
        margin-bottom: 0.3rem;
    }
    h2 {
        font-size: 1.3rem !important;
        color: #1a73e8;
        margin-top: 1.8rem;
        margin-bottom: 0.6rem;
    }
    h3 {
        font-size: 1.1rem !important;
        color: #333333;
        margin-top: 1rem;
        margin-bottom: 0.3rem;
    }

    p, li {
        font-size: 1rem !important;
        color: #444444;
        line-height: 1.5;
    }

    hr {
        margin-top: 1.5rem;
        margin-bottom: 1.5rem;
        border: 1px solid #e0e0e0;
    }

    /* Reduce gap between image and text columns */
    [data-testid="column"] {
        padding-top: 0 !important;
        padding-bottom: 0 !important;
        margin-top: 0 !important;
        margin-bottom: 0 !important;
    }

    /* Adjust spacing specifically for header */
    .header-container {
        margin-bottom: 0.5rem;
    }

    .footer {
        text-align: center;
        color: gray;
        margin-top: 2rem;
        font-size: 0.9rem;
    }
    </style>
""", unsafe_allow_html=True)

# ============ HEADER SECTION ============
with st.container():
    st.markdown("<div class='header-container'>", unsafe_allow_html=True)
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("FATIN.jpg", width=150)
    with col2:
        st.markdown("<h1>Fatin Nurasiyah Abdul Rahim</h1>", unsafe_allow_html=True)
        st.write("📧 rhfatin@gmail.com | 📱 (+60) 16-480-5956")
        st.markdown("[🔗 LinkedIn](https://www.linkedin.com/in/fatin-nurasiyah-21559b129)")
    st.markdown("</div>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# ============ EDUCATION ============
with st.container():
    st.markdown("<h2>🎓 Education</h2>", unsafe_allow_html=True)
    st.write("**Bachelor in Information Technology**, University of Malaysia, Kelantan (2023–2027)")
st.markdown("<hr>", unsafe_allow_html=True)

# ============ WORK EXPERIENCE ============
with st.container():
    st.markdown("<h2>💼 Work Experience</h2>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<h3>Internship (Diploma)</h3>", unsafe_allow_html=True)
        st.write("**Asia Tech Biz Sdn Bhd** | 6 months")
        st.markdown("""
        - Assisted in IT-related tasks  
        - Gained exposure to real-world business systems
        """)

    with col2:
        st.markdown("<h3>Crew (F&B)</h3>", unsafe_allow_html=True)
        st.write("**Food & Beverage Operations** | 2 years")
        st.markdown("""
        - Provided customer service  
        - Handled orders, ensured customer satisfaction, maintained quality
        """)

    st.markdown("<h3>Stokis Business – Chocojar (1 year)</h3>", unsafe_allow_html=True)
    st.markdown("""
    - Managed stock distribution and customer engagement  
    - Enhanced sales through effective marketing strategies
    """)
st.markdown("<hr>", unsafe_allow_html=True)

# ============ SKILLS ============
with st.container():
    st.markdown("<h2>⚡ Skills</h2>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        - **Programming Languages:** Java, C++  
        - **Web Development:** HTML, Flutter
        """)

    with col2:
        st.markdown("""
        - Strong communication & teamwork  
        - Business & marketing experience  
        - Customer service excellence
        """)
st.markdown("<hr>", unsafe_allow_html=True)

# ============ PROJECTS ============
with st.container():
    st.markdown("<h2>🚀 Projects</h2>", unsafe_allow_html=True)

    st.markdown("<h3>Security Smart Home Automation (Diploma Project)</h3>", unsafe_allow_html=True)
    st.markdown("""
    - Controlled lights & fans automatically  
    - Integrated alarm system with phone notifications for intrusions
    """)

    st.markdown("<h3>Automated Vending Machine for Prescription Medication (Degree Group Project)</h3>", unsafe_allow_html=True)
    st.markdown("""
    - IoT-based vending system using ESP32-CAM & QR code  
    - Dispensed medicine to reduce patient waiting times
    """)

    st.markdown("<h3>TRIPJR Travel App (Degree Group Assignment)</h3>", unsafe_allow_html=True)
    st.markdo
