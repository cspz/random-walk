import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random as rnd

# --- Generate the random walk ---
steps = []
for _ in range(1000):
    steps.append(rnd.uniform(-5, 5))

arr = np.array(steps)

# --- Parameters ---
window_size = 100  # size of the moving buffer

# --- Set up the figure ---
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6))
fig.tight_layout(pad=3)

line_raw,    = ax1.plot([], [], label='Raw data', alpha=0.7)
line_avg,    = ax1.plot([], [], color='red', label='Running mean')
line_std_hi, = ax1.plot([], [], color='orange', linestyle='--', label='+1 std')
line_std_lo, = ax1.plot([], [], color='orange', linestyle='--', label='-1 std')

ax1.set_xlim(0, window_size)
ax1.set_ylim(-8, 8)
ax1.legend(loc='upper right')
ax1.set_title('Random Walk — Sliding Window')
ax1.set_ylabel('Value')

# Bar chart for live stats
stats_labels = ['Mean', 'Std Dev', 'Min', 'Max']
bars = ax2.bar(stats_labels, [0, 0, 0, 0], color=['red', 'orange', 'blue', 'green'])
ax2.set_ylim(-6, 6)
ax2.set_title('Live Statistics (current window)')
ax2.axhline(0, color='black', linewidth=0.5)

def update(frame):
    # The window slides forward each frame
    start = frame
    end = frame + window_size
    window = arr[start:end]

    x = np.arange(window_size)

    # Running mean and std *within* the window up to each point
    running_mean = [np.mean(window[:i+1]) for i in range(len(window))]
    running_std  = [np.std(window[:i+1])  for i in range(len(window))]
    running_std  = np.array(running_std)
    running_mean = np.array(running_mean)

    line_raw.set_data(x, window)
    line_avg.set_data(x, running_mean)
    line_std_hi.set_data(x, running_mean + running_std)
    line_std_lo.set_data(x, running_mean - running_std)

    # Update stats bars
    w_mean = np.mean(window)
    w_std  = np.std(window)
    w_min  = np.min(window)
    w_max  = np.max(window)
    for bar, val in zip(bars, [w_mean, w_std, w_min, w_max]):
        bar.set_height(val)

    ax1.set_title(f'Random Walk — Window [{start} : {end}]')
    return line_raw, line_avg, line_std_hi, line_std_lo, *bars

# frames = how many positions the window can start at
ani = animation.FuncAnimation(
    fig, update,
    frames=len(arr) - window_size,
    interval=50,       # milliseconds between frames
    blit=True
)

plt.show()


