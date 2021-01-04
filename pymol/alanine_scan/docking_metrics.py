import sys
import os
import re
import numpy as np
import pandas as pd
import enz

from tqdm import tqdm

def get_info(receptor, poses, scores):
    # enz.protein & list of enz.mols
    fe = receptor.df.loc[receptor.df['element_symbol'] == 'FE', ['x_coord','y_coord','z_coord']].values
    c2s = [i.df.loc[i.df['atom_number'] == 2,['x_coord','y_coord','z_coord']].values for i in poses]
    distances = [np.linalg.norm(fe - i) for i in c2s]
    pose_names = [int(re.findall('\d+', os.path.basename(i.struc))[0]) for i in poses]
    affinities = dict(zip(scores['mode'], scores['affinity (kcal/mol)']))
    df = pd.DataFrame({i:{'c2 distance':j, 'affinity':affinities[k],} for i,j,k in zip(pose_names,distances,affinities)}).T
    rmsd_ub = pd.concat([scores.loc[scores['mode'] == i, 'dist from best mode - rmsd - ub'] for i in df.index])
    rmsd_ub.index = df.index
    rmsd_lb = pd.concat([scores.loc[scores['mode'] == i, 'dist from best mode - lb'] for i in df.index])
    rmsd_lb.index = df.index
    df = pd.concat([df, rmsd_ub, rmsd_lb], axis=1)
    x = df['affinity'].abs().apply(np.exp) * df['c2 distance'] / 1000
    return df # x.mean()

def main(args):
    l = []
    for i in tqdm(args):
        try:
            p = enz.protein(os.path.join(i, 'clean_receptor.pdb'), cofactors = ['HEM'])
            poses = [enz.mol(os.path.join(i, j)) for j in os.listdir(i) if 'vina' in j]
            scores = pd.read_csv(os.path.join(i, 'scores.csv'),index_col=0)
            scores['mode'] = scores['mode'].astype(int)

            x = get_info(p, poses, scores).reset_index()
            x['name'] = os.path.basename(i)
            l.append(x)
        except:
            print('error',i)
    df = pd.concat(l)
    df.reset_index(inplace=True,drop=True)
    df.to_csv('vina-info.csv')
    print(df)

if __name__ == '__main__':
    main(sys.argv[1:])
