import pandas as pd
import matplotlib.pyplot as plt

output2 = pd.read_csv('D:/DataSciTest/answers/YearlyAverages.out', sep='\t')
# Find the highest annual average maximum/minmum temperature and highest total annual precipitation for each weather station
highmax = pd.DataFrame({'high_max':output2.groupby(['file_name'])['maximum'].max()}).reset_index()
highmin = pd.DataFrame({'high_min':output2.groupby(['file_name'])['minimum'].max()}).reset_index()
highprec = pd.DataFrame({'high_prec':output2.groupby(['file_name'])['precipitation'].max()}).reset_index()

# Count the number of weather stations meet the requirement per year
output2 = output2.join(highmax.set_index('file_name'), on = 'file_name')
output2 = output2.join(highmin.set_index('file_name'), on = 'file_name')
output2 = output2.join(highprec.set_index('file_name'), on = 'file_name')
output2['ishighmax'] = (output2['maximum'] == output2['high_max'])
output2['ishighmin'] = (output2['minimum'] == output2['high_min'])
output2['ishighprec'] = (output2['precipitation'] == output2['high_prec'])

cnt_highmax = output2.groupby(['year'])['ishighmax'].sum()
cnt_highmin = output2.groupby(['year'])['ishighmin'].sum()
cnt_highprec = output2.groupby(['year'])['ishighprec'].sum()

val = pd.concat([cnt_highmax, cnt_highmin, cnt_highprec], axis=1, join='outer').fillna(-9999)
val.reset_index(inplace=True)
output = val.sort_values(by=['year'])
output.to_csv('D:/DataSciTest/answers/YearHistogram.out', header=True, index=None, sep='\t')

val.plot.bar(x = 'year', rot = 0)
plt.xticks(rotation=90)
plt.xlabel('year',fontdict={'weight': 'bold'})
plt.ylabel('Frequency', fontdict={'weight': 'bold'})
plt.savefig('DataSciTest/answers/YearHistogram.png')