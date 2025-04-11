import streamlit as st
#from PIL import Image

# --- PAGE CONFIG ---
st.set_page_config(page_title="Mannisha Das | Portfolio", layout="centered")

# --- PROFILE IMAGE & NAME ---
#profile_pic = "profile.jpg"  # Replace with your image file name
#image = Image.open(profile_pic)

#st.image(image, width=150)
st.title("Manisha Das")
st.subheader("Aspiring Business Analyst | MBA in Business Analytics & Data Science")

# --- SOCIAL LINKS ---
st.markdown("**Connect with me:**")
st.markdown("""
[LinkedIn](https://www.linkedin.com/in/your-link) | 
[GitHub](https://github.com/your-github) | 
[Email](mailto:your.email@example.com) | 
[Portfolio](https://your-portfolio-link.com)
""")

# --- SUMMARY ---
st.header("🔍 Summary")
st.write("""
Motivated MBA trainee with a passion for data storytelling, analytics, and impactful business decisions. 
Strong background in data visualization, communication, and project management, with hands-on experience in tools like Tableau, Power BI, and Excel.
""")

# --- EDUCATION ---
st.header("🎓 Education")
st.write("""
**MBA in Business Analytics & Data Science**  
Your University Name | 2024 – Present

**B.Sc. in Data Science**  
Techno India University | Year of Passing  
""")

# --- EXPERIENCE ---
st.header("💼 Experience")
st.write("""
**Product Analyst (Intern)**  
Company Name | Jan 2024 – Apr 2024  
- Analyzed customer trends and developed dashboards for business insights.  
- Contributed to project planning and decision-making using data-backed insights.

**Data Analytics Virtual Intern**  
Deloitte (Australia) | 2024  
- Created a Tableau dashboard to solve real business problems.  
""")

# --- SKILLS ---
st.header("🛠 Skills")
st.write("""
- **Data Tools:** Excel, Tableau, Power BI, IBM Cognos Analytics  
- **Programming:** Python, SQL  
- **Soft Skills:** Communication, Fast Learner, Project Management  
""")

# --- PROJECTS ---
st.header("📊 Projects")
st.write("""
**Sales Dashboard using Power BI**  
- Analyzed sales data, created YoY growth charts, and customer segmentation analysis.

**Career Guidance Chatbot**  
- Used IBM Watson Assistant to build an AI chatbot for psychometric testing.

**Zomato Campaign Pop-up Analysis**  
- Designed a marketing strategy for Independence Day targeted at West Bengal region.
""")

# --- CERTIFICATIONS & ACHIEVEMENTS ---
st.header("📜 Certifications & Achievements")
st.write("""
- **IBM Business Intelligence** (30 hours)  
- **Scaler Data Visualization Masterclass**  
- **IIT Kanpur – Machine Learning with Python**  
- **Forage Virtual Experience – Tata & Deloitte**  
""")

# --- HOBBIES ---
st.header("🎨 Hobbies")
st.write("""
- Exploring AI innovations  
- Designing memes for educational content  
- Emceeing and public speaking  
- Writing short blogs on LinkedIn  
""")

# --- FOOTER ---
st.markdown("---")
st.caption("Made with ❤️ using Streamlit")
