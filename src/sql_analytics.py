import sqlite3
import pandas as pd

def run_sql_analytics(students_df, panel_df, db_path="analytics.db"):
    conn = sqlite3.connect(db_path)

    # Write tables
    students_df.to_sql("students", conn, if_exists="replace", index=False)
    panel_df.to_sql("enrollments", conn, if_exists="replace", index=False)

    # 1) Dropout rate by modality
    q1 = """
    SELECT
        s.modality,
        AVG(e.dropped) AS dropout_rate
    FROM enrollments e
    JOIN students s USING(student_id)
    GROUP BY s.modality
    """
    dropout_by_modality = pd.read_sql(q1, conn)

    # 2) Dropout rate by semester
    q2 = """
    SELECT
        semester,
        AVG(dropped) AS dropout_rate
    FROM enrollments
    GROUP BY semester
    ORDER BY semester
    """
    dropout_by_semester = pd.read_sql(q2, conn)

    # 3) Top 10 colonias by dropout rate
    q3 = """
    SELECT
        colonia_id,
        AVG(dropped) AS dropout_rate
    FROM enrollments
    GROUP BY colonia_id
    ORDER BY dropout_rate DESC
    LIMIT 10
    """
    high_risk_colonias = pd.read_sql(q3, conn)

    conn.close()

    return {
        "dropout_by_modality": dropout_by_modality,
        "dropout_by_semester": dropout_by_semester,
        "high_risk_colonias": high_risk_colonias
    }
