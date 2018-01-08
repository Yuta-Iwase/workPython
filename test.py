import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0., 10., 0.1)
s = np.sin(x)
c = np.cos(x)

fig = plt.figure()

ax1 = fig.add_subplot(211)
ax1.plot(x, s)
ax1.set_ylim(-3, 3)

ax2 = fig.add_subplot(212)
ax2.plot(x, c)
ax2.set_ylim(-3, 3)

#plt.show()