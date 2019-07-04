import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plorts
plt.style.use(['plorts', 'plorts-web'])

xmax = 2*np.pi
f = lambda x,offset: (offset+1)*np.sin(x-offset)
xs = np.arange(0,xmax,0.1)
offsets = range(0,len(plorts.palettes.solarized))
offsets = [4,5,6,7]
df = pd.DataFrame([[x, f(x, offset), i, np.abs(f(x, offset))] for x in xs for i,offset in enumerate(offsets)], columns=["x", "y", "offset", "abs"])

plt.figure()
plt.title("Scatter Plot Example")
plorts.scatter(df, x="x", y="y", hue="offset")
plorts.legend(loc='end')
plt.ylabel("Y label")
plt.xlabel("X label")
plorts.style_axis()
plt.show()
