import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class GewohnheitsExperiment:
    def __init__(self, titel, bereich, definition, messmethode, ergebnisse, theorie):
        self.titel = titel
        self.bereich = bereich
        self.definition = definition
        self.messmethode = messmethode
        self.ergebnisse = ergebnisse
        self.theorie = theorie

    def anzeigen(self):
        print(f"\n--- {self.titel} ---")
        print(f"Forschungsbereich: {self.bereich}")
        print(f"Definition: {self.definition}")
        print(f"Messmethode: {self.messmethode}")
        print(f"Ergebnisse: {self.ergebnisse}")
        print(f"Theoretische Implikationen: {self.theorie}")

# Instanzen der Experimente erstellen
exp1 = GewohnheitsExperiment(
    titel="Stimulus-Response-Gewohnheiten",
    bereich="Assoziatives Lernen",
    definition="Gewohnheiten sind durch Reize ausgelöste Verhaltensweisen, die durch wiederholte Verstärkung entstehen.",
    messmethode="Untersuchungen an Tiermodellen mit Belohnungsentwertung und Kontingenzabbau.",
    ergebnisse="Verhalten bleibt trotz Entwertung der Belohnung bestehen, was auf Gewohnheitsbildung hinweist.",
    theorie="Unterstützt die Ansicht, dass Gewohnheiten unabhängig von zielgerichteten Systemen operieren."
)

exp2 = GewohnheitsExperiment(
    titel="Selbstberichtete Gesundheitsgewohnheiten",
    bereich="Gesundheitspsychologie",
    definition="Gewohnheiten sind automatische Handlungen, die durch Kontext-Reaktions-Assoziationen entstehen.",
    messmethode="Selbstberichtsskalen wie der Self-Report Habit Index (SRHI).",
    ergebnisse="Stärkere selbstberichtete Gewohnheiten sagen Verhaltenskonsistenz voraus.",
    theorie="Gewohnheiten können bewusst reflektiert werden, operieren aber meist unbewusst."
)

exp3 = GewohnheitsExperiment(
    titel="Lernen von Bewegungssequenzen",
    bereich="Motorische Kontrolle",
    definition="Gewohnheiten sind Fähigkeiten, die durch Wiederholung automatisch werden.",
    messmethode="Reaktionszeiten und Genauigkeit in sequentiellen Reaktionszeitaufgaben.",
    ergebnisse="Leistung verbessert sich mit Übung, was auf Beteiligung des prozeduralen Gedächtnisses hinweist.",
    theorie="Zeigt eine neuronale Verschiebung von kortikaler Kontrolle zu subkortikalen Strukturen wie den Basalganglien."
)

# Liste der Experimente
experimente = [exp1, exp2, exp3]

# Darstellung der Experimente
for exp in experimente:
    exp.anzeigen()

# Daten für Visualisierung vorbereiten
daten = {
    "Titel": [exp.titel for exp in experimente],
    "Forschungsbereich": [exp.bereich for exp in experimente],
    "Messmethode": [exp.messmethode for exp in experimente],
    "Ergebnisse": [exp.ergebnisse for exp in experimente]
}

df = pd.DataFrame(daten)

# Balkendiagramm erstellen
plt.figure(figsize=(10, 6))
sns.set(style="whitegrid")
sns.countplot(y="Forschungsbereich", data=df, palette="crest", order=df["Forschungsbereich"])
plt.title("Forschungsbereiche zu Gewohnheiten", fontsize=16)
plt.xlabel("Anzahl")
plt.ylabel("Forschungsbereich")
plt.tight_layout()
plt.show()
