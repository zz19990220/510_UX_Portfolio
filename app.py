```python
import streamlit as st
from pathlib import Path
import datetime

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
      :root {
        --brand: #4B2E83;
        --brand-light: rgba(75,46,131,0.06);
      }
      /* 全局字体 & 行距 */
      body, p, li {
        font-family: 'Inter', 'Noto Sans SC', sans-serif !important;
        line-height: 1.6 !important;
      }
      h1, h2, h3 {
        font-weight: 700;
        color: #222;
        margin-bottom: 1rem;
      }
      /* Hero 区 */
      .hero {
        background: var(--brand-light);
        padding: 4rem 3rem;
        border-radius: 12px;
        max-width: 800px;
        margin: 0 auto 2rem auto;
      }
      .hero .emoji {
        font-size: 1.2em;
        vertical-align: middle;
      }
      /* Sidebar 宽度 & 配色 */
      [data-testid="stSidebar"] {
        background: #f5f5f7 !important;
        width: 200px !important;
      }
      /* 主区内边距 */
      .css-18e3th9 {
        padding-top: 1rem !important;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
      }
      /* Footer 居中 */
      .footer {
        text-align: center;
        margin-top: 2rem;
        color: #555;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

# ─── DATA ────────────────────────────────────────────────────────────────────
LANGS = ["English", "中文"]

CONTENT = {
    "English": {
        "hero_title": "<span class='emoji'>🥳</span> Hi there!<br>This is Leon 张曾.<br>A product designer",
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
        "hero_title": "<span class='emoji'>🥳</span> 嗨！<br>我是张曾 Leon。<br>一名产品设计师",
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
page = st.sidebar.radio("Go to", ["🏠 Home", "💼 Projects", "📫 Contact"], index=0)
language = st.sidebar.selectbox("Language / 语言", LANGS, index=0)
texts = CONTENT[language]
st.sidebar.markdown("---")
st.sidebar.caption("© 2025 Leon Zhang")

# ─── SECTIONS ────────────────────────────────────────────────────────────────
def hero_section():
    st.markdown(
        f"<div class='hero'><h1>{texts['hero_title']}</h1></div>",
        unsafe_allow_html=True,
    )

def about_section():
    c1, c2 = st.columns([1, 3], gap="large")
    with c1:
        p = Path("images/avatar.jpg")
        if p.exists():
            st.image(str(p), width=180, caption="Portrait of Leon Zhang", use_column_width=False)
        else:
            st.warning("⚠️ Upload `avatar.jpg` to `/images` to show your photo.")
    with c2:
        st.subheader(texts["about_title"])
        st.markdown(texts["about_body"], unsafe_allow_html=True)

def projects_section():
    st.markdown("## Projects / 项目", unsafe_allow_html=True)
    for proj in texts["projects"]:
        st.markdown("---")
        col_img, col_txt = st.columns([2, 3])
        with col_img:
            p = Path(proj["img"])
            if p.exists():
                st.image(str(p), use_container_width=True)
            else:
                st.error("⚠️ Place your image in `/images`")
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
    hero_section()
    about_section()
elif page.startswith("💼"):
    projects_section()
else:
    contact_section()

# ─── FOOTER ──────────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown(
    f"<div class='footer'>Made with Streamlit • Last updated: {datetime.date.today():%b %Y}</div>",
    unsafe_allow_html=True,
)
```