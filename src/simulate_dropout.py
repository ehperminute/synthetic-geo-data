import numpy as np
import pandas as pd

def simulate_semesters(df_students, n_semesters=8, seed=42):
    np.random.seed(seed)

    records = []
    for _, row in df_students.iterrows():
        dropped = False

        for sem in range(1, n_semesters + 1):
            if dropped:
                break

            p_dropout = (
                0.05
                + 0.04 * (row["ses_index"] < -1)
                + 0.03 * (row["internet_access"] == 0)
                + 0.02 * (row["transport_time"] > 60)
                + 0.03 * (row["modality"] == "En Línea")
            )

            dropped_flag = np.random.rand() < p_dropout

            records.append({
                "student_id": row["student_id"],
                "semester": sem,
                "dropped": int(dropped_flag),
                "p_dropout": p_dropout,
                "colonia_id": row["colonia_id"]
            })

            if dropped_flag:
                dropped = True

    return pd.DataFrame(records)
