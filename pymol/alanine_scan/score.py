import pandas as pd
import numpy as np

def scorefn(df):
    c2 = df['c2 distance']
    aff = df['affinity']
    aff = np.exp(aff.abs())
    score =  aff/c2
    return score / 10**3

def main():
    data = pd.read_csv('vina-info.csv', index_col=0)
    data['resn'] = pd.Series(\
[int(i[1])  if len(i) == 2 else 'DM'  for i in data['name'].str.findall('\d+') ])
    dmscore = scorefn(data.loc[data['resn'] == 'DM', :]).mean()

    results = []
    for i in data['resn'].unique():
        mutant = data.loc[data['resn'] == i, :]
        score = scorefn(mutant).mean() - dmscore
        results.append([i, score])
    pd.DataFrame(results, columns = ['res', 'score']).to_csv('relative-scores.csv')



if __name__ == '__main__':
    main()
