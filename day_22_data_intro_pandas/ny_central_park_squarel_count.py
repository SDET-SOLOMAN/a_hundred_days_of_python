import pandas

ny_data = pandas.read_csv('2018_ny.csv')
fur_color = ny_data["Primary Fur Color"]
gray = len(fur_color[fur_color == 'Gray'].to_list())
black = len(fur_color[fur_color == 'Black'].to_list())
Cinnamon = len(fur_color[fur_color == 'Cinnamon'].to_list())

filtered_data = {
    'colors': ['gray', 'black', 'red'],
    'num_of_animals': [gray, black, Cinnamon]
}

filtered_d = pandas.DataFrame(filtered_data)
print(filtered_d)
filtered_d.to_csv('filtered_fur_list.csv')