import matplotlib.pyplot as plt
import numpy as np
     

graphs = ['Graph 1', 'Graph 2', 'Graph 3']
dijkstra_times = [0.00030, 0.00040, 0.00060]
bellman_ford_times = [0.00010, 0.00040, 0.00100]
     

# Create a bar width
bar_width = 0.35
index = np.arange(len(graphs))
     

# Create a figure and axis
fig, ax = plt.subplots()

# Plot bars for Dijkstra and Bellman-Ford times
bar1 = ax.bar(index, dijkstra_times, bar_width, label='Dijkstra')
bar2 = ax.bar(index + bar_width, bellman_ford_times, bar_width, label='Bellman-Ford')

# Add labels and title
ax.set_xlabel('Graph')
ax.set_ylabel('Time (ms)')
ax.set_title('Performance Comparison of Dijkstra vs Bellman-Ford')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(graphs)
ax.legend()

# Show the plot
plt.tight_layout()
plt.show()