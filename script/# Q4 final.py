# Q4 final
import pandas as pd
import numpy as np

output2 = pd.read_csv('D:/DataSciTest/answers/YearlyAverages.out', sep='\t')
df = pd.read_csv('D:/DataSciTest/yld_data/US_corn_grain_yield.txt', sep='\t', names=['year', 'yield'])
output2 = output2.replace('-9999', np.nan)

df_cd = pd.merge(output2, df, how='left', on = 'year')
corr = df_cd[['yield','maximum', 'minimum', 'precipitation','file_name']].groupby(['file_name']).corr(method = 'pearson')
corr = corr.round(2)
corr.reset_index(inplace=True)

rst = corr.loc[corr['level_1'] == 'yield']
output = rst[['file_name', 'maximum', 'minimum', 'precipitation']]
output.sort_values(by=['file_name'])
output.to_csv('D:/DataSciTest/answers/Correlations.out', header=True, index=None, sep='\t')