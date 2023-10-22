import matplotlib.pyplot as plt

# Create a figure
manager = plt.get_current_fig_manager()
print(type(*manager.window.maxsize()[0]))

# Show the plot
