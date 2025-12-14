import numpy as np
import pandas as pd

def simulate_semesters(df_students, n_semesters=8, seed=42):
    rng = np.random.default_rng(seed)

    n = len(df_students)
    
    # base dropout probability per student (vectorized)
    p_base = (
        0.05
        + 0.04 * (df_students["ses_index"] < -1)
        + 0.03 * (df_students["internet_access"] == 0)
        + 0.03 * (df_students["modality"] == "En Línea")
    ).to_numpy()

    alive = np.ones(n, dtype=bool)
    records = []
    baseline = np.array([0.18, 0.10, 0.06, 0.04, 0.03, 0.025, 0.02, 0.02])
    for sem in range(1, n_semesters + 1):
        # only sample for students still enrolled
        u = rng.random(n)
        p = p_base * baseline[sem - 1]
        dropped = (u < p) & alive

        records.append(pd.DataFrame({
            "student_id": df_students["student_id"],
            "semester": sem,
            "dropped": dropped,
            "p_dropout": p_base,
            "colonia_id": df_students["colonia_id"]
        }))

        # update survival
        alive &= ~dropped

    panel = pd.concat(records, ignore_index=True)

    # remove semesters after dropout
    panel = panel[panel.groupby("student_id")["dropped"].cumsum() <= 1]

    return panel
