# Leon Zhang – Streamlit Portfolio Web

A single-file Streamlit web portfolio with bilingual support (English / 中文), sidebar navigation, responsive layout, and graceful image fallback.  
Created for the **INFO 510 – Portfolio Web** assignment (Spring 2025).

<p align="center">
  <img src="images/screenshot_home.png" width="700">
</p>

---

## ⭐ Features

| Feature                           | Details |
|-----------------------------------|---------|
| **Single-file app**               | All logic in `app.py` for easy grading |
| **Bilingual toggle**              | `English` / `中文` switch in sidebar |
| **Top navigation**                | Home / Projects / Contact |
| **Responsive hero banner**        | Full-width pale-green section |
| **Image graceful-degrade**        | Placeholder notice if `images/*` missing |
| **Streamlit ≥ 1.32 compatible**   | No deprecated APIs |

---

## 1 · Prerequisites

| Tool | Version |
|------|---------|
| Python | 3.9 – 3.12 |
| pip    | latest |
| Streamlit | installed automatically (see below) |

---

## 2 · Local Setup & Run

```bash
# 1. Clone
git clone https://github.com/zz19990220/510_UX_Portfolio.git
cd 510_UX_Portfolio

# 2. (Optional) create & activate venv
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# 3. Install deps (only Streamlit + Pillow)
pip install streamlit pillow

# 4. Run 🏃
streamlit run app.py