import streamlit as st
from app_pages.profile import profile_page
from utils.database import create_database , get_all_students  ,get_dashboard_stats
from app_pages.eligibility import eligibility_page
import os
from app_pages.predictor import predictor_page
from app_pages.resume_analyzer import resume_analyzer_page
from app_pages.chatbot import chatbot_page
import pandas as pd
import plotly.express as px
from app_pages.roadmap import roadmap_page
from utils.footer import footer

print("RUNNING FROM:", os.getcwd())

create_database()
# ---------------- APP CONFIG ----------------
st.set_page_config(
    page_title="Next Offer",
    page_icon="🚀",
    layout="wide"
)

st.markdown("""
<style>
            header {
    background: transparent !important;
}

[data-testid="stHeader"] {
    background: rgba(0,0,0,0) !important;
}

[data-testid="stToolbar"] {
    right: 1rem;
}


/* ===== Main App ===== */
.stApp {
    background: linear-gradient(135deg, #020617, #0f172a, #111827);
    color: white;
}

/* ===== Sidebar ===== */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #111827, #1e1b4b);
    border-right: 1px solid rgba(255,255,255,0.08);
}
        

section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] span {
    color: white !important;
}

/* ===== Headings ===== */
h1, h2, h3 {
    color: #f8fafc !important;
}

/* ===== Text ===== */
p, label {
    color: #cbd5e1;
}

/* ===== Buttons ===== */
.stButton > button {
    background: linear-gradient(90deg, #2563eb, #7c3aed);
    color: white !important;
    border: none;
    border-radius: 14px;
    padding: 12px 24px;
    font-weight: 600;
    box-shadow: 0 0 20px rgba(99,102,241,0.35);
}

/* ===== Metric Cards ===== */
div[data-testid="metric-container"] {
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.12);
    backdrop-filter: blur(12px);
    border-radius: 18px;
    padding: 20px;
}

/* ===== Inputs ===== */
/* ===== Inputs ===== */
.stTextInput input,
.stTextArea textarea,
[data-baseweb="input"] input,
[data-baseweb="textarea"] textarea {
    background-color: white !important;
    color: black !important;
    border-radius: 12px !important;
    caret-color: black !important;
    -webkit-text-fill-color: black !important;
}

::placeholder {
    color: #94a3b8 !important;
    opacity: 1 !important;
}     


/* ===== Progress Bar ===== */
.stProgress > div > div {
    background: linear-gradient(90deg, #06b6d4, #6366f1);
}
            .hero-box {
    background: linear-gradient(135deg, rgba(37,99,235,0.25), rgba(124,58,237,0.25));
    border: 1px solid rgba(255,255,255,0.15);
    padding: 35px;
    border-radius: 24px;
    backdrop-filter: blur(16px);
    box-shadow: 0 0 30px rgba(99,102,241,0.2);
    margin-bottom: 25px;
}

.hero-title {
    font-size: 42px;
    font-weight: 700;
    color: white;
}

.hero-subtitle {
    font-size: 20px;
    color: #cbd5e1;
    margin-top: 12px;
}
            

.kpi-card {
    background: linear-gradient(135deg, rgba(37,99,235,0.18), rgba(124,58,237,0.18));
    border: 1px solid rgba(255,255,255,0.12);
    border-radius: 20px;
    padding: 25px;
    text-align: center;
    box-shadow: 0 0 20px rgba(99,102,241,0.15);
}

.kpi-title {
    color: #cbd5e1;
    font-size: 16px;
}

.kpi-value {
    color: white;
    font-size: 36px;
    font-weight: bold;
    margin-top: 10px;
}
            
input[type="text"] {
    color: black !important;
    background: white !important;
    -webkit-text-fill-color: black !important;
}
            
textarea {
    color: black !important;
    -webkit-text-fill-color: black !important;
}
            

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
st.sidebar.title("🚀 Next Offer")
st.sidebar.caption("Placement Intelligence Platform")

menu = [
    "Dashboard",
    "Student Profile",
    "Placement Recommendations",
    "Placement Predictor",
    "Resume Analyzer",
     "AI Career Roadmap",
    "AI Chatbot"
]

selected_page = st.sidebar.radio("Navigation", menu)

# ---------------- DASHBOARD ----------------
if selected_page == "Dashboard":
    st.markdown("""
<div class="hero-box">
    <div class="hero-title">🚀 Next Offer </div>
    <div class="hero-subtitle">
        AI-powered platform to predict placements, analyze resumes,
        detect skill gaps, and accelerate career growth.
    </div>
</div>
""", unsafe_allow_html=True)

    st.markdown("---")

    students = get_all_students()

    total_students, avg_readiness, avg_resume, total_roles = get_dashboard_stats()

    df = pd.read_csv("data/student_dataset.csv")
    placement_counts = df["placement_status"].value_counts()

    col1, col2, col3, col4 = st.columns(4)

    with col1:
       st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">👨‍🎓  Registered Students</div>
        <div class="kpi-value">{total_students}</div>
    </div>
    """, unsafe_allow_html=True)

    with col2:
      st.markdown(f"""
    <div class="kpi-card">
    <div class="kpi-title">📈Avg Readiness Score</div>
    <div class="kpi-value">{avg_readiness}%</div>
   </div>
    """, unsafe_allow_html=True)

    with col3:
      st.markdown(f"""
     <div class="kpi-card">
    <div class="kpi-title">📄Avg ATS Score</div>
    <div class="kpi-value">{avg_resume}</div>
     </div>
     """, unsafe_allow_html=True)
      
    with col4:
      st.markdown(f"""
       <div class="kpi-card">
    <div class="kpi-title">🎯 Supported Roles</div>
    <div class="kpi-value">{total_roles}</div>
     </div>
      """, unsafe_allow_html=True)


    st.markdown("---")
    st.subheader("📊 Placement Analytics")

    col1, col2 = st.columns(2)

