#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 08:16:40 2024

@author: cornelius
"""

import numpy as np
import matplotlib.pyplot as plt

def minkowski_diagram():
    # Erstellen des Diagramms
    fig, ax = plt.subplots(figsize=(8, 8))

    # Grenzen des Diagramms
    ax.set_xlim(-3, 8)
    ax.set_ylim(-2, 10)

    # Zeit- und Raumachsen
    ax.axhline(0, color='black', linewidth=0.8, linestyle='--')
    ax.axvline(0, color='black', linewidth=0.8, linestyle='--')

    # Ereignisse A und B
    event_a = (0, 1)   # Ursprung (t=0, x=0)
    event_b = (0, 8.3)   # Auf der Zeitachse, (t=8, x=0)

    # Plotten der Weltlinie von A nach B (als gerade Linie auf der Zeitachse)
    ax.plot([event_a[0], event_b[0]], [event_a[1], event_b[1]], color='red', linewidth=2, label='free wordline')

    # Erstellen von "wobbly" Weltlinien zwischen A und B

    # Erstellen einer geschwungenen Linie
    t_values = np.linspace(1, 8.3, 500)
    wobble = np.sin(t_values * (1 + 5) * 0.5) * (0.2 + 0.1)  # Wackelbewegung
    x_values = wobble
    ax.plot(x_values, t_values, linestyle='--', linewidth=1.5, label=f'Non-free Worldline')

    # Label für Ereignisse A und B
    ax.scatter(*event_a, color='blue', zorder=5)
    ax.scatter(*event_b, color='blue', zorder=5)

    # Ereignisnamen A und B anzeigen
    ax.text(event_a[0] + 0.5, event_a[1], 'A', color='blue', fontsize=12)
    ax.text(event_b[0] + 0.5, event_b[1], 'B', color='blue', fontsize=12)

    # Achsen beschriften
    ax.set_xlabel('x', fontsize=12)
    ax.set_ylabel('ct', fontsize=12)
    ax.set_title('Minkowski-Diagramm', fontsize=14)

    # Legende anzeigen
    ax.legend(loc='upper right', fontsize=10)

    # Achsenverhältnis festlegen
    ax.set_aspect('equal', adjustable='box')

    # Gitter hinzufügen
    ax.grid(color='gray', linestyle=':', linewidth=0.5)

    # Diagramm als PDF speichern
    plt.savefig("minkowski_diagram.pdf", format="pdf")
    
    # Diagramm anzeigen
    plt.show()

# Funktion aufrufen
minkowski_diagram()
