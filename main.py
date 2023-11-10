import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse, Arc
import matplotlib.animation as animation

fig = plt.figure()
ax = fig.add_subplot(xlim=(-2, 2), ylim=(-2, 2))
ax.grid()
ax.set_aspect("equal")

# draw a head
head = plt.Circle((0, 0.3), 0.3, color="tomato")
ax.add_patch(head)

# draw a body
body = Ellipse((0, -0.5), 0.7, 1)
ax.add_patch(body)

# draw eyes
eyes_1 = Ellipse((-0.13, 0.35), 0.15, 0.25, color="white")
eyes_1.set_edgecolor("blue")
ax.add_patch(eyes_1)
eyes_2 = Ellipse((0.13, 0.35), 0.15, 0.25, color="white")
eyes_2.set_edgecolor("blue")
ax.add_patch(eyes_2)
eyes_3 = Ellipse((-0.13, 0.35), 0.07, 0.15, color="black")
ax.add_patch(eyes_3)
eyes_4 = Ellipse((0.13, 0.35), 0.07, 0.15, color="black")
ax.add_patch(eyes_4)

# draw nose
nose = plt.Circle((0.01, 0.17), 0.05, color="red")
ax.add_patch(nose)

# draw shoeas
shoes1 = Ellipse((-0.52, -1.95), 0.25, 0.1, color="black", fill=False)
ax.add_patch(shoes1)
shoes2 = Ellipse((0.52, -1.95), 0.25, 0.1, color="black", fill=False)
ax.add_patch(shoes2)
left_leg = plt.Line2D((-0.12, -0.45), (-0.98, -1.9))
ax.add_line(left_leg)
righ_leg = plt.Line2D((0.12, 0.45), (-0.98, -1.9))
ax.add_line(righ_leg)

# draw a mouth
mouth = Arc((0, 0.08), 0.15, 0.1, angle=180, theta1=0.0, theta2=180.0)
ax.add_patch(mouth)

static_frames = 100
num_samples = 100
x_right = np.empty(0)
y_right = np.empty(0)
x_left = np.empty(0)
y_left = np.empty(0)
z = []
alignment = []
shift = 0.1
x = np.concatenate(
    [np.linspace(shift, 1, num_samples), np.ones(static_frames)])
alignment.extend([0.3 for _ in range(num_samples + static_frames)])

# y=x
y = x - shift
x_right = np.concatenate([x_right, x])
y_right = np.concatenate([y_right, y])
x_left = np.concatenate([x_left, -x])
y_left = np.concatenate([y_left, -y])
z.extend(["x" for _ in range(num_samples + static_frames)])
alignment.extend([0.3 for _ in range(num_samples + static_frames)])

# y = -x
y = -x + shift
x_right = np.concatenate([x_right, x])
y_right = np.concatenate([y_right, y])
x_left = np.concatenate([x_left, -x])
y_left = np.concatenate([y_left, -y])
z.extend(["-x" for _ in range(num_samples + static_frames)])
alignment.extend([0.27 for _ in range(num_samples + static_frames)])

# y=|x|
y = np.abs(x - shift)
x_right = np.concatenate([x_right, x])
y_right = np.concatenate([y_right, y])
x_left = np.concatenate([x_left, -x])
y_left = np.concatenate([y_left, y])
z.extend(["|x|" for _ in range(num_samples + static_frames)])
alignment.extend([0.26 for _ in range(num_samples + static_frames)])

# y=-|x|
y = -np.abs(x - shift)
x_right = np.concatenate([x_right, x])
y_right = np.concatenate([y_right, y])
x_left = np.concatenate([x_left, -x])
y_left = np.concatenate([y_left, y])
z.extend(["-|x|" for _ in range(num_samples + static_frames)])
alignment.extend([0.26 for _ in range(num_samples + static_frames)])

# y=x^2
y = (x - shift) ** 2
x_right = np.concatenate([x_right, x])
y_right = np.concatenate([y_right, y])
x_left = np.concatenate([x_left, -x])
y_left = np.concatenate([y_left, y])
z.extend([r"$x^2$" for _ in range(num_samples + static_frames)])
alignment.extend([0.26 for _ in range(num_samples + static_frames)])

# y=-x^2
y = -(x - shift) ** 2
x_right = np.concatenate([x_right, x])
y_right = np.concatenate([y_right, y])
x_left = np.concatenate([x_left, -x])
y_left = np.concatenate([y_left, y])
z.extend([r"$-x^2$" for _ in range(num_samples + static_frames)])
alignment.extend([0.21 for _ in range(num_samples + static_frames)])

