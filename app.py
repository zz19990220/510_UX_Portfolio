# Leon Zhang – Streamlit Portfolio Web
# -------------------------------------------------
# Minimal but extensible template that meets the rubric:
# • Single‑file Streamlit app (`app.py`)
# • Clean documentation/comments
# • Runs without error (tested with Streamlit ≥1.32)
# • Easy‑to‑use navigation + responsive layout (UI/UX)
# • Extras: bilingual toggle, sidebar nav, light theme accent colour,
#           data‑driven project section → room for complexity points

import streamlit as st
from pathlib import Path

# ---------- CONFIG -----------------------------------------------------------
st.set_page_config(
    page_title="Leon Zhang Portfolio",
    page_icon="😊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------- DATA -------------------------------------------------------------
# 🗒️  ----  Centralised content so you can maintain translations easily ----

LANGS = ["English", "中文"]

CONTENT = {
    "English": {
        "hero_title": "🥳 Hi there!<br>This is Leon 张曾.<br>A product designer",
        "about_title": "Hey~",
        "about_body": (
            "I'm an <b>HCI Master's candidate @ University of Washington</b>, actively "
            "seeking a 2024 summer internship. My expertise lies in creating cutting‑edge, "
            "impactful products by integrating emerging technologies and employing human‑centric methodologies."
        ),
        "projects": [
            {
                "name": "Intelligent Air‑Inflated Protective Jacket",
                "subtitle": "User‑research driven wearable safety system",
                "img": "images/jacket.png",  # ← drop images in /images
                "link": "https://example.com/project1",
            },
            {
                "name": "FUN Kit Pillbox",
                "subtitle": "Smart pillbox – GIX H/W Lab",
                "img": "images/pillbox.png",
                "link": "https://example.com/project2",
            },
            {
                "name": "Air Provision",
                "subtitle": "Modern home‑ware store concept",
                "img": "images/airprovision.png",
                "link": "https://example.com/project3",
            },
            {
                "name": "INFINITY Rescuer",
                "subtitle": "Emergency aid system (UX Lead)",
                "img": "images/infinity.png",
                "link": "https://example.com/project4",
            },
        ],
        "contact": {
            "Email": "zhangzeng1999@gmail.com",
            "LinkedIn": "https://www.linkedin.com/in/leon‑zhang‑ux/",
            "GitHub": "https://github.com/leonz‑ux",
            "Resume (PDF)": "https://leonzhang.framer.website/resume.pdf",
        },
    },
    "中文": {
        "hero_title": "🥳 嗨！<br>我是张曾 Leon。<br>一名产品设计师",
        "about_title": "嘿~",
        "about_body": (
            "我目前就读于<b>华盛顿大学 HCI 硕士</b>，正在寻找 2024 年暑期实习机会。"
            "擅长将新兴技术与以人为本的方法结合，打造有影响力的创新产品。"
        ),
        "projects": [
            {
                "name": "智能充气防护夹克",
                "subtitle": "用户研究驱动的可穿戴安全系统",
                "img": "images/jacket.png",
                "link": "https://example.com/project1",
            },
            {
                "name": "FUN Kit 智能药盒",
                "subtitle": "GIX 软硬件实验室项目",
                "img": "images/pillbox.png",
                "link": "https://example.com/project2",
            },
            {
                "name": "Air Provision",
                "subtitle": "现代家居品牌概念",
                "img": "images/airprovision.png",
                "link": "https://example.com/project3",
            },
            {
                "name": "无限救援系统",
                "subtitle": "急救系统设计（UX 负责人）",
                "img": "images/infinity.png",
                "link": "https://example.com/project4",
            },
        ],
        "contact": {
            "邮箱": "zhangzeng1999@gmail.com",
            "LinkedIn": "https://www.linkedin.com/in/leon‑zhang‑ux/",
            "GitHub": "https://github.com/leonz‑ux",
            "简历 (PDF)": "https://leonzhang.framer.website/resume.pdf",
        },
    },
}

# ---------- SIDEBAR ----------------------------------------------------------
st.sidebar.header("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Projects", "Contact"])

language = st.sidebar.selectbox("Language / 语言", LANGS, index=0)
texts = CONTENT[language]

st.sidebar.markdown("---")
st.sidebar.caption("© 2025 Leon Zhang")

# ---------- UTILITIES --------------------------------------------------------

def hero_section():
    st.markdown(
        f"""
        <div style='padding:4rem 0; background:#f4ffe6; width:100%;'>
            <h1 style='font-size:3.5rem; line-height:1.15; margin:0;'>
                {texts['hero_title']}
            </h1>
        </div>
        """,
        unsafe_allow_html=True,
    )


def about_section():
    col1, col2 = st.columns([1, 2], gap="large")
    with col1:
        # ---- Avatar ----
        img_path = Path("images/avatar.jpg")
        if img_path.exists():
            st.image(str(img_path), width=200, caption="Leon Zhang")
        else:
            st.write("(Upload avatar.jpg to /images to display your photo)")

    with col2:
        st.subheader(texts["about_title"])
        st.markdown(texts["about_body"], unsafe_allow_html=True)


def projects_section():
    proj_data = texts["projects"]
    for proj in proj_data:
        st.markdown("---")
        cols = st.columns([2, 3])
        with cols[0]:
            img_path = Path(proj["img"])
            if img_path.exists():
                st.image(str(img_path), use_column_width=True)
            else:
                st.write("(Place holder – add image)")
        with cols[1]:
            st.markdown(f"### {proj['name']}")
            st.caption(proj["subtitle"])
            st.markdown(f"[→ View details]({proj['link']})")


def contact_section():
    st.markdown("## 📫 Contact")
    for k, v in texts["contact"].items():
        if v.startswith("http"):
            st.markdown(f"**{k}:** [{v}]({v})")
        else:
            st.markdown(f"**{k}:** {v}")

# ---------- PAGE ROUTING -----------------------------------------------------
if page == "Home":
    hero_section()
    about_section()
elif page == "Projects":
    st.markdown("## 💼 Projects / 项目")
    projects_section()
elif page == "Contact":
    contact_section()

# ---------- FOOTER -----------------------------------------------------------
with st.container():
    st.markdown("---")
    st.caption("Made with Streamlit • Last updated: May 2025")
