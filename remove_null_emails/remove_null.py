import pandas as pd

data = pd.read_csv('organizations.csv') #read csv file as table
data = data.dropna() #drops any row that is missing a value
data.to_csv('emails.csv', index = False) 
