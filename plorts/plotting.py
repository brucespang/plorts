import os
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from . import palettes
import errno


def colors_from_hue(data, hue, cmap):
    # TODO: add a version of this that takes a number of arguments
    # Alternatively, figure out how to do the C0, C1, ... business
    if hue is None:
        return [cmap(0.5)]

    num_colors = len(data.groupby(hue))
    cm_subsection = np.linspace(0.2, 0.8, num_colors + 2)
    cm_subsection = cm_subsection[1 : num_colors + 1]
    return [cmap(v) for v in cm_subsection]


def hueize(data, hue=None, cmap=palettes.neon, *args, **kwargs):
    """
    Groups a dataframe by hues, if any, and generates plot settings for each hue.

    Returns
    -------
      Generator of (pd.DataFrame, kwargs), where the kwargs can be used in matplotlib functions.

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
    """
    if "colors" in kwargs:
        colors = kwargs["colors"]
        del kwargs["colors"]
    elif "color" in kwargs:
        colors = [kwargs.get("color")]
    else:
        colors = colors_from_hue(data, hue, cmap)

    if hue is None:
        hues = [(None, data)]
    else:
        hues = data.groupby(hue)

    for i, (label, grp) in enumerate(hues):
        new_kwargs = kwargs.copy()

        # matplotlib doesn't like it when we have these in its kwargs.
        new_kwargs.pop("markers", None)
        new_kwargs.pop("linestyles", None)

        if "markers" in kwargs:
            markers = kwargs["markers"]
            new_kwargs["marker"] = markers[i % len(markers)]

        if "linestyles" in kwargs:
            linestyles = kwargs["linestyles"]
            new_kwargs["linestyle"] = linestyles[i % len(linestyles)]

        if "labels" in kwargs:
            # XXX: TODO
            pass

        new_kwargs.update(
            {
                "label": label,
                "color": colors[i % len(colors)],
            }
        )

        yield (grp, new_kwargs)


def plot(data, x, y, error=None, *args, **kwargs):
    data = data.sort_values(x, ascending=True)

    for df, kwargs in hueize(data, *args, **kwargs):
        if error is not None:
            plt.errorbar(list(df[x]), list(df[y]), yerr=df[error], **kwargs)
        else:
            plt.plot(list(df[x]), list(df[y]), **kwargs)

    plt.ylabel(y)
    plt.xlabel(x)
    plt.gca().autoscale(tight=True)
    plt.gca().margins(y=0.1)


def interp_nans(x, y):
    is_nan = np.isnan(y)
    res = y * 1.0
    res[is_nan] = np.interp(x[is_nan], x[-is_nan], y[-is_nan])
    return res


def interp(df, x, y):
    df = df.sort_values(x)
    df[y] = interp_nans(df[x], df[y])
    return df[[x, y]]


def stackplot(data, x, y, hue, cmap=palettes.neon):
    combined_df = []
    for x_val in data[x]:
        for h_val in set(data[hue]):
            matches = data[(data[x] == x_val) & (data[hue] == h_val)]
            if len(matches) == 0:
                combined_df.append(pd.DataFrame([{x: x_val, y: None, hue: h_val}]))
            elif len(matches) == 1:
                combined_df.append(matches)
            else:
                print(matches)
    combined_df = pd.concat(combined_df)

    interpolated = (
        combined_df.groupby(hue).apply(lambda df: interp(df, x, y)).reset_index()
    )

    xs = np.array(interpolated[x])
    yss = []
    labels = []
    for k, grp in interpolated.groupby(hue):
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
                    ys.append(0.0)
                else:
                    ys.append(ys[-1])
        assert len(grp_xs) == 0
        assert len(grp_ys) == 0
        assert len(ys) == len(xs)
        yss.append(np.array(ys, dtype=float))

    if cmap is not None:
        colors = colors_from_hue(interpolated, hue, cmap)
    else:
        colors = None

    plt.stackplot(xs, *yss, labels=labels, colors=colors)

    plt.ylabel(y)
    plt.xlabel(x)
    plt.gca().autoscale(tight=True)
    plt.gca().margins(y=0.1)


def scatter(data, x, y, markers=["o"], linestyles=[""], **kwargs):
    return plot(data=data, x=x, y=y, markers=markers, linestyles=linestyles, **kwargs)


def hist(data, x, alpha=0.5, rwidth=0.92, *args, **kwargs):
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

      alpha: float
        opacity of histogram (default: 0.5)

      rwidth: float
        The relative width of the bars as a fraction of the bin width (default: 0.92)
    """
    new_kwargs = dict(alpha=alpha, rwidth=rwidth)
    new_kwargs.update(kwargs)
    for df, kwargs in hueize(data, *args, **new_kwargs):
        plt.hist(df[x], **kwargs)
    plt.xlabel(x)
    plt.ylabel("Frequency")


def cdf(data, x, *args, **kwargs):
    """
    Plot a cdf from a dataframe column.

    If hue is provided, plot many overlayed cdfs, one per value of the data[hue] column.

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
    """
    for df, kwargs in hueize(data, *args, **kwargs):
        sorted_data = np.sort(df[x])
        sorted_data_cdf = np.arange(len(sorted_data)) / float(len(sorted_data)) * 100
        plt.plot(sorted_data, sorted_data_cdf, *args, **kwargs)
    plt.ylabel("Cumulative % Data")
    plt.xlabel(x)


def pdf(data, x, bins=10, normalize=True, *args, **kwargs):
    """
    Plot a probability density function (pdf) from a dataframe column.

    If hue is provided, plot many overlayed pdf, one per value of the data[hue] column.

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

      bins: int or sequence of scalars or str, optional
        Bins to use for the function. See `numpy.histogram <https://numpy.org/doc/stable/reference/generated/numpy.histogram.html>`

      normalize: boolean
        Normalize to a probability density (default). If false, returns a histogram.
    """
    for df, kwargs in hueize(data, *args, **kwargs):
        ys, xs = np.histogram(df[x], bins=bins)
        if normalize:
            ys = np.array(ys) / sum(ys) * 100
        plt.plot(xs[:-1], ys, *args, **kwargs)
    plt.ylabel("% Data")
    plt.xlabel(x)


def savefig(filename, **kwargs):
    """Saves a figure, but also creates the directory and calls tight_layout before saving"""
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    if "bbox_inches" not in kwargs:
        kwargs["bbox_inches"] = "tight"
    if "pad_inches" not in kwargs:
        kwargs["pad_inches"] = 0

    plt.tight_layout(pad=0)
    plt.savefig(filename, **kwargs)
