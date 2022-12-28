
import pandas as pd

# data = pd.read_csv('weather_data.csv')
# d = data['temp']
# # print(d.max())
# print(data[data['day'] == 'Friday'])
# print([data['temp'].max()])
# print(data[data['temp'] == data['temp'].max()])

data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
# print(data[data['Primary Fur Color'] == 'Gray'])
grey = data['Primary Fur Color'][data['Primary Fur Color'] == 'Gray'].count()
red = data['Primary Fur Color'][data['Primary Fur Color'] == 'Cinnamon'].count()
black = data['Primary Fur Color'][data['Primary Fur Color'] == 'Black'].count()


csv_dict = {'fur color': ['Gray', 'Red', 'Black'], 'colors': [grey,red,black]}

# csv_dict = {'Grey': [grey], 'Red': [red], 'Black': [black]}
print(csv_dict)

df = pd.DataFrame.from_dict(csv_dict)
df.to_csv("data.csv")


