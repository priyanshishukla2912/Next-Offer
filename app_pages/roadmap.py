import streamlit as st


def generate_recommendations(cgpa, skills, projects, internships, target_role):
    recommendations = []
    weak_areas = []

    skills_lower = skills.lower()

    role_skills = {
        "Data Scientist": ["python", "sql", "machine learning", "statistics"],
        "ML Engineer": ["python", "machine learning", "deep learning"],
        "Data Analyst": ["sql", "excel", "power bi"],
        "Software Engineer": ["dsa", "oops", "dbms"]
    }

    required_skills = role_skills.get(target_role, [])

    missing_skills = []
    for skill in required_skills:
        if skill not in skills_lower:
            missing_skills.append(skill)

    if cgpa < 7:
        weak_areas.append("Low CGPA")
        recommendations.append(
            "Focus on improving academic performance or highlight stronger projects."
        )

    if projects < 2:
        weak_areas.append("Insufficient Projects")
        recommendations.append(
            "Build at least 2–3 strong real-world projects."
        )

    if internships < 1:
        weak_areas.append("No Internship Experience")
        recommendations.append(
            "Try securing at least one internship."
        )

    if missing_skills:
        weak_areas.append("Skill Gap")
        recommendations.append(
            f"Learn these missing skills: {', '.join(missing_skills)}"
        )

    return weak_areas, recommendations


def roadmap_page():
    st.title("🧠 AI Career Roadmap")
    st.write("Generate your personalized placement roadmap.")

    student = st.session_state.get("student_profile", None)

    if student is None:
        st.warning("⚠ Please fill Student Profile first.")
        return

    cgpa = student["cgpa"]
    skills = student["skills"]
    projects = student["projects"]
    internships = student["internships"]
    target_role = student["target_role"]

    st.info(f"""
Profile Loaded ✅

CGPA: {cgpa}
Projects: {projects}
Internships: {internships}
Target Role: {target_role}
Skills: {skills}
""")

    if st.button("Generate Roadmap"):
        weak_areas, recommendations = generate_recommendations(
            cgpa,
            skills,
            projects,
            internships,
            target_role
        )

        st.subheader("🎯 Weak Areas")

        if weak_areas:
            for area in weak_areas:
                st.warning(area)
        else:
            st.success("No major weak areas detected!")

        st.subheader("🚀 Personalized Roadmap")

        if recommendations:
            for rec in recommendations:
                st.write(f"✅ {rec}")
        else:
            st.success(
                "Excellent profile! Keep applying and practicing interviews."
            )

