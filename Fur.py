import fractal
import random
import numpy as np
import matplotlib.pyplot as plt

def generate_fractal_fur():
    # Create a fractal object with random parameters
    f = fractal.Fractal(random.randint(3, 6), random.uniform(0.1, 0.9), random.uniform(0.1, 0.9))
    # Generate the fractal shape
    fur = f.generate()
    # Add noise to the fractal shape to make it look more like fur
    noise = np.random.normal(0, 0.05, fur.shape)
    fur = fur + noise
    fur = np.clip(fur, 0, 1)
    # Apply a fur-like color map to the fractal shape
    fur = plt.cm.Oranges(fur)
    # Return the fractal fur
    return fur

# Generate 10 fractal fur images
for i in range(10):
    fur = generate_fractal_fur()
    plt.imsave("fractal_fur_{}.png".format(i), fur)
