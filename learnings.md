# Day 1

## app.py
app.py is the entry point of the software.

Responsibilities:
1. Configure application
2. Handle navigation
3. Route user to correct page

Without app.py, all pages remain disconnected.


## Layered Architecture

My project follows layered architecture:

UI Layer → Page Layer → Logic Layer → Data Layer

Benefits:
- modular code
- easier debugging
- easier scaling
- reusable components


## Single Source of Truth (SSOT)

SSOT means storing important data in one place and reusing it everywhere.

Benefits:
- avoids duplication
- prevents inconsistency
- improves user experience

## Types of Bugs

Not all bugs come from wrong syntax.

Common bug categories:
1. Syntax bugs
2. Logic bugs
3. Architecture bugs
4. Framework integration bugs

Example:
Using folder name "pages" triggered Streamlit auto-routing.

## Separation of Concerns

A software component should have one clear responsibility.

Example:
profile.py -> handles UI
utils -> handles logic/storage

Benefits:
- easier debugging
- reusable code
- cleaner architecture

There are many databases:

DB	Type
SQLite	Embedded DB
MySQL	Server DB
PostgreSQL	Enterprise DB
MongoDB	NoSQL

We choose SQLite because:

✅ Zero installation
✅ Comes with Python
✅ Uses single .db file
✅ Great for small–medium apps



## Cursor

Cursor acts as bridge between Python and database.

Python sends SQL commands using cursor.


## Data Access Layer (DAL)

DAL is a software layer responsible for interacting with the database.

Responsibilities:
- insert data
- fetch data
- update data
- delete data

Benefits:
- keeps database logic separate from UI
- improves maintainability

## Idempotent Operation

An operation is idempotent if running it multiple times gives the same safe result.

Example:
CREATE TABLE IF NOT EXISTS

## CRUD Operations

Database systems mainly perform 4 operations:

C = Create
R = Read
U = Update
D = Delete

Example:
Saving a new student profile is a CREATE operation.


## Parameterized Queries

Using ? placeholders prevents SQL injection.

Example:
INSERT INTO table VALUES (?, ?)

Safer than string formatting SQL queries.

## SQL SELECT

SELECT retrieves data from database.

Example:
SELECT * FROM students

This fetches all rows and columns.

## Streamlit Hot Reload

Streamlit automatically reruns app when files change.

But sometimes (especially in Windows/OneDrive), changes in imported files
like profile.py or database.py may not reload properly.

Fix:
1. Save all files
2. Refresh browser
3. Restart Streamlit
4. If still stale, modify app.py or stop/restart server

## Routing

Routing decides which page/component to render
based on user navigation.

In PlacementGPT:
app.py acts as router.

Nested if statements allow multi-stage decision making.

Example:
Button clicked -> Company selected -> Eligibility check

Scalable code means code that can handle growth
without major rewriting.

Dictionary + loops help reduce repetition.



# Day 3 Learnings

* Built Placement Predictor page using Streamlit.

* Learned scoring-based prediction model instead of direct ML.

* Prediction factors:

  * CGPA (30)
  * Projects (20)
  * Internships (20)
  * DSA (20)
  * Communication (10)

* Learned **feature engineering**:
  Selecting useful inputs/features for prediction.

* Revised **Python indentation & variable scope**:
  Variables inside blocks may not work outside.

* Learned Streamlit issue:
  Multiple running terminals can cause old code/cache problems.

* database.py functions:

  * create_database()
  * save_student()
  * get_all_students()

* Project architecture:

  * app.py → router
  * app_pages → UI pages
  * utils → backend logic

- Learned file uploading using st.file_uploader()
- Learned PDF parsing using PyPDF2
- PDFs can be converted into text for AI analysis


# PlacementGPT Notes

## Preprocessing
- Drop irrelevant columns → student_id, salary_package_lpa
- Encode categorical features using One-Hot Encoding
- Convert target labels → Placed:1, Not Placed:0

## ML Pipeline
Dataset → Preprocessing → Train-Test Split → Model Training → Evaluation → Deployment

## Train-Test Split
- 80% train
- 20% test
Purpose: evaluate model on unseen data

## Random Forest
- Ensemble of Decision Trees
- Good for tabular data
- Handles nonlinear patterns
- Less overfitting

## Features & Target
X → input features  
y → placement_status

### DB Schema Upgrade
Extended student database with certifications and communication fields to support hybrid AI placement scoring.