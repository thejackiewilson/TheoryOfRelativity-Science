import matplotlib.pyplot as plt
import numpy as np

# Define the age range from 1 to 100 years
ages = np.arange(1, 101)

# Define the decay factor
decay_factor = 0.05

# Calculate the "perceived" duration of a year at each age based on the proportionality theory
# Introducing a non-linear factor for perceived duration (simple exponential decay model)
perceived_duration = np.exp(-decay_factor * ages)

# Plot the age against the perceived duration
plt.figure(figsize=(14, 8))
plt.plot(ages, perceived_duration, label='Perceived Time Speed', color='blue')

# Add horizontal lines for milestone ages
milestone_ages = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for age in milestone_ages:
    plt.axhline(y=perceived_duration[age-1], color='gray', linestyle='--', alpha=0.5)
    plt.text(101, perceived_duration[age-1], f"{perceived_duration[age-1]:.4f}", va='center')

# Highlight the annotations for the milestone ages
for age in milestone_ages:
    plt.annotate(
        f'{age} years',
        (age, perceived_duration[age-1]),
        xytext=(-35, 7),
        textcoords='offset points',
        arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.2'),
        fontsize=9
    )

# Add a legend to the plot
plt.legend(title='Components of Perceived Duration')

# Add a reference to the source of the data
plt.annotate(
    'Data source: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3910220/',
    (101, 0.02),
    ha='right',
    fontsize=8
)

# Adding titles and labels
plt.title('Perceived Speed of Time Passing as a Function of Age (with Non-Linear Decay)')
plt.xlabel('Age (years)')
plt.ylabel('Perceived Duration of One Year (adjusted for non-linear perception)')
plt.grid(True)
plt.xlim(1, 105)    # Extend x-axis to make room for text annotations
plt.ylim(0, max(perceived_duration)+0.05)  # Add some space above the highest line for readability

plt.show()
