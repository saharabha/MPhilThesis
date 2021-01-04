import pandas as pd
import matplotlib.pyplot as plt
from pymol import cmd

def normalize(col):
    # col = pd.Series
    col -= col.min()
    col /= col.max()
    return col

def make_colors(csv):
    df = pd.read_csv(csv)
    scores = normalize(df['score'])
    colors = plt.cm.coolwarm(scores)[:,:-1]
    return {i:j for i, j in zip(df['res'], colors)}
    



def heatmap(scores):
    colors = make_colors(scores)
    df = pd.read_csv(scores)
    nscores = normalize(df['score'])
    for i, j in zip(colors.keys(), nscores):
        cmd.set_color(f'c{i}', colors[i].tolist())
        cmd.show('sticks', f'(sidechain, resi {i})')
        cmd.color(f'c{i}', f'resi {i}')


cmd.extend('heatmap', heatmap)
