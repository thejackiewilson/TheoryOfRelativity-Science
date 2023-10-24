import numpy as np
import matplotlib.pyplot as plt

def visible_matter_curve(r, luminous_mass):
    # Using Kepler's law simplified for circular orbits and a central mass.
    # v^2 = G*M/r
    # For simplicity, we'll set G = 1 and scale everything else accordingly.
    velocity = np.sqrt(luminous_mass / r)
    return velocity

def dark_matter_curve(r, luminous_mass, dark_matter_factor):
    # We'll simulate the effect of dark matter by adding a term that increases velocity.
    velocity = np.sqrt(luminous_mass / r + dark_matter_factor * r)
    return velocity

# Create a range of distances from the galactic center
r = np.linspace(0.1, 10, 400)

# Compute velocities
v_visible = visible_matter_curve(r, 1)
v_dark_matter = dark_matter_curve(r, 1, 0.2)

plt.figure(figsize=(10, 6))
plt.plot(r, v_visible, label='Visible Matter Only')
plt.plot(r, v_dark_matter, label='With Dark Matter Influence', linestyle='--')
plt.xlabel('Distance from Galactic Center')
plt.ylabel('Rotational Velocity')
plt.title('Galaxy Rotation Curves')
plt.legend()
plt.grid(True)
plt.show()
