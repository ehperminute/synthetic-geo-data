"""
simulate_dropout.py
-------------------

Simulates semester-by-semester student inscriptions and dropout risk.
Produces a long-format panel dataset similar to institutional academic records.

"""

import numpy as np
import pandas as pd


def simulate_semesters(df_students, n_semesters=8, seed=42):
    """Creates panel data of semester enrollment + dropout using logistic risk."""
    np.random.seed(seed)

    records = []
    for _, row in df_students.iterrows():
        dropped = False
        
        for sem in range(1, n_semesters + 1):
            if dropped:
                break

            # Base dropout probability influenced by features
            p_dropout = (
                0.05
                + 0.04 * (row["ses_index"] < -1)  # lower SES → higher risk
                + 0.03 * (row["internet_access"] == 0)
                + 0.02 * (row["transport_time"] > 60)
                + 0.03 * (row["modality"] == "En Línea")
                + 0.05 * ([10, 7, 4, 3, 2, 2, 2, 2][row["semester"]])
            )

            dropped_flag = np.random.rand() < p_dropout

            records.append({
                "student_id": row["student_id"],
                "semester": sem,
                "dropped": int(dropped_flag),
                "p_dropout": p_dropout,
            })

            if dropped_flag:
                dropped = True

    return pd.DataFrame(records)
