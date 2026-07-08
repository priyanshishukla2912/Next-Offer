import streamlit as st


def predictor_page():
    st.title("📈 Placement Predictor")

    # Fetch student profile
    student = st.session_state.get("student_profile", None)

    if student is None:
        st.warning("⚠ Please fill Student Profile first.")
        return

    # Auto-loaded values
    cgpa = student["cgpa"]
    projects = student["projects"]
    internships = student["internships"]
    communication_score = student["communication"]

    # Convert communication score into category
    if communication_score <= 4:
        communication = "Poor"
    elif communication_score <= 7:
        communication = "Average"
    else:
        communication = "Good"

    # Show loaded profile
    st.info(f"""
Profile Loaded ✅

CGPA: {cgpa}
Projects: {projects}
Internships: {internships}
Communication: {communication}
""")

    # Only ask DSA level
    dsa_level = st.selectbox(
        "DSA Level",
        ["Beginner", "Intermediate", "Advanced"]
    )

    if st.button("Predict Placement Chance"):

        score = 0

        # CGPA (30 marks)
        score += (cgpa / 10) * 30

        # Projects (20 marks)
        score += min(projects * 5, 20)

        # Internships (20 marks)
        score += min(internships * 10, 20)

        # DSA (20 marks)
        if dsa_level == "Beginner":
            score += 5
        elif dsa_level == "Intermediate":
            score += 12
        else:
            score += 20

        # Communication (10 marks)
        if communication == "Poor":
            score += 2
        elif communication == "Average":
            score += 6
        else:
            score += 10

        probability = round(score, 2)

        st.subheader(f"🎯 Placement Probability: {probability}%")
        st.progress(probability / 100)

        if probability >= 80:
            st.success("High Placement Chance 🚀")
        elif probability >= 60:
            st.warning("Medium Placement Chance ⚡")
        else:
            st.error("Low Placement Chance 📉")

        st.subheader("📌 Recommendations")

        if cgpa < 7.5:
            st.write("• Improve CGPA above 7.5")

        if projects < 3:
            st.write("• Build more real-world projects")

        if internships == 0:
            st.write("• Try getting at least one internship")

        if dsa_level == "Beginner":
            st.write("• Practice more DSA problems")

        if communication == "Poor":
            st.write("• Improve communication and interview confidence")

