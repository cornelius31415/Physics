
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 13:30:20 2024

@author: cornelius
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import derivative
from scipy.optimize import fsolve

# Konstanten definieren
r_s = 2  # Schwarzschild-Radius
m = 1    # Masse des Teilchens
l_values = [1, 5, 7, 11]  # Verschiedene Drehimpulse

# Effektives Potential definieren
def v_eff_schwarzschild(r, r_s, m, l):
    term1 = (1 - r_s / r)
    term2 = m**2 + l**2 / r**2
    return term1 * term2

# Ableitung des Potentials
def v_eff_prime(r, r_s, m, l):
    return derivative(v_eff_schwarzschild, r, dx=1e-6, args=(r_s, m, l))

# Kritische Punkte finden
def find_critical_points(r_s, m, l):
    initial_guesses = np.linspace(2.1, 80, 10)  # Realistische Startwerte
    critical_points = []

    for guess in initial_guesses:
        try:
            root = fsolve(v_eff_prime, guess, args=(r_s, m, l))[0]
            if 2.1 < root < 100 and root not in critical_points:  # Filterung
                critical_points.append(root)
        except Exception as e:
            pass

    return sorted(critical_points)

# Plot erstellen
plt.figure(figsize=(10, 6))  # Größere Plot-Größe
r = np.linspace(2.1, 200, 500)  # Weniger Punkte für bessere Performance

# Farben für jede Kurve
colors = ['blue', 'green', 'orange', 'purple']

for l, color in zip(l_values, colors):
    v_eff_values = v_eff_schwarzschild(r, r_s, m, l)
    plt.plot(r, v_eff_values, label=f"L={l}", color=color)

    # Kritische Punkte berechnen
    critical_points = find_critical_points(r_s, m, l)
    for point in critical_points:
        v_value = v_eff_schwarzschild(point, r_s, m, l)
        # Kritische Punkte in Kurvenfarbe mit schwarzer Umrandung
        plt.scatter(point, v_value, color=color, edgecolor='black', s=100, zorder=5)

plt.axhline(0, color="black", linewidth=0.5, linestyle="--")
plt.title("Schwarzschild Metric Effective Potential for Massive Bodies")
plt.xlabel("r")
plt.ylabel("$V_{eff}(r)$")
plt.ylim(-0.1, 5)  # Y-Achse begrenzen
plt.xlim(2, 50)    # X-Achse begrenzen
plt.grid()
plt.legend()
plt.savefig("BHeffective.png", format="png")
plt.show()




# Konstanten definieren
l_values = [0.2, 0.6, 2, 3]  # Verschiedene Drehimpulse
mu = 1  # reduzierte Masse

# Effektives Potential definieren
def v_eff(r, l, mu):
    gravitational_term = -1 / r
    centrifugal_term = (l**2) / (2 * mu * r**2)
    return gravitational_term + centrifugal_term

# Ableitung des Potentials
def v_eff_prime(r, l, mu):
    return derivative(v_eff, r, dx=1e-6, args=(l, mu))

# Kritische Punkte finden
def find_critical_points(l, mu):
    initial_guesses = np.linspace(0.2, 5, 10)  # Realistische Startwerte
    critical_points = []

    for guess in initial_guesses:
        try:
            root = fsolve(v_eff_prime, guess, args=(l, mu))[0]
            if 0.1 < root < 5 and root not in critical_points:  # Filterung
                critical_points.append(root)
        except Exception as e:
            pass

    return sorted(critical_points)

# Plot erstellen
plt.figure(figsize=(8, 6))
r = np.linspace(0.1, 5, 500)

# Farben für jede Kurve
colors = ['blue', 'green', 'orange','red']

for l, color in zip(l_values, colors):
    v_eff_values = v_eff(r, l, mu)
    plt.plot(r, v_eff_values, label=f"L={l}", color=color)

    # Kritische Punkte berechnen
    critical_points = find_critical_points(l, mu)
    for point in critical_points:
        v_value = v_eff(point, l, mu)
        # Kritische Punkte in Kurvenfarbe mit schwarzer Umrandung
        plt.scatter(point, v_value, color=color, edgecolor='black', s=100, zorder=5)

plt.axhline(0, color="black", linewidth=0.5, linestyle="--")
plt.title("Effective Potential in Newtonian Mechanics")
plt.xlabel("r")
plt.ylabel("$V_{eff}(r)$")
plt.ylim(-5, 5)
plt.grid()
plt.legend()
plt.savefig("newtonEffective.png", format="png")
plt.show()
