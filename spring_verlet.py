# uncomment the next line if running in a notebook
# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

# mass, spring constant, initial position and velocity
m = 1
k = 1
x = 0
v = 1

# simulation time, timestep and time
t_max = 100
dt = 0.001 # Must be less than 1 or starts to become unstable
t_array = np.arange(0, t_max, dt)

# initialise empty lists to record trajectories
x_list = []
v_list = []

# Euler integration
for i, t in enumerate(t_array):

    # append current state to trajectories
    x_list.append(x)

    # calculate new position
    a = -k * x / m

    # Make a good estimate at the next position if not starting from rest
    if i < 1 and v != 0:
        x = x + dt * v; 
    else:
        x = 2 * x - x_list[i-1] + (dt ** 2) * a

for j, t in enumerate(t_array[1:-1]):

    i = j + 1
    
    # append current state to trajectories
    v_list.append(v)

    # calculate new velocity
    v = (x_list[i+1] - x_list[i-1]) / (2 * dt)

# Boundary conditions
v_list[0] = None
v_list[-1] = None   

# convert trajectory lists into arrays, so they can be sliced (useful for Assignment 2)
x_array = np.array(x_list)
v_array = np.array(v_list)

# plot the position-time graph
plt.figure(1)
plt.clf()
plt.xlabel('time (s)')
plt.grid()
plt.plot(t_array, x_array, label='x (m)')
plt.plot(t_array[1:-1], v_array, label='v (m/s)')
plt.legend()
plt.show()
