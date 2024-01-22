import cv2
import matplotlib.pyplot as plt
import numpy as np


from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def rgb_to_hsv(contents: bytes):
    image = Image.open(io.BytesIO(contents))
    image_rgb = np.array(image)

    # Assuming image_rgb is in the range [0, 255]
    image_rgb = image_rgb.astype(np.uint8)

    # Convert RGB to HSV
    image_hsv = matplotlib.colors.rgb_to_hsv(image_rgb / 255.0)

    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(image_rgb)
    plt.title('Input Image (RGB)')

    plt.subplot(1, 2, 2)
    plt.imshow(matplotlib.colors.hsv_to_rgb(image_hsv))
    plt.title('Result Image (HSV)')

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

    # manager = plt.get_current_fig_manager()
    # manager.window.wm_geometry("+880+380")
    # manager.resize(975, 550)
    plt.show()
