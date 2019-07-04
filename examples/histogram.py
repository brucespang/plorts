import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plorts
import seaborn as sns
plt.style.use(['plorts', 'plorts-web'])

xmax = 2*np.pi
f = lambda x,offset: (offset+1)*np.sin(x-offset)
xs = np.arange(0,xmax,0.1)
offsets = range(0,len(plorts.palettes.solarized))
offsets = [4,5,6,7]
df = pd.DataFrame([[x, f(x, offset), i, np.abs(f(x, offset))] for x in xs for i,offset in enumerate(offsets)], columns=["x", "y", "offset", "abs"])

plt.figure()
plorts.hist(data=df[np.logical_or(df.offset == 3, df.offset == 0)],
            x="y", hue="offset",
           bins=np.arange(-10,10,1))
plt.ylabel("Y label")
plt.xlabel("X label")
plt.legend(loc='best')
plt.title("Histogram Example")
plt.axis(xmin=-8,xmax=8)
plorts.style_axis()
