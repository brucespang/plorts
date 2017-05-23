import os
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import palettes

def colors_from_hue(data, hue, cmap):
    num_colors = len(set(data[hue]))
    cm_subsection = np.linspace(0.2, 0.8, num_colors+2)
    cm_subsection = cm_subsection[1:num_colors+1]
    return [ cmap(v) for v in cm_subsection ]


def plot(data, x, y, hue=None, markers=[None], linestyles=['-'], cmap=palettes.neon):
    data = data.sort_values(x, ascending=True)
    if hue:
        if cmap is not None:
            colors = colors_from_hue(data, hue, cmap)

        for i,(key,grp) in enumerate(data.groupby(hue)):
            marker = markers[i % len(markers)]
            linestyle = linestyles[i % len(linestyles)]
            if cmap is not None:
                color = colors[i]
            else:
                color = None
            plt.plot(grp[x], grp[y], label=key, marker=marker, linestyle=linestyle, color=color)
    else:
        plt.plot(data[x], data[y])

    plt.ylabel(y)
    plt.xlabel(x)
    plt.gca().autoscale(tight=True)
    plt.gca().margins(y=0.1)

def stackplot(data, x, y, hue, cmap=palettes.neon):
    xs = data[x]
    yss = []
    labels = []
    for k,grp in data.groupby(hue):
        labels.append(k)
        ys = []
        for v in xs:
            matching = grp[grp[x] == v]
            if len(matching) > 0:
                ys.extend(matching[y])
            else:
                ys.append(None)
        yss.append(ys)

    if cmap is not None:
        colors = colors_from_hue(data, hue, cmap)
    else:
        colors = None

    plt.stackplot(xs, yss, labels=labels, colors=colors)

    plt.ylabel(y)
    plt.xlabel(x)
    plt.gca().autoscale(tight=True)
    plt.gca().margins(y=0.1)

def scatter(data, x, y, hue=None, markers=[None], cmap=palettes.neon):
    return plot(data=data,x=x,y=y, hue=hue,markers=['o'], linestyles=[''],cmap=cmap)

def savefig(filename):
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    plt.savefig(filename, tight_layout=True)
