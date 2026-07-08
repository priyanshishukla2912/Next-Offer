import streamlit as st
import PyPDF2
from utils.database import get_target_roles


def resume_analyzer_page():
    st.title("📄 Resume Analyzer")

    # Skill Mapping
    role_skills = {
        "Data Scientist": [
            "python", "sql", "machine learning",
            "statistics", "pandas", "power bi"
        ],

        "ML Engineer": [
            "python", "machine learning",
            "deep learning", "tensorflow", "docker"
        ],

        "Data Analyst": [
            "sql", "excel", "power bi",
            "tableau", "python"
        ],

        "Software Engineer": [
            "dsa", "oops", "dbms",
            "system design", "git"
        ]
    }

    # Dynamic roles from database
    roles = get_target_roles()

    target_role = st.selectbox(
        "Select Target Role",
        roles
    )

    uploaded_file = st.file_uploader(
        "Upload Resume (PDF)",
        type=["pdf"]
    )

    if uploaded_file is not None:

        st.success("Resume uploaded successfully!")

        pdf_reader = PyPDF2.PdfReader(uploaded_file)

        resume_text = ""

        for page in pdf_reader.pages:
            text = page.extract_text()

            if text:
                resume_text += text

        with st.expander("View Extracted Resume Text"):
            st.text_area(
                "Resume Content",
                resume_text,
                height=300
            )

        skill_keywords = [
            "python",
            "sql",
            "machine learning",
            "deep learning",
            "power bi",
            "excel",
            "git",
            "c++",
            "java",
            "javascript",
            "react",
            "node",
            "docker",
            "kubernetes",
            "aws",
            "tensorflow",
            "pandas",
            "numpy",
            "tableau",
            "statistics",
            "dsa",
            "dbms",
            "oops",
            "system design"
        ]

        resume_lower = resume_text.lower()

        detected_skills = []

        for skill in skill_keywords:
            if skill in resume_lower:
                detected_skills.append(skill)

        st.subheader("Detected Skills")

        if detected_skills:
            for skill in detected_skills:
                st.badge(skill)
        else:
            st.warning("No known skills detected.")

        # ---------------- Role Skill Matching ----------------

        if target_role in role_skills:

            required_skills = role_skills[target_role]

            matched_skills = []
            missing_skills = []

            for skill in required_skills:
                if skill in detected_skills:
                    matched_skills.append(skill)
                else:
                    missing_skills.append(skill)

            skill_match_score = (
                len(matched_skills) /
                len(required_skills)
            ) * 100

            st.subheader("🎯 Skill Match Score")

            st.progress(skill_match_score / 100)

            st.write(f"{round(skill_match_score,2)}%")

            if missing_skills:

                st.subheader("Missing Skills")

                for skill in missing_skills:
                    st.error(skill)

            else:
                st.success("🎉 Great! You have all required skills.")

        else:

            st.info(
                "Skill mapping for this role will be added in the next update."
            )

        # ---------------- ATS Score ----------------

        score = 0

        score += len(detected_skills) * 5

        if "project" in resume_lower:
            score += 15

        if "education" in resume_lower:
            score += 15

        if "internship" in resume_lower:
            score += 15

        if "skills" in resume_lower:
            score += 15

        score = min(score, 100)

        st.write("")

        st.subheader(f"📊 ATS Score : {score}/100")

        st.progress(score / 100)

        if score >= 80:
            st.success("🚀 Excellent Resume")

        elif score >= 60:
            st.warning("⚡ Good Resume, but can be improved")

        else:
            st.error("❌ Resume needs major improvements")