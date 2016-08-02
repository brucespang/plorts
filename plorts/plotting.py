import os
import matplotlib.pyplot as plt

def plot(data, x, y, hue=None, markers=[None], linestyles=['-']):
    data = data.sort_values(x, ascending=True)
    if hue:
        for i,(key,grp) in enumerate(data.groupby(hue)):
            marker = markers[i % len(markers)]
            linestyle = linestyles[i % len(linestyles)]
            plt.plot(grp[x], grp[y], label=key, marker=marker, linestyle=linestyle)
    else:
        plt.plot(data[x], data[y])

    plt.ylabel(y)
    plt.xlabel(x)

def savefig(filename):
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    plt.savefig(filename, tight_layout=True)
