import streamlit as st
from utils.database import save_student, get_target_roles
from utils.readiness import calculate_readiness_score


def profile_page():

    st.title("👤 Student Profile")

    # -----------------------------
    # Initialize Session State
    # -----------------------------
    defaults = {
        "name": "",
        "college": "",
        "branch": "IT",
        "cgpa": 7.0,
        "skills": "",
        "projects": 0,
        "internships": 0,
        "certifications": 0,
        "communication": 5,
        "target_role": "AI Engineer"
    }

    # First visit
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

    # If profile already saved, preload values
    if "student_profile" in st.session_state:
        for key, value in st.session_state["student_profile"].items():
            if key in defaults:
                st.session_state[key] = value

    # -----------------------------
    # Basic Details
    # -----------------------------

    st.text_input(
        "Full Name",
        key="name"
    )

    st.text_input(
        "College Name",
        key="college"
    )

    st.selectbox(
        "Branch",
        ["IT", "CSE", "ECE", "EE", "ME", "Civil"],
        key="branch"
    )

    st.slider(
        "CGPA",
        0.0,
        10.0,
        key="cgpa"
    )

    st.text_area(
        "Technical Skills",
        placeholder="Python, SQL, Machine Learning, React...",
        key="skills"
    )

    st.number_input(
        "Number of Projects",
        min_value=0,
        max_value=20,
        step=1,
        key="projects"
    )

    st.number_input(
        "Number of Internships",
        min_value=0,
        max_value=10,
        step=1,
        key="internships"
    )

    st.number_input(
        "Number of Certifications",
        min_value=0,
        step=1,
        key="certifications"
    )

    st.slider(
        "Communication Skill",
        min_value=1,
        max_value=10,
        key="communication"
    )

    roles = get_target_roles()

    # Ensure target role exists
    if st.session_state.target_role not in roles:
        st.session_state.target_role = roles[0]

    st.selectbox(
        "Preferred Role",
        roles,
        key="target_role"
    )

    # -----------------------------
    # Save Button
    # -----------------------------

    if st.button("💾 Save Profile"):

        score, level, weak_areas = calculate_readiness_score(
            st.session_state.cgpa,
            st.session_state.skills,
            st.session_state.projects,
            st.session_state.internships,
            st.session_state.certifications,
            st.session_state.communication
        )

        save_student(
            name=st.session_state.name,
            college=st.session_state.college,
            branch=st.session_state.branch,
            cgpa=st.session_state.cgpa,
            skills=st.session_state.skills,
            projects=st.session_state.projects,
            internships=st.session_state.internships,
            certifications=st.session_state.certifications,
            communication=st.session_state.communication,
            target_role=st.session_state.target_role,
            resume_score=None,
            readiness_score=score
        )

        st.session_state["student_profile"] = {
            "name": st.session_state.name,
            "college": st.session_state.college,
            "branch": st.session_state.branch,
            "cgpa": st.session_state.cgpa,
            "skills": st.session_state.skills,
            "projects": st.session_state.projects,
            "internships": st.session_state.internships,
            "certifications": st.session_state.certifications,
            "communication": st.session_state.communication,
            "target_role": st.session_state.target_role,
            "readiness_score": score
        }

        st.success("✅ Profile Saved Successfully!")

        st.subheader("🎯 Placement Readiness")

        st.progress(score / 100)

        st.metric(
            "Readiness Score",
            f"{score}%"
        )

        st.info(f"Placement Level: **{level}**")

        if weak_areas:

            st.warning("Areas to Improve")

            for area in weak_areas:
                st.write(f"• {area}")