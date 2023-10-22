import numpy as np
import matplotlib.pyplot as plt
import webcolors


class Mandelbrot:
    def __init__(self, max_iter: int, width: int, height: int, color: tuple) -> None:
        self.max_iter = max_iter
        self.width, self.height = width, height
        self.xmin, self.xmax = -2.0, 1.0
        self.ymin, self.ymax = -1.5, 1.5
        self.color = color

    def __mandelbrot(self, c: int) -> int:
        z = 0
        n = 0
        while abs(z) <= 2 and n < self.max_iter:
            z = z * z + c
            n += 1
        return n

    def __generate_graph(self) -> None:
        img = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        for x in range(self.width):
            for y in range(self.height):
                real = self.xmin + (self.xmax - self.xmin) * x / (self.width - 1)
                imag = self.ymin + (self.ymax - self.ymin) * y / (self.height - 1)
                c = complex(real, imag)
                color = self.__mandelbrot(c)
                img[y, x] = self.color if color == self.max_iter else (0, 0, 0)
        return img

    def show_graph(self) -> None:
        img = self.__generate_graph()
        plt.imshow(img, extent=(self.xmin, self.xmax, self.ymin, self.ymax))
        plt.title('Mandelbrot Fractal')
        plt.xlabel('Real')
        plt.ylabel('Imaginary')
        plt.show()

# Example usage
max_iter = 256
width, height = 800, 800
hex_color = '#81a12f'  # You can choose any RGB color you prefer
mandelbrot_set = Mandelbrot(max_iter, width, height, webcolors.hex_to_rgb(hex_color))
mandelbrot_set.show_graph()
