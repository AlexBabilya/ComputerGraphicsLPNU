import numpy as np
import matplotlib.pyplot as plt


class BrownianMotion():
    def __init__(self, num_steps: int, color: str,
                 dt: float, diffusion_coefficient: float) -> None:
        self.num_steps = num_steps
        self.dt = dt
        self.diffusion_coefficient = diffusion_coefficient
        self.timesteps = np.arange(0, self.num_steps) * self.dt
        self.positions_x = np.zeros(self.num_steps)
        self.positions_y = np.zeros(num_steps)
        self.color = color

    def __brownian_motion(self) -> None:
        for i in range(1, self.num_steps):
            displacement_x = np.random.normal(
                0, np.sqrt(2 * self.diffusion_coefficient * self.dt))
            displacement_y = np.random.normal(
                0, np.sqrt(2 * self.diffusion_coefficient * self.dt))

            self.positions_x[i] = self.positions_x[i - 1] + displacement_x
            self.positions_y[i] = self.positions_y[i - 1] + displacement_y

    def show_graph(self) -> None:
        self.__brownian_motion()
        plt.figure(figsize=(8, 6))
        plt.plot(self.positions_x,
                 self.positions_y,
                 label='2D Brownian Motion',
                 color=self.color)
        plt.title('2D Brownian Motion')
        plt.xlabel('X Position')
        plt.ylabel('Y Position')
        plt.legend()
        plt.grid(True)
        manager = plt.get_current_fig_manager()
        manager.window.wm_geometry("+900+400")
        manager.resize(975, 550)
        plt.show()
