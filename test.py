import plorts
import matplotlib
import matplotlib.pyplot as plt

plt.style.use(["plorts", "plorts-web"])

# plot some stuff
plt.plot([0,2,3], [1,2,10], label="1")
plt.plot([0,2,3], [3,2,1], label="2")
plt.plot([0,2,3], [2,2,2], label="3")
plt.title("test")
plorts.legend(loc='end')
plt.axis(xmin=0, ymin=0)
plt.xlabel("x")
plt.ylabel("y")

# creates the directories and everything!
plorts.savefig('output/test.png')

plt.show()
