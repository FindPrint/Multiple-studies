"""
seaice_ou_quadratic.py
----------------------

Simulation du déclin de la banquise arctique en septembre
à l'aide d'un processus d'Ornstein–Uhlenbeck (OU) avec drift quadratique.

Étapes :
1. Charger les données NSIDC (N_09_extent_v4.0.csv).
2. Normaliser par rapport à la climatologie 1981–2010.
3. Définir le drift quadratique μ(t) avec coefficients calibrés.
4. Simuler 20 trajectoires OU jusqu'en 2050.
5. Extraire les minima de septembre.
6. Calculer l'année médiane de franchissement du seuil φ* < 0.5.
7. Produire et sauvegarder une figure de synthèse.
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

# -----------------------------
# 1. Charger les données NSIDC
# -----------------------------
data = pd.read_csv("N_09_extent_v4.0.csv")
data.columns = data.columns.str.strip()

# Garder uniquement les colonnes utiles
data = data[["year", "mo", "extent", "area"]].copy()
data["date"] = pd.to_datetime(dict(year=data["year"], month=data["mo"], day=1))

# Normalisation par rapport à la climatologie 1981–2010
clim = data[(data["year"] >= 1981) & (data["year"] <= 2010)]["extent"].mean()
data["phi_star"] = data["extent"] / clim

# -----------------------------
# 2. Paramètres du modèle OU
# -----------------------------
a, b, c = 1.1945, -0.000955, -0.000000033  # coefficients quadratiques
gamma = 0.13   # vitesse de rappel
D = 0.00020    # intensité du bruit
n_sims = 20    # nombre de trajectoires

# Horizon temporel : 1979–2050
n_steps = (2050 - 1979) * 12
t = np.arange(n_steps)
dates = pd.date_range("1979-01-01", periods=n_steps, freq="MS")

# Drift quadratique μ(t)
mu_t = a + b * t + c * t**2

# -----------------------------
# 3. Simulations OU
# -----------------------------
simulations = []
for s in range(n_sims):
    phi = np.zeros(n_steps)
    phi[0] = 1.0
    for k in range(1, n_steps):
        phi[k] = phi[k-1] - gamma * (phi[k-1] - mu_t[k]) + np.sqrt(2*D) * np.random.randn()
    simulations.append(phi)

# -----------------------------
# 4. Extraire minima de septembre
# -----------------------------
threshold = 0.5
crossing_years = []
sim_sept = []

for sim in simulations:
    sim_df = pd.DataFrame({"date": dates, "phi": sim})
    sim_df["month"] = sim_df["date"].dt.month
    sim_df["year"] = sim_df["date"].dt.year
    sept = sim_df[sim_df["month"] == 9].groupby("year")["phi"].mean()
    sim_sept.append(sept)
    below = sept[sept < threshold]
    crossing_years.append(below.index[0] if not below.empty else None)

valid_years = [int(y) for y in crossing_years if y is not None]
median_year = int(np.median(valid_years)) if valid_years else None

print("Années de franchissement :", crossing_years)
print("Année médiane :", median_year)

# -----------------------------
# 5. Figure de synthèse
# -----------------------------
plt.figure(figsize=(14, 7))

# Observations historiques (points noirs, septembre uniquement)
sept_obs = data[data["mo"] == 9]
plt.scatter(sept_obs["date"], sept_obs["phi_star"], color="black", label="Observé (septembre)")

# Trajectoires simulées
for sept in sim_sept:
    plt.plot(sept.index, sept.values, alpha=0.4, color="steelblue")

# Seuils
plt.axhline(1.0, color="red", linestyle="--", label="Climatologie")
plt.axhline(0.5, color="orange", linestyle="--", label="Seuil critique 0.5")

plt.title("Banquise Arctique — Synthèse septembre (observations + simulations OU quadratique)")
plt.xlabel("Année")
plt.ylabel("φ*(t) en septembre")
plt.legend()
plt.grid(True)

# Inset : histogramme des années de franchissement
if valid_years:
    ax_inset = inset_axes(plt.gca(), width="35%", height="35%", loc="upper right")
    sns.histplot(valid_years, bins=range(min(valid_years), max(valid_years)+1),
                 ax=ax_inset, color="skyblue", edgecolor="black")
    ax_inset.axvline(median_year, color="red", linestyle="--", label=f"Médiane {median_year}")
    ax_inset.set_title("Distribution des franchissements")
    ax_inset.set_xlabel("Année")
    ax_inset.set_ylabel("Fréquence")
    ax_inset.legend()

plt.tight_layout()

# -----------------------------
# 6. Sauvegarde automatique
# -----------------------------
os.makedirs("../figures", exist_ok=True)
plt.savefig("../figures/synthese.png", dpi=300)
plt.show()
