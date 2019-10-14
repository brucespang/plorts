import os
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from . import palettes
import errno

def colors_from_hue(data, hue, cmap):
    num_colors = len(data.groupby(hue))
    cm_subsection = np.linspace(0.2, 0.8, num_colors+2)
    cm_subsection = cm_subsection[1:num_colors+1]
    return [ cmap(v) for v in cm_subsection ]


# XXX: this method is a disaster
def plot(data, x, y, error=None, hue=None, markers=[None], linestyles=['-'], cmap=palettes.neon, label_lines=True, **kwargs):
    data = data.sort_values(x, ascending=True)

    if hue:
        if cmap is not None:
            colors = colors_from_hue(data, hue, cmap)

        for i,(key,grp) in enumerate(data.groupby(hue)):
            if label_lines:
                label = key
            else:
                label = ""
            marker = markers[i % len(markers)]
            linestyle = linestyles[i % len(linestyles)]
            if cmap is not None:
                color = colors[i]
            else:
                color = None
            if error is not None:
                plt.errorbar(list(grp[x]), list(grp[y]), yerr=grp[error], color=color, marker=marker, linestyle=linestyle, label=label, **kwargs)
            else:
                plt.plot(list(grp[x]), list(grp[y]), label=label, color=color, marker=marker, linestyle=linestyle, **kwargs)
    else:
        color = cmap(0.5)
        if error is not None:
            plt.errorbar(list(data[x]), list(data[y]), yerr=data[error], color=color, marker=markers[0], linestyle=linestyles[0], **kwargs)
        else:
            plt.plot(list(data[x]), list(data[y]), color=color, marker=markers[0], linestyle=linestyles[0], **kwargs)

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

def scatter(data, x, y, hue=None, cmap=palettes.neon, markers=['o'], **kwargs):
    return plot(data=data,x=x,y=y, hue=hue,markers=markers, linestyles=[''],cmap=cmap, **kwargs)

def hist(data, x, hue=None, cmap=palettes.neon, **kwargs):
    """
    Plot a histogram from a dataframe column.

    If hue is provided, plot many overlayed histograms, one per value of the data[hue] column.

    Parameters
    ----------

      data: pandas.DataFrame
        dataframe to plot

      x: string
        column of data to plot

    Keyword Arguments
    -----------------

      hue: string
        column of dataframe to split on

      cmap
        colormap to use

      alpha: float
        opacity of histogram
    """
    if 'rwidth' not in kwargs:
        kwargs['rwidth'] = 0.92

    if hue:
        colors = colors_from_hue(data, hue, cmap)
        
        if 'alpha' not in kwargs:
            kwargs['alpha'] = 0.5

        for i,(k,grp) in enumerate(data.groupby(hue)):
            if cmap:
                color = colors[i]
            else:
                color = None
     
            plt.hist(grp[x], label=k, color=color, **kwargs)
    else:
        if 'color' not in kwargs:
            kwargs['color'] = cmap(0.5)

        plt.hist(data[x], **kwargs)

def cdf(data, *args, **kwargs):
    sorted_data = np.sort(data)
    sorted_data_cdf = np.arange(len(sorted_data))/float(len(sorted_data)) * 100 
    plt.plot(sorted_data, sorted_data_cdf, *args, **kwargs)
    
def savefig(filename, **kwargs):
    """Saves a figure, but also creates the directory and calls tight_layout before saving"""
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    if 'bbox_inches' not in kwargs:
        kwargs['bbox_inches'] = 'tight'
    if 'pad_inches' not in kwargs:
        kwargs['pad_inches'] = 0
            
    plt.tight_layout(pad=0)
    plt.savefig(filename, **kwargs)
