from pathlib import Path
import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic_file = current_dir / "assets" / "laraven.jpg"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "La Raven Gordon's Digital CV"
PAGE_ICON = ":֎🇦🇮:"

# Personal Details
NAME = "La Raven Gordon"
DESCRIPTION = """
Enterprise AI Brain Specialist | LLM Training & Evaluation | AI Brain Clone Methodology for SMBs | Foundation-First AI Adoption | Generative AI Strategist
"""
EMAIL = "laraven.gordon@gmail.com"

# Social Media Links
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/laraven-gordon/",
    "GitHub": "https://github.com/gordon-laraven",
    "Twitter (X)": "https://x.com/LaRaven_Gordon",
    "Threads": "https://www.threads.com/@laraven_charde",
}

# Projects
PROJECTS = {
    '⚡️ Relocation Insights Application: Conversational AI with LangChain and Google Gen AI': 'https://github.com/dmmonjur/Final-project.git', 
    '🧬 AI Model Training & Optimization for Biochemistry and Chemistry Domains': 'https://app.outlier.ai/expert/referrals/link/Lxp3HlJRUJDg4naJ4g15Cg2l-_g', 
    '🏊‍♀️ Olympic Swimming Analysis: Historical Data Processing and Forecasting': 'https://github.com/kkuria1/Olympic-swimming-analysis.git', 
    '💳 Banking Interface System: Secure Transaction System with Conversational Flows': 'https://github.com/gordon-laraven/customer_banking.git', 
    '🥗 Indigenous Vegetables Research: Nutritional Analysis and Educational Materials': 'https://storytelling.marine.rutgers.edu/amaranth/', 
    '🏥 Obesity Classification System: ML Model for Health Factor Analysis': 'https://github.com/gordon-laraven/diabetes_project_2.git' 
}

