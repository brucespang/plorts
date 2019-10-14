import matplotlib.pyplot as plt
from math import atan2,degrees
import numpy as np

def legend(*args, **kwargs):
    """
    plt.legend with a few extra location options:

    * inline: place legends on top of line
    * end: place legend at the right end of line
    * max: place legend slightly up and right of the max value of each line
    
    Parameters
    ----------

      loc: string or int
        location to place the legend
    """
    if 'loc' in kwargs:
        if kwargs['loc'] == 'inline':
            del kwargs['loc']
            legend_inline(*args, **kwargs)
        elif kwargs['loc'] == 'end':
            del kwargs['loc']
            legend_end(*args, **kwargs)
        elif kwargs['loc'] == 'max':
            del kwargs['loc']
            legend_max(*args, **kwargs)
        else:
            plt.legend(*args, **kwargs)
    else:
        plt.legend(*args, **kwargs)

def legend_end(xoff=0.05, yoff=0, *args, **kwargs):
    lines = plt.gca().get_lines()

    for line in lines:
        label = line.get_label()
        #Take only the lines which have labels other than the default ones
        if "_line" in label:
            continue
        x = line.get_xdata()[-1] + xoff
        y = line.get_ydata()[-1] + yoff
        ax = line.axes
        ax.text(x,y,label,
                color=line.get_color(),
                bbox=dict(facecolor=ax.get_facecolor(),
                          edgecolor=ax.get_facecolor(),
                          x=x, y=y,
                          pad=2),
                **kwargs)

def legend_max(xoff=0.05, yoff=0.01, *args, **kwargs):
    lines = plt.gca().get_lines()

    for line in lines:
        label = line.get_label()
        #Take only the lines which have labels other than the default ones
        if "_line" in label:
            continue

        max_idx = np.argmax(line.get_ydata())
        x = line.get_xdata()[max_idx] + xoff
        y = line.get_ydata()[max_idx] + yoff
        
        ax = line.axes
        ax.text(x,y,label,
                color=line.get_color(),
                **kwargs)
        
def legend_inline(xvals=None,xoffset=None,**kwargs):
    lines = plt.gca().get_lines()

    ax = lines[0].axes
    labLines = []
    labels = []

    #Take only the lines which have labels other than the default ones
    for line in lines:
        label = line.get_label()
        if "_line" not in label:
            labLines.append(line)
            labels.append(label)

    if xvals is None:
        xmin,xmax = ax.get_xlim()
        xvals = np.linspace(xmin,xmax,len(labLines)+2)[1:-1]

        if xoffset is not None:
            xvals += xoffset

    for line,x,label in zip(labLines,xvals,labels):
        label_line(line,x,label,**kwargs)

#Label line with line2D label data
def label_line(line,x,label=None,**kwargs):
    ax = line.axes
    xdata = line.get_xdata()
    ydata = line.get_ydata()

    #if (x < xdata[0]) or (x > xdata[-1]):
    #    print('x label location is outside data range!')
    #    return

    #Find corresponding y co-ordinate and angle of the
    ip = 1
    for i in range(len(xdata)):
        if x < xdata[i]:
            ip = i
            break

    y = ydata[ip-1] + (ydata[ip]-ydata[ip-1])*(x-xdata[ip-1])/(xdata[ip]-xdata[ip-1])

    if not label:
        label = line.get_label()

    trans_angle = 0

    #Set a bunch of keyword arguments
    if 'color' not in kwargs:
        kwargs['color'] = line.get_color()

    if ('horizontalalignment' not in kwargs) and ('ha' not in kwargs):
        kwargs['ha'] = 'center'

    if ('verticalalignment' not in kwargs) and ('va' not in kwargs):
        kwargs['va'] = 'center'

    if 'clip_on' not in kwargs:
        kwargs['clip_on'] = True

    if 'zorder' not in kwargs:
        kwargs['zorder'] = 2.5

    ax.text(x,y,label,rotation=trans_angle,
            bbox=dict(facecolor=ax.get_facecolor(),
                      edgecolor=ax.get_facecolor(),
                      pad=2),
            **kwargs)
