import numpy as np

positions = np.loadtxt("positions.txt", delimiter=",") # m
velocities = np.loadtxt("velocities.txt", delimiter=",") # m
masses = np.loadtxt("masses.txt", delimiter=",") # kg


g = np.array([0, -9.81]) # kg/m-s2

# time increment between the consecutive time steps
dt = 0.01 # s

old_positions = np.copy(positions)

# simulate forces, velocities, and positions for 100 time steps
for step in range(100):
    # update velocities using dv = g*dt
    velocities += g * dt # m/s

    # update positions
    positions += velocities * dt # m


new_positions = positions

np.savetxt("new_positions.txt", new_positions, delimiter=",")
