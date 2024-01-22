import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.animation import FuncAnimation
from matplotlib.transforms import Affine2D
from matplotlib.widgets import Button


def find_fourth_point(points):
    p1, p2, p3 = points
    vector_B = [p3[0] - p2[0], p3[1] - p2[1]]
    p4 = [p1[0] + vector_B[0], p1[1] + vector_B[1]]
    return p4


def apply_affine_transform(matrix, points):
    transformed_points = []
    for x, y in points:
        point = np.array([[x], [y], [1]])  # Convert to column vector
        """
        x
        y
        1
        """
        transformed_point = matrix @ point
        transformed_points.append((transformed_point[0, 0],
                                   transformed_point[1, 0]))
    return transformed_points


def update_animation(frame, poly, points, vertex, scale):
    theta = np.radians(-frame)
    vertices = np.array(points)
    rotation_vertex = vertices[vertex]

    scale_factor = 1 - frame * scale / 360.0

    transform_matrix = Affine2D()
    """
    1 0 0
    0 1 0
    0 0 1
    """
    transform_matrix.rotate_deg_around(rotation_vertex[0], rotation_vertex[1],
                                       np.degrees(theta))
    """
    cos(theta)      -sin(theta)    x - xcos(theta) + ysin(theta)
    sin(theta)       cos(theta)    y - ycos(theta) - xsin(theta)
    0                0             1
    """

    transform_matrix.scale(scale_factor, scale_factor)
    """
    x * scale_factor         0              0
        0              y * scale_factor     0
        0                    0              1
    """
    # Apply affine transformation to all vertices
    transformed_vertices = apply_affine_transform(transform_matrix.
                                                  get_matrix(), vertices)

    # Update the xy data of the existing Polygon
    poly.set_xy(transformed_vertices)


def toggle_animation(event, anim):
    global running
    if running:
        anim.event_source.stop()
    else:
        anim.event_source.start()
    running = not running


def animate_rotation(points, vertex, scale):
    global running
    running = True
    fig, ax = plt.subplots()
    ax.grid(True)
    points.append(find_fourth_point(points))

    # Create an initial Polygon
    poly = Polygon(points, closed=True, edgecolor='b')
    ax.add_patch(poly)

    anim = FuncAnimation(fig, update_animation,
                         fargs=(poly, points, vertex, scale),
                         frames=np.arange(0, 360, 1), interval=50)

    # Add a button to start/stop the animation
    ax_button = plt.axes([0.81, 0.01, 0.1, 0.04])
    button = Button(ax_button, 'Start/Stop', color='lightgoldenrodyellow',
                    hovercolor='0.975')
    button.on_clicked(lambda event: toggle_animation(event, anim))

    # Adjust the limits to zoom out
    ax.set_xlim(-3, 5)
    ax.set_ylim(-3, 3)

    plt.show()
