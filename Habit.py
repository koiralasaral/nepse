from graphviz import Digraph
import matplotlib.pyplot as plt

# Define a class to represent each habit experiment
class HabitExperiment:
    def __init__(self, title, field, definition, measurement, findings, theory):
        self.title = title
        self.field = field
        self.definition = definition
        self.measurement = measurement
        self.findings = findings
        self.theory = theory

# Create sample experiments
exp1 = HabitExperiment(
    title="Experiment on Stimulus-Response Habits",
    field="Associative Learning",
    definition="Habits are stimulus-driven behaviors formed through repeated reinforcement.",
    measurement="Observed in animal models via reward devaluation and contingency degradation.",
    findings="Behavior persists even after reward is devalued, indicating habit formation.",
    theory="Supports the view that habits operate independently of goal-directed systems."
)

exp2 = HabitExperiment(
    title="Self-Reported Habit Tracking in Health Behaviors",
    field="Health Psychology",
    definition="Habits are actions performed automatically due to context-response association.",
    measurement="Self-report scales like the Self-Report Habit Index (SRHI).",
    findings="Stronger self-reported habits predict behavior consistency over time.",
    theory="Habits can be consciously reflected on but typically operate outside awareness."
)

exp3 = HabitExperiment(
    title="Motor Sequence Learning Task",
    field="Motor Control Research",
    definition="Habits are skills that become automatic through repetition.",
    measurement="Response times and accuracy in serial reaction time tasks.",
    findings="Performance improves with practice, indicating procedural memory involvement.",
    theory="Shows neural shift from cortical control to subcortical (e.g., basal ganglia) as habits form."
)

# Create a list of experiments
experiments = [exp1, exp2, exp3]

# Visualize the distribution of fields of study
fields = [exp.field for exp in experiments]
field_counts = {field: fields.count(field) for field in set(fields)}

plt.bar(field_counts.keys(), field_counts.values(), color='skyblue', alpha=0.8)
plt.title("Distribution of Habit Research Fields")
plt.ylabel("Number of Experiments")
plt.xlabel("Fields of Study")
plt.xticks(rotation=45)
plt.show()

# Generate a flowchart for a concept (e.g., habit formation process)
dot = Digraph(comment='Habit Formation')
dot.node('S', 'Stimulus')
dot.node('D', 'Decision Point')
dot.node('G', 'Goal-Directed\n(Prefrontal Cortex)')
dot.node('H', 'Habitual\n(Dorsolateral Striatum)')
dot.node('O1', 'Outcome Eval')
dot.node('O2', 'Automated Response')

dot.edges(['SD'])
dot.edge('D', 'G', label='if deliberative')
dot.edge('D', 'H', label='if routine')
dot.edge('G', 'O1')
dot.edge('H', 'O2')

# Save and render the flowchart
dot.render('C:/Users/LENOVO/Desktop/flowchart/habit_formation_flowchart', format='png', cleanup=True)
print("Flowchart saved as 'habit_formation_flowchart.png'")