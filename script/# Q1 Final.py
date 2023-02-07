# Q1 Final
import pandas as pd
import os
rootdir = 'D:/DataSciTest/wx_data/'
output = pd.DataFrame([])
for dirPath, dirNames, files in os.walk(rootdir):   
    for file in files:
        fpath = os.path.join(dirPath, file)
        df = pd.read_csv(fpath, sep='\t', names=["date", "maximum", "minimum", "precipitation"])
        nan_count = ((df["precipitation"] == -9999) & (df["maximum"] != -9999) & (df["minimum"] != -9999)).sum()
        data = [[file, nan_count]]
        df_row = pd.DataFrame(data, columns=['file_name', 'days_of_missing'])
        output = output.append(df_row)
output.sort_values(by=['file_name'])
output.to_csv('D:/DataSciTest/answers/MissingPrcpData.out', header=True, index=None, sep='\t')