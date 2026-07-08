def calculate_readiness_score(
    cgpa,
    skills,
    projects,
    internships,
    certifications,
    communication
):
    score = 0
    weak_areas = []

    # CGPA (25)
    cgpa_score = min((cgpa / 10) * 25, 25)
    score += cgpa_score
    if cgpa < 7:
        weak_areas.append("CGPA")

    # Skills (30)
    skill_list = [s.strip() for s in skills.split(",") if s.strip()]
    skill_score = min(len(skill_list) * 5, 30)
    score += skill_score
    if len(skill_list) < 4:
        weak_areas.append("Skills")

    # Projects (15)
    project_score = min(projects * 5, 15)
    score += project_score
    if projects < 2:
        weak_areas.append("Projects")

    # Internships (10)
    internship_score = min(internships * 5, 10)
    score += internship_score
    if internships == 0:
        weak_areas.append("Experience")

    # Certifications (10)
    cert_score = min(certifications * 2.5, 10)
    score += cert_score
    if certifications == 0:
        weak_areas.append("Certifications")

    # Communication (10)
    comm_score = communication
    score += comm_score
    if communication < 6:
        weak_areas.append("Communication")

    score = round(score)

    if score >= 85:
        level = "Excellent"
    elif score >= 70:
        level = "Good"
    elif score >= 50:
        level = "Average"
    else:
        level = "Needs Improvement"

    return score, level, weak_areas