# --- STREAMLIT PAGE CONFIG ---
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFILE PIC ---
if css_file.exists():
    with open(css_file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

PDFbyte = None
if resume_file.exists():
    with open(resume_file, "rb") as pdf_file:
        PDFbyte = pdf_file.read()

profile_pic = Image.open(profile_pic_file)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    if PDFbyte:
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

# --- CORE EXPERTISE ---
st.write('\n')
st.subheader("Core Expertise")
st.write(
    'I\'ve built business powerhouses, and now I help small and mid-sized businesses translate strategy into AI and machine learning systems that drive growth, efficiency, and scale.\n\n'
    'With a background spanning executive leadership, entrepreneurship, and scientific research, I design enterprise-level AI architectures typically reserved for large organizations and make them accessible to growing businesses. My work emphasizes systems thinking, evidence-based decision-making, and measurable ROI. See the Projects section for applied examples.'
)

# --- EDUCATION & CREDENTIALS ---
st.write('\n')
st.subheader("Education & Credentials")
st.write(
    """
- 🎓 **AI & Machine Learning Certificate**, Columbia Engineering (2024)
- 🎓 **Bachelor of Science - Biochemistry**, Rutgers University (2022)
"""
)

# --- CERTIFICATIONS ---
st.write('\n')
st.subheader("Certifications")
st.write(
    """
- 🎓 **AI and Machine Learning Bootcamp**, Columbia Engineering (Issued Dec 2024)
- 📚 **Intermediate Tutor**, Tutor.com (Issued Apr 2023)
- 🌱 **Worker Training Greenhouse**, Rutgers University–New Brunswick
- 🔬 **Laboratory & Biosafety Training**, Rutgers University
"""
)

# --- KEY QUALIFICATIONS & IMPACT ---
st.write('\n')
st.subheader("Key Qualifications & Impact")
st.write(
    """
- ✔️ Enterprise-level AI system design focused on business outcomes and scalability
- ✔️ Reduced AI response errors by 40% and achieved 95% user satisfaction
- ✔️ Built ML pipelines processing 10,000+ data points with 98% accuracy
- ✔️ Strong executive communication and cross-functional leadership
"""
)

# --- TECHNICAL SKILLS ---
st.write('\n')
st.subheader("Technical Skills")
st.write(
    """
- 🤖 AI/ML: LangChain, TensorFlow, PyTorch, Hugging Face, OpenAI API, Transformers, Generative AI
- 👩‍💻 Programming: Python, SQL, Latex, REST APIs, Git, Jupyter
- 📊 Analytics: Pandas, NumPy, Prophet, Data Visualization
- 🗄️ Databases: Postgres, MongoDB
- 📚 Scientific: Research Design, Validation, Biochemistry, Chemistry
"""
)

# --- LEADERSHIP & PROFESSIONAL SKILLS ---
st.write('\n')
st.subheader("Leadership & Professional Skills")
st.write(
    """
- 💼 Executive & Team Leadership (50+ team members)
- 🧠 Systems Thinking & Problem Decomposition
- 📈 Business Process Optimization
- 🤝 Cross-Functional Collaboration
- 🗣️ Technical Storytelling & Stakeholder Alignment
"""
)

# --- PROFESSIONAL EXPERIENCE ---
st.write('\n')
st.subheader("Professional Experience")
st.write("---")

st.write("🚧", "**Enterprise AI Brain Specialist**")
st.write("Dec 2023 - Present")
st.write(
    """
- ► Architect and evaluate AI models using LLM training expertise — RLHF pipelines, preference ranking, adversarial red-teaming, refusal/logic auditing, and rubric design — on frontier models.
- ► Apply the Three Brains framework (natural judgment, organized knowledge, AI brain clone) to build systems that reflect trained human judgment rather than generic outputs.
- ► Advise on compliance and ethics considerations (copyright, data privacy, regulatory exposure) in AI-generated content.
"""
)

st.write('\n')
st.write("🔬", "**Laboratory Assistant | Rutgers University–New Brunswick**")
st.write("Sep 2023 - Feb 2024")
st.write(
    """
- ► Conducted nutritional and mineral analysis using validated protocols
- ► Translated scientific data into clear insights and narratives
"""
)

st.write('\n')
st.write("📚", "**Tutor | The Princeton Review**")
st.write("Nov 2022 - Nov 2023")
st.write(
    """
- ► Diagnosed learning gaps and built structured improvement systems
- ► Strengthened analytical reasoning and problem-solving skills
"""
)

# --- SELECTED PROJECTS ---
st.write('\n')
st.subheader("Selected Projects")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")

# --- MEDIA & RECOGNITION ---
st.write('\n')
st.subheader("📣 Media & Recognition")
st.write("---")

# 🎙️ Interviews & Podcasts
st.markdown("### 🎙️ Interviews & Podcasts")
st.markdown("""
- **Quiet Impact Podcast**: *Quiet Achiever Spotlight – Empowering Small Businesses Through AI with LaRaven Gordon*  
  ▶️ [Watch on YouTube](https://www.youtube.com/watch?v=wcPwu0SjGBE)
""")

# 📰 Professional Features
st.markdown("### 📰 Professional Features")
st.markdown("""
- **NJ Legacy Work** – [Meet Our Team](https://njlegacywork.com/our-team/)
- **Vector NJ** – [Welcome Feature](https://njvector.com/welcome/)
""")

# 🎓 Academic & Research Recognition
st.markdown("### 🎓 Academic & Research Recognition")
st.markdown("""
I’m proud to have my academic work featured across a range of platforms, combining science, storytelling, and public education:

- **Academia.edu** – *Nutrition & Child Development Research*  
  📄 Title: *Limiting Child Exposure: The Organic Diet*  
  [Read Paper](https://www.academia.edu/36084562/Limiting_Child_Exposure_The_Organic_Diet_docx)

- **Amaranth – Digital Storytelling Feature (Rutgers University)**  
  🎬 A multimedia project exploring culture, environment, and narrative  
  [View Story](https://storytelling.marine.rutgers.edu/amaranth/)
""")
