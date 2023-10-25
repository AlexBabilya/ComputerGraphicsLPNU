import numpy as np
import matplotlib.pyplot as plt


class BrownianMotion():
    def __init__(self, num_steps: int, color: str,
                 dt: int, diffusion_coefficient: int) -> None:
        self.num_steps = num_steps
        self.dt = dt / 10
        # This parameter represents the time step size.
        # It determines the intervals at which
        # the position of the particle is updated in the simulation.
        self.diffusion_coefficient = diffusion_coefficient / 10
        # This parameter represents the diffusion coefficient,
        # which is a measure of how particles spread out over time.
        self.positions_x = np.zeros(self.num_steps)
        self.positions_y = np.zeros(num_steps)
        self.color = color

    def __brownian_motion(self) -> None:
        for i in range(1, self.num_steps):
            # Calculate the variance of the normal distribution
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
                 label='Brownian Motion',
                 color=self.color)
        plt.title('Brownian Motion')
        plt.xlabel('X Position')
        plt.ylabel('Y Position')
        plt.legend()
        plt.grid(True)
        manager = plt.get_current_fig_manager()
        manager.window.wm_geometry("+880+380")
        manager.resize(975, 550)
        plt.show()
