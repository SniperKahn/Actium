import numpy as np
import matplotlib.pyplot as plt

def dh_matrix(theta, d, a, alpha):
    alpha_rad = np.radians(alpha)
    return np.array([
        [np.cos(theta), -np.sin(theta)*np.cos(alpha_rad),  np.sin(theta)*np.sin(alpha_rad), a*np.cos(theta)],
        [np.sin(theta),  np.cos(theta)*np.cos(alpha_rad), -np.cos(theta)*np.sin(alpha_rad), a*np.sin(theta)],
        [0,              np.sin(alpha_rad),               np.cos(alpha_rad),              d],
        [0,              0,                                0,                              1]
    ])

def plot_arm(angles_deg):
    angles_rad = np.radians(angles_deg)
    L1, L2, L3, L4 = 70, 120, 100, 60 # mm
    
    # Table: [theta, d, a, alpha]
    dh_table = [
        [angles_rad[0], L1, 0,   0],
        [angles_rad[1], 0,  0,   90],
        [angles_rad[2], 0,  L2,  0],
        [angles_rad[3], 0,  L3,  0],
        [angles_rad[4], L4, 0,   90]
    ]
    
    points = [[0, 0, 0]] # Start at origin
    T_accumulator = np.eye(4)
    
    for row in dh_table:
        T_link = dh_matrix(*row)
        T_accumulator = T_accumulator @ T_link
        # Extract the position (x, y, z) from the cumulative matrix
        points.append(T_accumulator[:3, 3])
    
    # Visualization using Matplotlib
    pts = np.array(points)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(pts[:,0], pts[:,1], pts[:,2], '-o', lw=3, markersize=8)
    ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z')
    ax.set_title("5DOF Digital Twin")
    plt.show()

# Test the plot
plot_arm([90, 90, 90, 90, 90])