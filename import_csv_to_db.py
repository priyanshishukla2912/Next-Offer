import sqlite3
import pandas as pd

# Read the CSV
df = pd.read_csv("data/student_dataset.csv")

# Connect to database
conn = sqlite3.connect("data/placementgpt.db")
cursor = conn.cursor()

# Optional: Remove existing records
cursor.execute("DELETE FROM students")

# Insert all rows
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
        float(row["cgpa"]),
        row["skills"],
        int(row["projects"]),
        int(row["internships"]),
        row["target_role"],
        int(row["certifications"]),
        int(row["communication"]),
        int(row["resume_score"]),
        int(row["readiness_score"])
    ))

conn.commit()
conn.close()

print("✅ Successfully imported", len(df), "students into SQLite.")