import streamlit as st

# Sidebar Navigation
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go to:", ["About Me", "Education", "Work Experience", "Skills", "Projects"])

# About Me Page
if page == "About Me":
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("FATIN.jpg", width=150) 
    with col2:
        st.title("Fatin Nurasiyah binti Abdul Rahim")
        st.write("📧 rhfatin@gmail.com | 📱 (+60) 16-480-5956")
        st.markdown("🔗 [LinkedIn](https://www.linkedin.com/in/fatin-nurasiyah)")
        st.write("🆔 NRIC: 020324-02-0672")

    st.markdown("---")
    st.subheader("👩‍💻 About Me")
    st.write("""
    I am a motivated Information Technology student at University of Malaysia, Kelantan,
    passionate about software development, IoT projects, and mobile app design.
    I enjoy solving real-world problems through innovative technology solutions.
    """)

# Education Page
elif page == "Education":
    st.header("🎓 Education")
    st.write("**Bachelor in Information Technology**, University of Malaysia, Kelantan (2023–2027)")

# Work Experience Page
elif page == "Work Experience":
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

# Skills Page
elif page == "Skills":
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

# Projects Page
elif page == "Projects":
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

