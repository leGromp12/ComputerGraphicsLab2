import matplotlib.pyplot as plt
import numpy as np

def draw_star(ax, x, y, size, level, angle=0):
    if level == 0:
        return

    points = []
    for i in range(5):
        a = angle + i * 72
        x1 = x + np.cos(np.radians(a)) * size
        y1 = y + np.sin(np.radians(a)) * size
        points.append((x1, y1))

    for i in range(5):
        x_start, y_start = points[i]
        x_end, y_end = points[(i + 2) % 5]
        ax.plot([x_start, x_end], [y_start, y_end], color='cyan')

    for px, py in points:
        draw_star(ax, px, py, size * 0.36, level - 1, angle)




depth = int(input("Введіть глибину: "))

fig, ax = plt.subplots()
fig.set_facecolor('black')
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.axis('off')

draw_star(ax, 0, 0, 1, depth)

plt.show()



