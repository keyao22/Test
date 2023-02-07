# Q2 Final
import pandas as pd
import os
# I didn't delete the entire row if there is any missing data in at least one colunm. 
# I used -9999 to replace missing data. 
rootdir = 'D:/DataSciTest/wx_data/'
output = pd.DataFrame([])
for dirPath, dirNames, files in os.walk(rootdir):
    for file in files:
        fpath = os.path.join(dirPath, file)
        df = pd.read_csv(fpath, sep='\t', names=["date", "maximum", "minimum", "precipitation"])

        df['date'] = pd.to_datetime(df['date'], format='%Y%m%d')
        df['year'] = df['date'].dt.year

        avg_max_temp = (df[(df['maximum'] != -9999)]).groupby(['year'])['maximum'].mean()/10 
        avg_min_temp = (df[(df['minimum'] != -9999)]).groupby(['year'])['minimum'].mean()/10
        aggr_prep = (df[(df['precipitation'] != -9999)]).groupby(['year'])['precipitation'].sum()/100
    
        avg_max_temp = avg_max_temp.round(2)
        avg_min_temp = avg_min_temp.round(2)
        aggr_prep = aggr_prep.round(2)
        val = pd.concat([avg_max_temp,avg_min_temp, aggr_prep], axis=1, join='outer').fillna(-9999)
        val.reset_index(inplace=True)
        data = val.assign(file_name = file)
        data = data[['file_name','year', 'maximum','minimum','precipitation']]
        df_row = pd.DataFrame(data)
        output = output.append(df_row)
output.sort_values(by=['file_name'])
output.to_csv('D:/DataSciTest/answers/YearlyAverages.out', header=True, index=None, sep='\t')