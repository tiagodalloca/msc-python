import glob
import pandas as pd
from scipy import stats

all_files = glob.glob("../data/microdata-enem-2016/part-*")
frame = pd.concat((pd.read_csv(f, header=-1)
                   for f in all_files))

with open('../data/microdata-enem-2016/labels', 'r') as f:
    labels = f.readline().split(',')

frame.columns = labels

matrix = frame.as_matrix()

rs = [0] * 45

for i in range(45):
    rs[i] = (
        i,
        stats.pearsonr(matrix[i], matrix[48])[0],
    )

rs.sort(key=lambda x: x[1])

for i in range(45):
    print((labels[rs[i][0]] + ": {}").format(rs[i][1]))
