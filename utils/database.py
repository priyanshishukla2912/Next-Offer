import sqlite3


# ----------------------------
# Create Database
# ----------------------------
def create_database():
    conn = sqlite3.connect("data/placementgpt.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            college TEXT,
            branch TEXT,
            cgpa REAL,
            skills TEXT,
            projects INTEGER,
            internships INTEGER,
            target_role TEXT,
            certifications INTEGER,
            communication INTEGER,
            resume_score INTEGER,
            readiness_score INTEGER
        )
    """)

    conn.commit()
    conn.close()


# ----------------------------
# Save Student
# ----------------------------
def save_student(
    name,
    college,
    branch,
    cgpa,
    skills,
    projects,
    internships,
    target_role,
    certifications,
    communication,
    resume_score=None,
    readiness_score=None
):

    conn = sqlite3.connect("data/placementgpt.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO students(
            name,
            college,
            branch,
            cgpa,
            skills,
            projects,
            internships,
            target_role,
            certifications,
            communication,
            resume_score,
            readiness_score
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        name,
        college,
        branch,
        cgpa,
        skills,
        projects,
        internships,
        target_role,
        certifications,
        communication,
        resume_score,
        readiness_score
    ))

    conn.commit()
    conn.close()


# ----------------------------
# Get All Students
# ----------------------------
def get_all_students():

    conn = sqlite3.connect("data/placementgpt.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    conn.close()

    return students


# ----------------------------
# Dashboard Statistics
# ----------------------------
def get_dashboard_stats():

    conn = sqlite3.connect("data/placementgpt.db")
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM students")
    total_students = cursor.fetchone()[0]

    cursor.execute("SELECT AVG(readiness_score) FROM students")
    avg_readiness = cursor.fetchone()[0]

    cursor.execute("SELECT AVG(resume_score) FROM students")
    avg_resume = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(DISTINCT target_role) FROM students")
    total_roles = cursor.fetchone()[0]

    conn.close()

    # Handle NULL values safely
    avg_readiness = avg_readiness if avg_readiness is not None else 0
    avg_resume = avg_resume if avg_resume is not None else 0
    total_roles = total_roles if total_roles is not None else 0

    return (
        total_students,
        round(avg_readiness, 1),
        round(avg_resume, 1),
        total_roles
    )


# ----------------------------
# Target Roles
# ----------------------------
def get_target_roles():

    conn = sqlite3.connect("data/placementgpt.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT DISTINCT target_role
        FROM students
        WHERE target_role IS NOT NULL
        ORDER BY target_role
    """)

    roles = [row[0] for row in cursor.fetchall()]

    conn.close()

    # If database is empty, show default roles
    if not roles:
        roles = [
            "AI Engineer",
            "Machine Learning Engineer",
            "Data Scientist",
            "Data Analyst",
            "Software Engineer",
            "Backend Developer",
            "Frontend Developer",
            "Full Stack Developer",
            "Cloud Engineer",
            "DevOps Engineer",
            "Cyber Security Engineer",
            "Business Analyst"
        ]

    return roles