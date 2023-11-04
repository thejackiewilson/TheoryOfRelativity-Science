import matplotlib.pyplot as plt
import numpy as np

# Define the age range from 1 to 100 years
ages = np.arange(1, 101)

# Calculate the "perceived" duration of a year at each age based on the proportionality theory
# Using the formula: perceived_duration = 1 / age
perceived_duration = 1 / ages

# Plot the age against the perceived duration
plt.figure(figsize=(10, 6))
plt.plot(ages, perceived_duration, label='Perceived Time Speed')

# Adding titles and labels
plt.title('Perceived Speed of Time Passing as a Function of Age')
plt.xlabel('Age (years)')
plt.ylabel('Perceived Duration of One Year (proportional to lifetime)')
plt.legend()
plt.grid(True)
plt.show()