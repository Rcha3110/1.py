import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(3, 2, 1)
plt.title("Graph 1")
plt.xlabel("Time")
plt.ylabel("Pressure")
plt.plot(x,y)
#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(3, 2, 2)
plt.title("Graph 2")
plt.plot(x,y)

#plot 3:
x = np.array([0, 1, 2, 3,4])
y = np.array([10, 20, 30, 40, 55])

plt.subplot(3, 2, 3)
plt.title("Graph 3")
plt.plot(x,y)

#plot 4:
x = np.array([0, 1, 2, 3,4,5])
y = np.array([10, 20, 30, 40, 55,20])

plt.subplot(3, 2, 4)
plt.title("Graph 4")
plt.plot(x,y)

#plot 4:
x = np.array([0, 1, 2, 3,4,5,8])
y = np.array([10, 20, 30, 40, 55,20,45])

plt.subplot(3, 2, 5)
plt.title("Graph 4")
plt.plot(x,y)

plt.suptitle("Graph analysis")
plt.show()
