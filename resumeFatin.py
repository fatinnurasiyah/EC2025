import streamlit as st

# 1️⃣ Setup page
st.set_page_config(page_title="Resume - Fatin Nurasiyah", layout="wide")

# 2️⃣ Compact layout (kurangkan ruang antara seksyen)
st.markdown("""
<style>
    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
        padding-left: 3rem;
        padding-right: 3rem;
    }
    h1, h2, h3 {
        margin-bottom: 0.2rem;
    }
    p {
        margin-bottom: 0.3rem;
    }
</style>
""", unsafe_allow_html=True)

# 3️⃣ Header section
col1, col2 = st.columns([1, 3])
with col1:
    st.image("FATIN.jpg", width=120)
with col2:
    st.title("Fatin Nurasiyah Abdul Rahim")
    st.write("📧 rhfatin@gmail.com | 📱 (+60) 16-480-5956")
    st.markdown("[🔗 LinkedIn](https://www.linkedin.com/in/fatin-nurasiyah)")

st.write("---")

# 4️⃣ Education
st.subheader("🎓 Education")
st.write("**Bachelor in Information Technology**, University of Malaysia, Kelantan (2023–2027)")

st.write("---")

# 5️⃣ Work Experience
st.subheader("💼 Work Experience")

col1, col2 = st.columns(2)
with col1:
    st.write("**Internship (Diploma)** — Asia Tech Biz Sdn Bhd (6 months)")
    st.markdown("""
    - Assisted in IT-related tasks  
    - Gained exposure to real-world business systems
    """)

with col2:
    st.write("**Crew (F&B)** — Food & Beverage Operations (2 years)")
    st.markdown("""
    - Provided customer service  
    - Handled orders, ensured customer satisfaction, maintained quality
    """)

st.write("**Stokis Business – Chocojar (1 year)**")
st.markdown("""
- Managed stock distribution and customer engagement  
- Enhanced sales through effective marketing strategies
""")

st.write("---")

# 6️⃣ Skills
st.subheader("⚡ Skills")

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

st.write("---")

# 7️⃣ Projects
st.subheader("🚀 Projects")
st.markdown("""
**Security Smart Home Automation (Diploma Project)**  
- Controlled lights & fans automatically  
- Integrated alarm system with phone notifications  

**Automated Vending Machine for Prescription Medication (Degree Group Project)**  
- IoT-based vending system using ESP32-CAM & QR code  
- Dispensed medicine to reduce patient waiting times  

**TRIPJR Travel App (Degree Group Assignment)**  
- Flutter-based travel app  
- Enabled hotel & homestay search + booking
""")

st.write("---")
st.markdown("<p style='text-align: center; color: gray;'>© 2025 Fatin Nurasiyah Abdul Rahim</p>", unsafe_allow_html=True)
st.markdown("---")
st.subheader("🧭 Test and Refine")

st.markdown("""
- ✅ **Ensure all information is accurate and well-organized.**  
- 🎨 **Check that the page is visually appealing and easy to navigate.**  
- 💡 Optionally, add styling with `st.markdown` or CSS for a polished look.  
- ⚙️ **Explore Streamlit’s documentation** for extra features like:
  - Buttons (`st.button`)
  - Sliders (`st.slider`)
  - Media display (`st.audio`, `st.video`)
  - Layout customization (`st.columns`, `st.container`)
- 🧼 **Keep your design clean and professional.**
""")

