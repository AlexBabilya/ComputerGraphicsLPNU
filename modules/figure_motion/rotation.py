import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.animation import FuncAnimation


def rotate_point(x, y, cx, cy, theta):
    x_rot = cx + (x - cx) * np.cos(theta) + (y - cy) * np.sin(theta)
    y_rot = cy - (x - cx) * np.sin(theta) + (y - cy) * np.cos(theta)
    return x_rot, y_rot


def find_fourth_point(points):
    p1, p2, p3 = points
    vector_B = [p3[0] - p2[0], p3[1] - p2[1]]
    p4 = [p1[0] + vector_B[0], p1[1] + vector_B[1]]
    return p4


def update_animation(frame, ax, points, vertex, scale):
    ax.clear()
    ax.grid(True)

    theta = np.radians(frame)
    vertices = np.array(points)
    rotation_vertex = vertices[vertex]

    scale_factor = 1 - frame * scale / 360.0

    # Rotate all vertices except the fixed vertex
    rotated_vertices = np.array([rotate_point(v[0], v[1], rotation_vertex[0],
                                              rotation_vertex[1], theta)
                                 if i != vertex else v for i,
                                 v in enumerate(vertices)])
    print(rotated_vertices)
    # Scale the rotated vertices
    scaled_rotated_vertices = rotated_vertices * scale_factor

    parallelogram = Polygon(scaled_rotated_vertices, closed=True,
                            edgecolor='b')
    ax.add_patch(parallelogram)

    ax.set_xlim(-2, 4)
    ax.set_ylim(-2, 2)
    ax.set_aspect('equal', adjustable='box')


def animate_rotation(points, vertex, scale):
    fig, ax = plt.subplots()
    points.append(find_fourth_point(points))
    anm = FuncAnimation(fig, lambda frame: update_animation(frame, ax, points,
                                                            vertex, scale),
                        frames=np.arange(0, 360, 1), interval=50)
    manager = plt.get_current_fig_manager()
    manager.window.wm_geometry("+880+380")
    manager.resize(975, 550)
    plt.show()
