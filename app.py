# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃  Leon Zhang – Streamlit Portfolio Web                  ┃
# ┃  单文件 · 双语切换 · 顶部导航 · 全宽 Hero 区域           ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

import streamlit as st
from pathlib import Path

# ─── CONFIG ──────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Leon Zhang Portfolio",
    page_icon="😊",
    layout="wide",
    initial_sidebar_state="collapsed",  # 折叠侧边栏
)

# ─── CUSTOM CSS ──────────────────────────────────────────────────────────────
st.markdown(
    """
    <style>
      /* 隐藏默认侧边栏 */
      [data-testid="stSidebar"] { display: none; }

      /* 主内容区内边距 */
      .css-18e3th9 { padding-top:1rem; padding-left:2rem; padding-right:2rem; }

      /* Hero 全宽样式 */
      .hero {
        width:100vw;
        position: relative;
        left: 50%;
        right: 50%;
        margin-left: -50vw;
        margin-right: -50vw;
        padding: 3rem;
        background: #f4ffe6;
      }

      /* 顶部导航 & 语言选择 */
      .top-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 1.5rem;
      }
      .top-bar .nav-tabs button {
        margin-right: 1rem;
        font-size: 1rem;
      }
      .top-bar .nav-tabs button:hover {
        background-color: #e0f0ff;
      }
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

# ─── TOP NAV & LANGUAGE ───────────────────────────────────────────────────────
# 横向选项卡做导航
st.markdown('<div class="top-bar">', unsafe_allow_html=True)
tabs = st.tabs(["🏠 Home", "💼 Projects", "📫 Contact"])
# 语言选择放在右侧
language = st.selectbox("Language / 语言", LANGS, index=0)
st.markdown('</div>', unsafe_allow_html=True)

texts = CONTENT[language]

# ─── SECTIONS ────────────────────────────────────────────────────────────────
def hero_section():
    st.markdown(
        f"""
        <div class="hero">
          <h1 style="font-size:3.5rem; line-height:1.2; margin:0;">
            {texts['hero_title']}
          </h1>
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
            st.write("⚠️ Upload `avatar.jpg` 到 `images/` 文件夹以显示头像")
    with c2:
        st.subheader(texts["about_title"])
        st.markdown(texts["about_body"], unsafe_allow_html=True)

def projects_section():
    st.markdown("## 💼 Projects / 项目")
    for proj in texts["projects"]:
        st.markdown("---")
        col1, col2 = st.columns([2, 3])
        with col1:
            img_p = Path(proj["img"])
            if img_p.exists():
                st.image(str(img_p), use_container_width=True)
            else:
                st.write("⚠️ 将项目图片放到 `images/` 文件夹里")
        with col2:
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

# ─── PAGE ROUTING ────────────────────────────────────────────────────────────
with tabs[0]:
    hero_section()
    about_section()
with tabs[1]:
    projects_section()
with tabs[2]:
    contact_section()

# ─── FOOTER ──────────────────────────────────────────────────────────────────
st.markdown("---")
st.caption("Made with Streamlit • Last updated: May 2025")