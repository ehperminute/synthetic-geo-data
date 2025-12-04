"""
generate_population.py
----------------------

Generates a synthetic student population with demographic, socioeconomic,
and geographic attributes. Designed to be portable and reproducible.

This module does NOT rely on real student data.
"""

import numpy as np
import pandas as pd
from faker import Faker

fake = Faker('es_MX')


def generate_students(n_students=1200, seed=42):
    """Generate synthetic students with demographic and SES attributes."""
    np.random.seed(seed)

    sexes = ['F', 'M']
    modalities = ['Escolarizado', 'Semiescolarizado', 'En Línea']

    data = {
        "student_id": np.arange(1, n_students + 1),
        "sex": np.random.choice(sexes, n_students),
        "age": np.random.normal(19, 1.8, n_students).round().astype(int),
        "ses_index": np.random.normal(0, 1, n_students),  # socioeconomic indicator
        "internet_access": np.random.choice([0, 1], n_students, p=[0.25, 0.75]),
        "transport_time": np.abs(np.random.normal(40, 12, n_students)).round().astype(int),
        "modality": np.random.choice(modalities, n_students, p=[0.7, 0.2, 0.1]),
    }

    df = pd.DataFrame(data)
    df["name"] = [fake.name() for _ in range(n_students)]

    return df


def assign_colonias(df_students, colonias_df):
    """
    Randomly assign each student to a colonia from the cleaned geography table.

    Expects colonias_df to contain:
    - 'colonia_id'
    - 'colonia_name'
    - and optionally 'alcaldia'
    """
    assigned = colonias_df.sample(len(df_students), replace=True).reset_index(drop=True)

    df_students["colonia_id"] = assigned["colonia_id"]
    df_students["colonia_name"] = assigned["colonia_name"]
    df_students["alcaldia"] = assigned.get("alcaldia", None)

    return df_students


if __name__ == "__main__":
    # quick manual test
    print(generate_students(5))
