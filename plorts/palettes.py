import matplotlib

def gradient_to_colormap(name, gradient):
    gradient = [(pos,matplotlib.colors.to_rgb(name)) for pos,name in gradient]
    cmap = {"red":[], "green":[], "blue":[]}
    for pos,(r,g,b) in gradient:
        cmap["red"].append((pos,r,r))
        cmap["green"].append((pos,g,g))
        cmap["blue"].append((pos,b,b))
    return matplotlib.colors.LinearSegmentedColormap(name, cmap)


colorblind = ["#0072B2", "#009E73", "#D55E00",
              "#CC79A7", "#F0E442", "#56B4E9"]

solarized = ["#6c71c4", "#268bd2", "#2aa198", "#859900",
             "#b58900", "#cb4b16", "#dc322f", "#d33682"]

cool = gradient_to_colormap("cool",[(0, "white"), (0.25, "#DCEDC8"), (0.45, "#42B3D5"), (0.75, "#1a237e"), (1, "black")])

warm = gradient_to_colormap("warm", [(0, "white"), (0.3, "#feeb65"), (0.65, "#e4521b"), (0.85, "#4d342f"), (1, "black")])

neon = gradient_to_colormap("neon", [(0, "white"), (0.2, "#ffecb3"), (0.45, "#e85285"), (0.65, "#6a1b9a"), (1, "black")])
