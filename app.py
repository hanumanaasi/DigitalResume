from pathlib import Path

import requests
import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets10.lottiefiles.com/private_files/lf30_wqypnpu5.json")

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "HanumanResumeLatest.pdf"
profile_pic = current_dir / "assets" / "picofme.png"
skills_pic = current_dir / "assets" / "skills2.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital RESUME | Hanuman Kumar Aasi"
PAGE_ICON = ":wave:"
NAME = "Hanuman Kumar Aasi"
DESCRIPTION = """
A Full Stack Java Developer from Hyderabad"""
EMAIL = "hanumankumar.aasi@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/hanuman-kumar-aasi-8a02031b4/",
    "GitHub": "https://github.com/hanumanaasi",
    "Twitter": "https://twitter.com/aasihanuman",
}
PROJECTS = {
    "🏆 A Hotel Website - Which shows the complete picture of a five star hotel" : "Status: 🏗️",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)
skills_pic = Image.open(skills_pic)

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


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 2 Years of expereince in IT Industry deleaing with the Enterprise Applications.
- ✔️ Strong hands on experience and knowledge in Java, Angular, Typescript, HTML and CSS.
- ✔️ Good understanding of Business architectural modules.
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.image(skills_pic, width=300)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "***********Software Engineer | Concentrix Catalyst***********")
st.write("May, 2022 - Present")
st.write(
    """

- ► As a Java developer currently workig under Enterprise Application of RailRoad service dealing with the transformation of legacy systems.
- ► Built API services on top of the cache level mechanism.
- ► Developed the dashboards by creating the event handlers for the data comparison between legacy systems and new systems.
- ► Developed solutions for various new business scenarios as part of the new feature development.
- ► Involved in continuous integration and continuous deployment software development practice.
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "***********Associate Software Engineer | Mphasis Limited***********")
st.write("March, 2021 - May, 2022")
st.write(
    """
- ► As a full stack java developer contributed for the logistics application towards the development new features meets with the customer 
    requirements and business goals.
- ► Built different modules, pipes, services and reusable components as a part of frontend development. 
- ► Responsible for the creation of efficient design and development of user interaction screens using HTML, CSS, Bootstrap, Angular 6.
- ► Participated in design & code review processes.
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")

st.write("---")
st.subheader("Get in touch with me!")
contact_form = """
    
    <form action="https://formsubmit.co/hanumankumar.aasi@gmail.com" method="POST">
    <input type="hidden"name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
</form>

    """
    
st.markdown(contact_form, unsafe_allow_html=True)

st.write("\n")

st.write("---")

st.write("© Hanuman Kumar Aasi, All rights reserved.🤓")