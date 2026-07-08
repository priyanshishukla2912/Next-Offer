import streamlit as st


def eligibility_page():
    st.title("📋 Eligibility Checker")

    student = st.session_state.get("student_profile", None)

    if student is None:
        st.warning("⚠ Please fill Student Profile first.")
        return


    company = st.selectbox(
        "Select Company",
        ["Flipkart", "Amazon", "Microsoft", "Data Science Role"]
    )
    
    cgpa = student["cgpa"]
    projects = student["projects"]
    skills = student["skills"].split(",")

    st.info(f"""
Profile Loaded ✅

CGPA: {cgpa}
Projects: {projects}
Skills: {student["skills"]}
""")



    company_rules = {
    "Flipkart": {
        "cgpa": 7.0,
        "projects": 2,
        "skills": ["dsa"]
    },

    "Amazon": {
        "cgpa": 7.5,
        "projects": 2,
        "skills": ["python", "dsa"]
    },

    "Microsoft": {
        "cgpa": 8.0,
        "projects": 3,
        "skills": ["dsa", "oop"]
    },

    "Data Science Role": {
        "cgpa": 7.0,
        "projects": 2,
        "skills": ["python", "sql", "ml"]
    }
}


    if st.button("Check Eligibility"):
      rules = company_rules[company]

      required_cgpa = rules["cgpa"]
      required_projects = rules["projects"]
      required_skills = rules["skills"]

      skills = [skill.strip() for skill in student["skills"].split(",")]
      skills_lower = [skill.lower() for skill in skills]

      skills_ok = True
      for skill in required_skills:
        if skill not in skills_lower:
          skills_ok = False




      if cgpa >= required_cgpa and projects >= required_projects and skills_ok:
        st.success(f"Eligible for {company} ✅")
        st.info(f"""
Required CGPA: {required_cgpa}
Required Projects: {required_projects}
Required Skills: {", ".join(required_skills)}
""")
      else:
        st.error(f"Not Eligible for {company} ❌")

