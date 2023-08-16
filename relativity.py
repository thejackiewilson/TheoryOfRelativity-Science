import math

def time_dilation_factor(velocity_fraction):
    """
    Calculate the time dilation factor for a given velocity as a fraction of the speed of light.

    :param velocity_fraction: Velocity as a fraction of the speed of light (0 <= velocity_fraction < 1)
    :return: Time dilation factor
    """
    if velocity_fraction < 0 or velocity_fraction >= 1:
        raise ValueError("Velocity fraction must be in the range [0, 1)")
    
    return 1 / math.sqrt(1 - velocity_fraction**2)

def main():
    speed_of_light = 299792458  # Speed of light in meters per second (m/s)
    velocity_fraction = 0.9  # Velocity as a fraction of the speed of light

    dilation_factor = time_dilation_factor(velocity_fraction)
    print(f"Time dilation factor for {velocity_fraction * 100}% the speed of light: {dilation_factor}")

if __name__ == "__main__":
    main()


# This script calculates the time dilation factor for an object moving at 90% of the speed of light. 
# The factor represents how much slower time appears to pass for the object compared to a stationary observer. 
# Note that the velocity_fraction parameter should be in the range [0, 1), where 0 represents an object at rest, and values closer to 1 represent velocities approaching the speed of light.
