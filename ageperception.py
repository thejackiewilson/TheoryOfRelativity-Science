import matplotlib.pyplot as plt
import numpy as np

# Define the age range from 1 to 100 years
ages = np.arange(1, 101)

# Define the decay factor for the perceived duration calculation
decay_factor = 0.05

# Calculate the "perceived" duration of a year at each age using an exponential decay to simulate non-linear perception
perceived_duration = np.exp(-decay_factor * ages)

# Define milestone ages for annotations and horizontal lines
milestone_ages = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Plot the age against the perceived duration
plt.figure(figsize=(14, 8))
plt.plot(ages, perceived_duration, label='Perceived Time Speed', color='blue', lw=2)

# Add horizontal lines for milestone ages
# Define a color map to differentiate milestone ages
colors = plt.cm.viridis(np.linspace(0, 1, len(milestone_ages)))

for age, color in zip(milestone_ages, colors):
    plt.axhline(y=perceived_duration[age-1], color=color, linestyle='--', alpha=0.7, lw=1)
    plt.text(101, perceived_duration[age-1], f"{perceived_duration[age-1]:.4f}", va='center', color=color)

# Highlight the annotations for the milestone ages with dynamic positioning to avoid overlap
offsets = np.linspace(10, -10, len(milestone_ages))
for age, offset, color in zip(milestone_ages, offsets, colors):
    plt.annotate(
        f'{age} years',
        (age, perceived_duration[age-1]),
        xytext=(15, offset),
        textcoords='offset points',
        arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.2', color=color),
        fontsize=9,
        color=color
    )

# Add a legend to the plot
plt.legend(title='Components of Perceived Duration')

# Add a reference to the source of the data (One provided isn't real)
plt.annotate(
    'Example source: Hypothetical model based on proportionality and non-linear decay',
    (1, -0.08),
    xycoords=('axes fraction', 'axes fraction'),
    ha='left',
    va='top',
    fontsize=8
)

# Adding titles and labels
plt.title('Perceived Speed of Time Passing as a Function of Age (with Non-Linear Decay)')
plt.xlabel('Age (years)')
plt.ylabel('Perceived Duration of One Year (adjusted for non-linear perception)')
plt.grid(True)
plt.xlim(1, 105)  # Extend x-axis to make room for text annotations
plt.ylim(0, max(perceived_duration)+0.05)  # Add some space above the highest line for readability

plt.show()
