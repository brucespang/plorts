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
sns.boxplot(data=df, x="offset", y="y")
plt.ylabel("Y label")
plt.xlabel("X label")
plt.title("Boxplot Example")
plorts.style_axis()
plt.show()
