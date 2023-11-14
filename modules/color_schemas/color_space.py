import cv2
import matplotlib.pyplot as plt
import numpy as np


def rgb_to_hsv(contents: bytes):
    image_np = np.frombuffer(contents, np.uint8)
    image_rgb = cv2.imdecode(image_np, cv2.IMREAD_UNCHANGED)

    image_hsv = cv2.cvtColor(image_rgb, cv2.COLOR_BGR2HSV)
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(image_rgb, cv2.COLOR_BGR2RGB))
    plt.title('Input Image (RGB)')

    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(image_hsv, cv2.COLOR_BGR2RGB))
    plt.title('Result Image (HSV)')

    manager = plt.get_current_fig_manager()
    manager.window.wm_geometry("+880+380")
    manager.resize(975, 550)
    plt.show()


def hsv_to_rgb(contents: bytes):
    image_np = np.frombuffer(contents, np.uint8)
    image_hsv = cv2.imdecode(image_np, cv2.IMREAD_UNCHANGED)

    image_rgb = cv2.cvtColor(image_hsv, cv2.COLOR_HSV2BGR)
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(image_hsv, cv2.COLOR_BGR2RGB))
    plt.title('Input Image (HSV)')

    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(image_rgb, cv2.COLOR_BGR2RGB))
    plt.title('Result Image (RGB)')

    manager = plt.get_current_fig_manager()
    manager.window.wm_geometry("+880+380")
    manager.resize(975, 550)
    plt.show()
