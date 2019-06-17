# uncomment the next line if running in a notebook
# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

scenario = int(input("Scenario (1-4): "))

m = 1
M = 6.42 * (10 ** 23)
G = 6.673 * (10 ** -11)
R = 3386000.0

if (scenario == 1): # Straight down descent from 10 km
    x = np.array([R + 10000, 0, 0]) 
    v = np.array([0, 0, 0])
    t_max = 100
    dt = 1
elif (scenario == 2): # Circular orbit at h m
    h = 100000
    x = np.array([R + h, 0, 0]) 
    v = np.array([0, ((G*M)/(R + h)) ** (1/2), 0])
    t_max = 6500
    dt = 0.1
elif (scenario == 3): # Circular orbit at perigee h m
    h = 100000
    e = 0.5
    x = np.array([R + h, 0, 0]) 
    v = np.array([0, ((G*M*(1+e))/(R + h)) ** (1/2), 0])
    t_max = 18000
    dt = 1
elif (scenario == 4): # Hyperbolic escape
    x = np.array([R, 0, 0]) 
    v = np.array([0, ((2*G*M)/(R)) ** (1/2), 0])
    t_max = 100000
    dt = 1


# simulation time, timestep and time

t_array = np.arange(0, t_max, dt)

# initialise empty lists to record trajectories
x_list = []
v_list = []

# Verlet integration
for i, t in enumerate(t_array):

    # append current state to trajectories
    x_list.append(x)

    # calculate new position
    a = -(G * M * x) / (np.linalg.norm(x)**3)

    # Make a good estimate at the next position if not starting from rest
    if i < 1 and np.linalg.norm(v) != 0:
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
if (scenario == 1):

    alt = [item[0] for item in x_array]
    
    plt.figure(1)
    plt.clf()
    plt.xlabel('time (s)')
    plt.grid()
    plt.plot(t_array, alt, label='altitude (m)')
    plt.axhline(y=R, xmin=0, xmax=1, color='red', linestyle='--', label='Surface')
    plt.legend()
    plt.show()

else:

    x = [item[0] for item in x_array]
    y = [item[1] for item in x_array]
    
    plt.figure(1)
    plt.clf()
    plt.xlabel('x (m)')
    plt.ylabel('y (m)')
    plt.grid()
    plt.plot(x, y)
    plt.legend()
    mars = plt.Circle((0,0),R,color='r')
    plt.gcf().gca().add_artist(mars)
    plt.axes().set_aspect('equal', 'datalim')
    plt.show()
    

