import os
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import palettes

def colors_from_hue(data, hue, cmap):
    num_colors = len(data.groupby(hue))
    cm_subsection = np.linspace(0.2, 0.8, num_colors+2)
    cm_subsection = cm_subsection[1:num_colors+1]
    return [ cmap(v) for v in cm_subsection ]


def plot(data, x, y, error=None, hue=None, markers=[None], linestyles=['-'], cmap=palettes.neon):
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
            if error is not None:
                plt.errorbar(grp[x], grp[y], yerr=grp[error], label=key, marker=marker, linestyle=linestyle, color=color)
            else:
                plt.plot(grp[x], grp[y], label=key, marker=marker, linestyle=linestyle, color=color)
    else:
        color = cmap(0.5)
        if error is not None:
            plt.errorbar(data[x], data[y], yerr=data[error], color=color)
        else:
            plt.plot(data[x], data[y], color=color)

    plt.ylabel(y)
    plt.xlabel(x)
    plt.gca().autoscale(tight=True)
    plt.gca().margins(y=0.1)

def stackplot(data, x, y, hue, cmap=palettes.neon):
    xs = np.array(data[x])
    yss = []
    labels = []
    for k,grp in data.groupby(hue):
        labels.append(k)
        grp_xs = grp[x].tolist()
        grp_ys = grp[y].tolist()
        ys = []
        for v in xs:
            if len(grp_xs) > 0 and grp_xs[0] == v:
                ys.append(grp_ys.pop(0))
                grp_xs.pop(0)
            else:
                if len(ys) == 0:
                    ys.append(0.)
                else:
                    ys.append(ys[-1])
        assert len(grp_xs) == 0
        assert len(grp_ys) == 0
        assert len(ys) == len(xs)
        yss.append(np.array(ys, dtype=float))

    if cmap is not None:
        colors = colors_from_hue(data, hue, cmap)
    else:
        colors = None

    plt.stackplot(xs, *yss, labels=labels, colors=colors)

    plt.ylabel(y)
    plt.xlabel(x)
    plt.gca().autoscale(tight=True)
    plt.gca().margins(y=0.1)

def scatter(data, x, y, hue=None, cmap=palettes.neon):
    return plot(data=data,x=x,y=y, hue=hue,markers=['o'], linestyles=[''],cmap=cmap)

def hist(x, cmap=palettes.neon, **kwargs):
    if 'color' not in kwargs:
        kwargs['color'] = cmap(0.5)
    if 'rwidth' not in kwargs:
        kwargs['rwidth'] = 0.92
    plt.hist(x, **kwargs)

def savefig(filename, **kwargs):
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    plt.tight_layout(pad=0)
    plt.savefig(filename, **kwargs)
