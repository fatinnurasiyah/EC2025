import streamlit as st

st.set_page_config(page_title="Fatin Nurasiyah | Resume", layout="wide")

col1, col2 = st.columns([1, 3])

with col1:
    st.image("profile.jpg", width=180)  

with col2:
    st.title("Fatin Nurasiyah binti Abdul Rahim")
    st.markdown("""
    **Email:** rhfatin@gmail.com  
    **Phone:** (+60) 16-480-5956  
    **LinkedIn:** [linkedin.com/in/fatin-nurasiyah](https://www.linkedin.com/in/fatin-nurasiyah)  
    """)

st.markdown("---")

col3, col4 = st.columns(2)

with col3:
    st.header("🎓 Education")
    st.markdown("""
    **Bachelor in Information Technology**  
    *University of Malaysia, Kelantan* (2023–2027)
    """)

with col4:
    st.header("💼 Work Experience")
    st.subheader("Internship – Asia Tech Biz Sdn Bhd (6 months)")
    st.markdown("""
    - Assisted in IT-related tasks  
    - Gained exposure to real-world business systems
    """)

    st.subheader("Crew (F&B) – 2 years")
    st.markdown("""
    - Provided customer service in food & beverage operations  
    - Handled orders, ensured customer satisfaction, and maintained service quality
    """)

    st.subheader("Stokis – Chocojar Business (1 year)")
    st.markdown("""
    - Managed small business operations including sales, marketing, and stock management
    """)

st.markdown("---")

st.header("🛠 Skills")
col5, col6 = st.columns(2)

with col5:
    st.markdown("""
    **Programming Languages**  
    - Java  
    - C++  
    """)

with col6:
    st.markdown("""
    **Web Development**  
    - HTML  
    - Flutter  
    """)

st.markdown("---")

st.header("📂 Projects")

st.subheader("Security Smart Home Automation (Diploma Project)")
st.markdown("""
- Controlled home appliances (lights and fans) automatically  
- Integrated alarm system with phone notifications in case of intrusions
""")

st.subheader("Automated Vending Machine for Prescription Medication (Degree Group Project)")
st.markdown("""
- Built an IoT-based vending system using ESP32-CAM and QR code  
- Dispensed medicine efficiently to reduce patient waiting times
""")

st.subheader("TRIPJR Travel App (Degree Group Assignment)")
st.markdown("""
- Developed a Flutter-based travel application  
- Enabled users to search and book nearby hotels or homestays for vacations
""")


st.header("⭐ Certifications & Extracurricular")
st.markdown("""
- Volunteer: Kelantan Outing Camera Camp (KOCC)  
- Facilitator: Kem Remajaku Sejahtera, Kedah (2024)  
- Committee: Mutiara Selawat Permata Ilmu Program
""")

# --- FOOTER ---
st.markdown("---")
st.markdown("💡 *This interactive resume was built with Streamlit.*")
