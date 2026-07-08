import pandas as pd
import sqlite3

df = pd.read_csv("demo_student_data.csv")

conn = sqlite3.connect("data/placementgpt.db")
cursor = conn.cursor()

for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO students (
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
        row["name"],
        row["college"],
        row["branch"],
        row["cgpa"],
        row["skills"],
        row["projects"],
        row["internships"],
        row["target_role"],
        row["certifications"],
        row["communication"],
        row["resume_score"],
        row["readiness_score"]
    ))

conn.commit()
conn.close()

print("Imported successfully!")
print("Rows:", len(df))