import pandas as pd

#read csv

df = pd.read_csv('Resources/cities.csv')

#save to file

df.to_html('./data.html', index=False)

#stringify

table = df.to_html()
print(table)