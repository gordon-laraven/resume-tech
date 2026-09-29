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
PAGE_ICON = "🧠"

# Personal Details
NAME = "La Raven Gordon"
DESCRIPTION = """
Enterprise AI Brain Specialist | LLM Training & Evaluation · Foundation-First AI Implementation | Founder, LCGIS
"""
EMAIL = "laraven.gordon@gmail.com"

# Social Media Links
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/laraven-gordon/",
    "Substack": "https://aibrainclone.substack.com/",
    "GitHub": "https://github.com/gordon-laraven",
    "Twitter (X)": "https://x.com/LaRaven_Gordon",
    "Threads": "https://www.threads.com/@laraven_charde",
}

# Projects
PROJECTS = {
    '⚡️ Relocation Insights Application: Conversational AI with LangChain and Google Gen AI': 'https://github.com/dmmonjur/Final-project.git', 
    '🧬 AI Model Training & Evaluation: 28+ Confidential Enterprise Projects (RLHF, Rubric Design, Fact-Checking, Red-Teaming)': None, 
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
    "I train and evaluate frontier AI models from the inside (RLHF, preference ranking, adversarial red-teaming, rubric design, fact-checking), "
    "and I use that experience to help small and mid-sized businesses adopt AI the right way.\n\n"
    "My framework, **Three Brains**, starts with human judgment (First Brain), builds documented systems and SOPs (Second Brain), "
    "and only then adds AI tools and automation (Third Brain). Most AI rollouts fail because they skip straight to the third. "
    "My background spans sales leadership, scientific research, and enterprise AI training, and I write about the work at "
    "[AI Brain Clone](https://aibrainclone.substack.com/)."
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
- 🤖 **Claude 101** and **AI Fluency: Framework & Foundations**, Anthropic
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
- ✔️ 28+ enterprise AI training and evaluation projects for frontier AI labs (details confidential under NDA)
- ✔️ Built and delivered onboarding frameworks for large teams (300 new hires trained in 3 days)
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
- 💼 Sales & Team Leadership (50+ team members)
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

st.write("🧠", "**Enterprise AI Brain Specialist | Self-Employed**")
st.write("Dec 2023 - Present")
st.write(
    """
- ► Train and evaluate frontier LLMs across 28+ confidential enterprise projects: RLHF pipelines, preference ranking, adversarial red-teaming, refusal/logic auditing, and rubric design
- ► Apply the Three Brains framework to build systems that reflect trained human judgment rather than generic outputs
- ► Advise on compliance and ethics: copyright, data privacy, and regulatory exposure in AI-generated content
"""
)

st.write('\n')
st.write("🧩", "**SMB & Individual AI Implementation Specialist | LCGIS (LC Gordon Intelligent Systems)**")
st.write("Jun 2021 - Present")
st.write(
    """
- ► Guide clients through a foundation-first method: readiness and fit assessment, discovery, and frictionless integration
- ► Help small businesses and individuals move beyond copy-paste prompts toward trained, personalized judgment
- ► Drive adoption across analytics, customer service, and internal automation
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

st.write('\n')
st.write("📈", "**Vector Marketing**")
st.write("Field Sales Manager (Oct 2020 - Present) · Event Sales Specialist (Apr 2021 - Present) · Branch Manager (Apr 2022 - Oct 2022) · Assistant Manager (Jan 2021 - May 2022)")
st.write(
    """
- ► Led and coached 50+ representatives; hired, trained, and developed sales teams
- ► Built an onboarding framework that trained 300 new hires in 3 days
- ► President's Club inductee
"""
)

# --- SELECTED PROJECTS ---
st.write('\n')
st.subheader("Selected Projects")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})" if link else project)

# --- MEDIA & RECOGNITION ---
st.write('\n')
st.subheader("📣 Media & Recognition")
st.write("---")

# 🎙️ Interviews & Podcasts
st.markdown("### ✍️ Writing")
st.markdown("- **AI Brain Clone** (Substack): [aibrainclone.substack.com](https://aibrainclone.substack.com/)")

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
