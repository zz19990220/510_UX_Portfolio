# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃  Leon Zhang – Streamlit Portfolio Web                  ┃
# ┃  Single-file app │ 双语切换 │ 侧边栏导航 │ 图像优雅降级  ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

import streamlit as st
from pathlib import Path

# ─── CONFIG ──────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Leon Zhang Portfolio",
    page_icon="😊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── CUSTOM CSS ──────────────────────────────────────────────────────────────
st.markdown(
    """
    <style>
      /* 把侧边栏背景改为浅灰 */
      [data-testid="stSidebar"] { background-color: #f7f8fa; }
      /* 给主区内容添加一点内边距 */
      .css-18e3th9 { padding-top:1rem; padding-left:2rem; padding-right:2rem; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ─── DATA ────────────────────────────────────────────────────────────────────
LANGS = ["English", "中文"]

CONTENT = {
    "English": {
        "hero_title": "🥳 Hi there!<br>This is Leon 张曾.<br>A product designer",
        "about_title": "Hey~",
        "about_body": (
            "I'm an <b>HCI Master's candidate @ University of Washington</b>, "
            "actively seeking a 2024 summer internship. My expertise lies in creating "
            "cutting-edge, impactful products by integrating emerging technologies "
            "and employing human-centric methodologies."
        ),
        "projects": [
            {
                "name": "Intelligent Air-Inflated Jacket",
                "subtitle": "Wearable safety system (user-research driven)",
                "img": "images/jacket.png",
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
                "subtitle": "Modern home-ware store concept",
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
            "LinkedIn": "https://www.linkedin.com/in/leon-zhang-ux/",
            "GitHub": "https://github.com/leonz-ux",
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
            "LinkedIn": "https://www.linkedin.com/in/leon-zhang-ux/",
            "GitHub": "https://github.com/leonz-ux",
            "简历 (PDF)": "https://leonzhang.framer.website/resume.pdf",
        },
    },
}

# ─── SIDEBAR ──────────────────────────────────────────────────────────────────
st.sidebar.title("🔖 Navigation")
# 带 Emoji 的单选按钮
page = st.sidebar.radio(
    "Go to",
    ["🏠 Home", "💼 Projects", "📫 Contact"],
    index=0,
)

language = st.sidebar.selectbox("Language / 语言", LANGS, index=0)
texts = CONTENT[language]

st.sidebar.markdown("---")
st.sidebar.caption("© 2025 Leon Zhang")

# ─── SECTIONS ────────────────────────────────────────────────────────────────
def hero_section():
    st.markdown(
        f"""
        <div style='padding:3rem; background:#f4ffe6;'>
          <h1 style='font-size:3.5rem; margin:0;'>{texts['hero_title']}</h1>
        </div>
        """,
        unsafe_allow_html=True,
    )

def about_section():
    c1, c2 = st.columns([1, 2], gap="large")
    with c1:
        p = Path("images/avatar.jpg")
        if p.exists():
            st.image(str(p), width=180, caption="Leon Zhang")
        else:
            st.write("⚠️ Upload avatar.jpg to /images to show your photo.")
    with c2:
        st.subheader(texts["about_title"])
        st.markdown(texts["about_body"], unsafe_allow_html=True)

def projects_section():
    st.markdown("## Projects / 项目")
    for proj in texts["projects"]:
        st.markdown("---")
        col_img, col_txt = st.columns([2, 3])
        with col_img:
            p = Path(proj["img"])
            if p.exists():
                st.image(str(p), use_container_width=True)
            else:
                st.write("⚠️ Place your image in /images")
        with col_txt:
            st.markdown(f"### {proj['name']}")
            st.caption(proj["subtitle"])
            st.markdown(f"[→ View details]({proj['link']})")

def contact_section():
    st.markdown("## 📫 Contact / 联系方式")
    for k, v in texts["contact"].items():
        if v.startswith("http"):
            st.markdown(f"**{k}:** [{v}]({v})")
        else:
            st.markdown(f"**{k}:** {v}")

# ─── ROUTING ─────────────────────────────────────────────────────────────────
if page.startswith("🏠"):
    hero_section(); about_section()
elif page.startswith("💼"):
    projects_section()
else:
    contact_section()

# ─── FOOTER ──────────────────────────────────────────────────────────────────
st.markdown("---")
st.caption("Made with Streamlit • Last updated: May 2025")