# Placement Distribution
    placement_counts = df["placement_status"].value_counts()

    fig1 = px.pie(
    values=placement_counts.values,
    names=placement_counts.index,
    hole=0.65,
    title="Placement Distribution",
    color_discrete_sequence=px.colors.sequential.Blues_r
)

    fig1.update_layout(
    template="plotly_dark",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font_color="white"
)

# Branch Distribution
    branch_counts = df["branch"].value_counts()

    fig2 = px.bar(
    x=branch_counts.index,
    y=branch_counts.values,
    title="Students by Branch",
    color=branch_counts.values,
    color_continuous_scale="Blues"
)

    fig2.update_layout(
    template="plotly_dark",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font_color="white",
    coloraxis_showscale=False
)

    with col1:
       st.plotly_chart(fig1, use_container_width=True)

    with col2:
       st.plotly_chart(fig2, use_container_width=True)

    st.markdown("""
<div style="
background:rgba(255,255,255,0.05);
padding:25px;
border-radius:20px;
border:1px solid rgba(255,255,255,0.12);
margin-top:20px;
">

<h3 style="color:white;">🤖 AI Platform Highlights</h3>

<p style="font-size:17px;line-height:2;color:#CBD5E1;">

✔ AI-powered Placement Prediction<br>
✔ Resume ATS Analysis<br>
✔ Company Eligibility Checker<br>
✔ Personalized Career Roadmaps<br>
✔ Interactive AI Career Assistant (Groq)<br>
✔ Live Student Analytics Dashboard

</p>

</div>
""", unsafe_allow_html=True)



elif selected_page == "Student Profile":
    profile_page()

elif selected_page == "Placement Recommendations":
    eligibility_page()

elif selected_page == "Placement Predictor":
    predictor_page()

elif selected_page == "Resume Analyzer":
    resume_analyzer_page()

elif selected_page == "AI Career Roadmap":
    roadmap_page()

elif selected_page == "AI Chatbot":
    chatbot_page()

footer()