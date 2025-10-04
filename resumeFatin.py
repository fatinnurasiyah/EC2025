import streamlit as st

# ============ PAGE SETTINGS ============
st.set_page_config(page_title="Resume - Fatin Nurasiyah", layout="wide")

# ============ HEADER SECTION ============
with st.container():
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("FATIN.jpg", width=130)
    with col2:
        st.title("Fatin Nurasiyah Abdul Rahim")
        st.write("📧 rhfatin@gmail.com | 📱 (+60) 16-480-5956")
        st.markdown("[🔗 LinkedIn](https://www.linkedin.com/in/fatin-nurasiyah-21559b129?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app)")
st.markdown("---")

# ============ EDUCATION ============
with st.container():
    st.header("🎓 Education")
    st.write("**Bachelor in Information Technology**, University of Malaysia, Kelantan (2023–2027)")
st.markdown("---")

# ============ WORK EXPERIENCE ============
with st.container():
    st.header("💼 Work Experience")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Internship (Diploma)")
        st.write("**Asia Tech Biz Sdn Bhd** | 6 months")
        st.markdown("""
        - Assisted in IT-related tasks  
        - Gained exposure to real-world business systems
        """)

    with col2:
        st.subheader("Crew (F&B)")
        st.write("**Food & Beverage Operations** | 2 years")
        st.markdown("""
        - Provided customer service  
        - Handled orders, ensured customer satisfaction, maintained quality
        """)

    st.subheader("Stokis Business – Chocojar (1 year)")
    st.markdown("""
    - Managed stock distribution and customer engagement  
    - Enhanced sales through effective marketing strategies
    """)
st.markdown("---")

# ============ SKILLS ============
with st.container():
    st.header("⚡ Skills")
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
st.markdown("---")

# ============ PROJECTS ============
with st.container():
    st.header("🚀 Projects")

    st.subheader("Security Smart Home Automation (Diploma Project)")
    st.markdown("""
    - Controlled lights & fans automatically  
    - Integrated alarm system with phone notifications for intrusions
    """)

    st.subheader("Automated Vending Machine for Prescription Medication (Degree Group Project)")
    st.markdown("""
    - IoT-based vending system using ESP32-CAM & QR code  
    - Dispensed medicine to reduce patient waiting times
    """)

    st.subheader("TRIPJR Travel App (Degree Group Assignment)")
    st.markdown("""
    - Flutter-based travel app  
    - Enabled hotel & homestay search + booking
    """)

# ============ FOOTER ============
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>© 2025 Fatin Nurasiyah Abdul Rahim</p>", unsafe_allow_html=True)