# y=x^3
y = (x - shift) ** 3
x_right = np.concatenate([x_right, x])
y_right = np.concatenate([y_right, y])
x_left = np.concatenate([x_left, -x])
y_left = np.concatenate([y_left, -y])
z.extend([r"$x^3$" for _ in range(num_samples + static_frames)])
alignment.extend([0.26 for _ in range(num_samples + static_frames)])

# y=sin x
y = np.sin(3.05 * (x - shift)) / 3
x_right = np.concatenate([x_right, x])
y_right = np.concatenate([y_right, y])
x_left = np.concatenate([x_left, -x])
y_left = np.concatenate([y_left, -y])
z.extend(["sin x" for _ in range(num_samples + static_frames)])
alignment.extend([0.18 for _ in range(num_samples + static_frames)])

# y=cos x
y = np.cos(3.05 * (x - shift)) / 3 - 1 / 3
x_right = np.concatenate([x_right, x])
y_right = np.concatenate([y_right, y])
x_left = np.concatenate([x_left, -x])
y_left = np.concatenate([y_left, y])
z.extend(["cos x" for _ in range(num_samples + static_frames)])
alignment.extend([0.18 for _ in range(num_samples + static_frames)])

# y=tan x
y = np.tan(x - shift)
x_right = np.concatenate([x_right, x])
y_right = np.concatenate([y_right, y])
x_left = np.concatenate([x_left, -x])
y_left = np.concatenate([y_left, -y])
z.extend(["tan x" for _ in range(num_samples + static_frames)])
alignment.extend([0.18 for _ in range(num_samples + static_frames)])

# y=cot x
x_right = np.concatenate([x_right, x])
y_right = np.concatenate([y_right, -y])
x_left = np.concatenate([x_left, -x])
y_left = np.concatenate([y_left, y])
z.extend(["cot x" for _ in range(num_samples + static_frames)])
alignment.extend([0.18 for _ in range(num_samples + static_frames)])

# y=e^x
x_e = np.concatenate(
    [np.linspace(shift, 1.2, num_samples), np.ones(static_frames)])
y = np.power(np.e, x_e/2)-1-shift/2
x_right = np.concatenate([x_right, x_e])
y_right = np.concatenate([y_right, y])
x_left = np.concatenate([x_left, -x_e])
y_left = np.concatenate([y_left, np.power(np.e, -x_e/2)-1+shift/2])
z.extend([r"$e^x$" for _ in range(num_samples + static_frames)])
alignment.extend([0.26 for _ in range(num_samples + static_frames)])

# x^2+y^2=R^2
y_2 = np.concatenate([np.linspace(0, 1, num_samples), np.ones(static_frames)])
x_2 = np.sqrt(0.25-(y_2-0.5)**2)
x_right = np.concatenate([x_right, x_2])
y_right = np.concatenate([y_right, y_2])
x_left = np.concatenate([x_left, -x_2])
y_left = np.concatenate([y_left, y_2])
z.extend([r"$x^2+y^2=R^2$" for _ in range(num_samples + static_frames)])
alignment.extend([0.05 for _ in range(num_samples + static_frames)])

length = len(x_right)
line1, = ax.plot(np.empty(num_samples), np.empty(num_samples), 'r', lw=2)
line2, = ax.plot(np.empty(num_samples), np.empty(num_samples), 'r', lw=2)

display_text = ax.text(
    0.3, 0.85, '', transform=ax.transAxes, fontsize=40, color="m")
template = 'y= %s'


def animate(i):
    first_idx = i // (num_samples + static_frames) * \
        (num_samples + static_frames)
    line1.set_data(x_right[first_idx:i], y_right[first_idx:i])
    line2.set_data(x_left[first_idx:i], y_left[first_idx:i])
    if z[i] != r"$x^2+y^2=R^2$":
        display_text.set_text(template % z[i])
    else:
        display_text.set_text(z[i])
    display_text.set_x(alignment[i])
    return line1, line2, display_text


ani = animation.FuncAnimation(fig, animate, np.arange(length), interval=10,
                              blit=True, repeat=False)


mywriter = animation.FFMpegWriter(fps=60)
ani.save('output.mp4', writer=mywriter)
# plt.show()
