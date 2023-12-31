import numpy as np
import matplotlib.pyplot as plt

def visible_matter_curve(r, luminous_mass):
    # Using Kepler's law simplified for circular orbits and a central mass.
    velocity = np.sqrt(luminous_mass / r)
    return velocity

def dark_matter_curve(r, luminous_mass, dark_matter_factor):
    # We'll simulate the effect of dark matter by keeping the velocity flat after a certain radius.
    base_velocity = np.sqrt(luminous_mass / r)
    dark_matter_effect = dark_matter_factor / (1 + np.exp(-r + 2))  # Sigmoid function centered at r=2
    velocity = base_velocity + dark_matter_effect
    return velocity

# Create a range of distances from the galactic center
r = np.linspace(0.1, 10, 400)

# Compute velocities
v_visible = visible_matter_curve(r, 1)
v_dark_matter = dark_matter_curve(r, 1, 2.0)

plt.figure(figsize=(10, 6))
plt.plot(r, v_visible, label='Visible Matter Only')
plt.plot(r, v_dark_matter, label='With Dark Matter Influence', linestyle='--')
plt.axhline(y=1.0, color='r', linestyle='-.', label='1.0 Rotational Velocity')
plt.axvline(x=2.0, color='g', linestyle='-.', label='2.0 Distance from Center')
plt.xlabel('Distance from Galactic Center')
plt.ylabel('Rotational Velocity')
plt.title('Galaxy Rotation Curves')
plt.legend()
plt.grid(True)
plt.show()

#This visual representation underscores the concept of dark matter: even though we cannot directly observe dark matter, its influence is evident in the rotation curves of galaxies.

#As the rotational velocity decreases steadily with dark matter influence, but rather falling into a slower velocity further away, dark matter speeds up as its distance increases. Perpendicular until 1.0 rotational velocity combined with a near 2 Distance from Galactic Center. 

#In galaxies without the influence of dark matter, we would expect the rotational velocities of stars to decrease with increasing distance from the galactic center. However, in the presence of dark matter, the rotation curves tend to remain flat or even increase, suggesting a large amount of unseen mass (dark matter) outside the visible galaxy.
