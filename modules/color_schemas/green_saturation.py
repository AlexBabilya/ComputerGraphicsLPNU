from PIL import Image
import matplotlib.pyplot as plt
import numpy as np


def change_green_saturation(image_path, coefficient):
    original_img = Image.open(image_path).convert("RGB")

    fig, axes = plt.subplots(1, 2, figsize=(10, 5))

    axes[0].imshow(np.asarray(original_img))
    axes[0].set_title("Original Image")

    width, height = original_img.size
    for i in range(width):
        for j in range(height):
            pixel = original_img.getpixel((i, j))
            r, g, b = pixel
            if not isinstance(pixel, tuple):
                r, g, b = (pixel, pixel, pixel)
            if g > 0:
                if coefficient < 50:
                    new_g = max(0, g - (g * coefficient / 100))
                elif coefficient > 50:
                    new_g = min(255, (g + ((255 - g)
                                           * (coefficient - 50) / 100)))
                else:
                    new_g = g
                original_img.putpixel((i, j), (r, int(new_g), b))

    axes[1].imshow(np.asarray(original_img))
    axes[1].set_title(f"Modified Image (Green Saturation: {coefficient}%)")

    # Show the plot
    # manager = plt.get_current_fig_manager()
    # manager.window.wm_geometry("+880+380")
    # manager.resize(975, 550)
    plt.show()
