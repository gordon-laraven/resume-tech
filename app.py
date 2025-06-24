from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "laraven.jpg"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "La Raven Gordon's Digital CV"
PAGE_ICON = ":👑:"

# Personal Details
NAME = "La Raven Gordon"
DESCRIPTION = """
AI/ML SOLUTIONS SPECIALIST & SCIENTIFIC DOMAIN EXPERT
"""
EMAIL = "laraven.gordon@gmail.com"

# Social Media Links
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/laraven-gordon/",
    "GitHub": "https://github.com/gordon-laraven",
    "Twitter (X)": "https://x.com/LaRaven_Gordon",
    "Threads": "https://www.threads.com/@laraven_charde",
}
PROJECTS = {
    '⚡️ Relocation Insights Application: Conversational AI with LangChain and Google Gen AI': 'https://github.com/dmmonjur/Final-project.git', 
    '🧬 AI Model Training & Optimization for Biochemistry and Chemistry Domains': 'https://app.outlier.ai/expert/referrals/link/Lxp3HlJRUJDg4naJ4g15Cg2l-_g', 
    '🏊‍♀️ Olympic Swimming Analysis: Historical Data Processing and Forecasting': 'https://github.com/kkuria1/Olympic-swimming-analysis.git', 
    '💳 Banking Interface System: Secure Transaction System with Conversational Flows': 'https://github.com/gordon-laraven/customer_banking.git', 
    '🥗 Indigenous Vegetables Research: Nutritional Analysis and Educational Materials': 'https://storytelling.marine.rutgers.edu/amaranth/', 
    '🏥 Obesity Classification System: ML Model for Health Factor Analysis': 'https://github.com/gordon-laraven/diabetes_project_2.git' 
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)

# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- EDUCATION & QUALIFICATIONS ---
st.write('\n')
st.subheader("Education & Qualifications")
st.write(
    """
### Education

- 🎓 **AI & Machine Learning Certificate**, Columbia Engineering (2024)
- 🎓 **Bachelor of Science - Biochemistry**, Rutgers University (2022)

### Certifications

- 🎓 **AI and Machine Learning Bootcamp**, Columbia Engineering (Issued Dec 2024)
  - Skills: Python, Prompt Engineering, Pandas, Project Planning, Prompt Design, Machine Learning, Machine Learning Pipeline
- 📚 **Intermediate Tutor**, Tutor.com (Issued Apr 2023)
  - Skills: Training, Chemistry, Biochemistry, English, Academic Support Services, Calculations, Communication, Logical Thinking
- 🌱 **Worker Training Greenhouse**, Rutgers University–New Brunswick (Issued Dec 2023 - Expired Dec 2024)
  - Skills: Leadership, Seeding, Greenhouse, Seed Production, Seed Storage
- 🔬 **Online Biosafety/Bloodborne Pathogens Refresher**, Rutgers University (Issued Sep 2023 - Expired Sep 2024)
  - Skills: Leadership, Plant Biology, Laboratory Safety, Bloodborne Pathogens, Bloodborne Pathogens Training
- 🔬 **Online Laboratory Safety Refresher**, Rutgers University (Issued Sep 2023 - Expired Sep 2024)
  - Skills: Leadership, Plant Biology, Laboratory Safety
- 🌱 **Online Plant and Plant-Related Research**, Rutgers University (Issued Sep 2023 - Expired Sep 2024)
  - Skills: Leadership, Research, Plant Biology, Plant Science, Research and Critical Analysis

### Key Qualifications

- ✔️ Proven expertise in developing and training machine learning models across multiple domains, including Biology, Chemistry, and Creative Writing 🤖
- ✔️ Strong experience in designing AI systems, reducing response errors by 40%, and achieving 95% user satisfaction with LLMs for scientific applications 📊
- ✔️ Skilled in building pipelines processing 10,000+ data points with 98% accuracy, and developing ML pipelines and scientific tools 💻
- ✔️ Excellent project management, instructional design, and data-driven decision-making skills, with experience in academic support and performance analysis 📈
"""
)

# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 🤖 AI/ML: LangChain, TensorFlow, PyTorch, Hugging Face, OpenAI API, Transformers, Generative AI
- 👩‍💻 Programming: Python, SQL, REST APIs, Git, Jupyter
- 📊 Data Analysis: Data Visualization, MS Excel, Pandas, NumPy, Prophet
- 🗄️ Databases: Postgres, MongoDB
- 📚 Scientific: Biochemistry, Chemistry, Plant Biology, Research, Lab Protocols, Scientific Validation
- 📈 Financial: Financial APIs
- 💬 NLP: Major language models (ChatGPT, Gemini, Deep AI)
"""
)

st.write('\n')
st.subheader("Soft Skills")
st.write(
    """
- 💼 Leadership: Led AI integration and automation projects, Led 50+ representatives
- 📈 Project Management: Developed and implemented AI customer service, Developed analytics and virtual training systems
- 💬 Communication: Developed and streamlined technical academic content, Provided academic support and performance analysis
- 🤔 Problem-Solving: Designed AI systems reducing response errors by 40%, Built pipelines processing 10,000+ data points with 98% accuracy
- 💡 Critical Thinking: Applied AI/ML expertise to scientific domain knowledge, Bridged complex scientific concepts with practical business applications
- 👥 Teamwork: Collaborated on projects, including AI model training and optimization
- 🔄 Adaptability: Adapted to new technologies and applications, including LangChain and Google Gen AI
- ⏰ Time Management: Managed multiple projects and tasks, including AI model training and optimization
"""
)

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write('\n')
st.write("🚧", "**AI Solutions Specialist & Data Auditor | Freelance**")
st.write("Dec 2023 - Present")
st.write(
    """
- ► Helped businesses harness the power of AI to drive growth and innovation
- ► Provided expert training, developed machine learning models, and created customized AI solutions
- ► Designed AI systems reducing response errors by 40%
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Small Business AI Implementation Specialist | Freelance**")
st.write("Dec 2023 - Present")
st.write(
    """
- ► Helped small businesses integrate AI tools to streamline operations, improve customer experiences, and support growth
- ► Assessed business needs, recommended tailored AI solutions, and guided smooth implementation and adoption
- ► Led AI integration and automation projects
"""
)

# --- JOB 3
st.write('\n')
st.write("🔬", "**Laboratory Assistant | Rutgers University–New Brunswick**")
st.write("Sep 2023 - Feb 2024")
st.write(
    """
- ► Executed sample preparation for nutritional and mineral analysis
- ► Analyzed and interpreted data for science storytelling
- ► Performed greenhouse and laboratory safety for a clean and productive work environment
"""
)

# --- JOB 4
st.write('\n')
st.write("📚", "**Tutor | The Princeton Review**")
st.write("Nov 2022 - Nov 2023")
st.write(
    """
- ► Coached students of various academic levels to become better students
- ► Analyzed and assessed students' problem areas
- ► Consulted students and parents with areas of weakness and strength
"""
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")