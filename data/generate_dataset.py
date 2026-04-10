"""
Synthetic Biomarker Dataset Generator
Generates a synthetic dataset inspired by the ATN biomarker framework
for Alzheimer's Disease classification research.

This dataset is SYNTHETIC and does NOT contain real patient data.
It is designed for educational assessment purposes only.

The distributions are loosely modeled after publicly reported ranges
in literature for CSF and blood-based AD biomarkers.
"""

import numpy as np
import pandas as pd

np.random.seed(42)

N_NC = 250
N_MCI = 150
N_AD = 85
N_TOTAL = N_NC + N_MCI + N_AD

def generate_biomarkers(n, diagnosis):
    """Generate synthetic biomarker values for a given diagnosis group."""
    
    if diagnosis == "NC":
        # Normal Cognition: high Aβ42, low tau, low NfL, low GFAP
        csf_ab42 = np.random.normal(680, 120, n)
        csf_tau = np.random.normal(180, 55, n)
        csf_ptau = np.random.normal(15, 5, n)
        plasma_ptau217 = np.random.normal(1.2, 0.5, n)
        plasma_ab42 = np.random.normal(18, 3.5, n)
        plasma_ab40 = np.random.normal(145, 25, n)
        plasma_nfl = np.random.normal(16, 6, n)
        plasma_gfap = np.random.normal(90, 30, n)
        age = np.random.normal(72, 7, n)
        
    elif diagnosis == "MCI":
        # MCI: intermediate values, HIGH VARIANCE (heterogeneous group)
        csf_ab42 = np.random.normal(520, 160, n)
        csf_tau = np.random.normal(260, 90, n)
        csf_ptau = np.random.normal(28, 12, n)
        plasma_ptau217 = np.random.normal(2.1, 0.9, n)
        plasma_ab42 = np.random.normal(15.5, 4, n)
        plasma_ab40 = np.random.normal(150, 30, n)
        plasma_nfl = np.random.normal(24, 10, n)
        plasma_gfap = np.random.normal(140, 50, n)
        age = np.random.normal(74, 6.5, n)
        
    elif diagnosis == "AD":
        # AD: low Aβ42, high tau, high NfL, high GFAP
        csf_ab42 = np.random.normal(350, 90, n)
        csf_tau = np.random.normal(400, 100, n)
        csf_ptau = np.random.normal(48, 15, n)
        plasma_ptau217 = np.random.normal(3.8, 1.2, n)
        plasma_ab42 = np.random.normal(12, 3, n)
        plasma_ab40 = np.random.normal(155, 28, n)
        plasma_nfl = np.random.normal(35, 12, n)
        plasma_gfap = np.random.normal(210, 60, n)
        age = np.random.normal(77, 6, n)
    
    # Generate sex (0=Female, 1=Male)
    sex = np.random.binomial(1, 0.48, n)
    
    # Education years
    education = np.clip(np.random.normal(16, 3, n), 8, 24).astype(int)
    
    df = pd.DataFrame({
        "CSF_AB42": csf_ab42,
        "CSF_TAU": csf_tau,
        "CSF_PTAU": csf_ptau,
        "PLASMA_PTAU217": plasma_ptau217,
        "PLASMA_AB42": plasma_ab42,
        "PLASMA_AB40": plasma_ab40,
        "PLASMA_NFL": plasma_nfl,
        "PLASMA_GFAP": plasma_gfap,
        "AGE": age,
        "SEX": sex,
        "EDUCATION_YEARS": education,
        "DIAGNOSIS": diagnosis
    })
    
    return df

# Generate data for each class
df_nc = generate_biomarkers(N_NC, "NC")
df_mci = generate_biomarkers(N_MCI, "MCI")
df_ad = generate_biomarkers(N_AD, "AD")

# Combine
df = pd.concat([df_nc, df_mci, df_ad], ignore_index=True)

# Shuffle
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Add patient IDs
df.insert(0, "PATIENT_ID", [f"SYNTH_{str(i).zfill(4)}" for i in range(len(df))])

# Compute derived ratios
df["PLASMA_AB42_AB40_RATIO"] = df["PLASMA_AB42"] / df["PLASMA_AB40"]
df["PLASMA_PTAU217_AB42_RATIO"] = df["PLASMA_PTAU217"] / df["PLASMA_AB42"]

# Inject ~5% missing values in selected columns (realistic scenario)
missing_cols = ["CSF_AB42", "CSF_TAU", "CSF_PTAU", "PLASMA_NFL", "PLASMA_GFAP"]
for col in missing_cols:
    mask = np.random.random(len(df)) < 0.05
    df.loc[mask, col] = np.nan

# Clip negative values (biomarker concentrations can't be negative)
biomarker_cols = ["CSF_AB42", "CSF_TAU", "CSF_PTAU", "PLASMA_PTAU217",
                  "PLASMA_AB42", "PLASMA_AB40", "PLASMA_NFL", "PLASMA_GFAP"]
for col in biomarker_cols:
    df[col] = df[col].clip(lower=0.01)

# Round values
df["AGE"] = df["AGE"].round(1)
for col in biomarker_cols + ["PLASMA_AB42_AB40_RATIO", "PLASMA_PTAU217_AB42_RATIO"]:
    df[col] = df[col].round(4)

# Save
df.to_csv("biomarker_data.csv", index=False)

print(f"Dataset generated: {len(df)} samples")
print(f"Class distribution:")
print(df["DIAGNOSIS"].value_counts())
print(f"\nColumns: {list(df.columns)}")
print(f"\nMissing values:")
print(df.isnull().sum()[df.isnull().sum() > 0])
print(f"\nSaved to data/biomarker_data.csv")
