import json


def get_biggest_bar(json_file='bars.json'):
    with open(json_file, 'r') as f:
        bars = json.load(f)
    biggest_bar = max(bars['features'], key=lambda bar: bar['properties']['Attributes']['SeatsCount'])
    return biggest_bar['properties']['Attributes']['Name']


def get_smallest_bar(json_file='bars.json'):
    with open(json_file, 'r') as f:
        bars = json.load(f)
    smallest_bar = min(bars['features'], key=lambda bar: bar['properties']['Attributes']['SeatsCount'])
    return smallest_bar['properties']['Attributes']['Name']


def get_nearest_bar(longitude, latitude, json_file='bars.json'):
    with open(json_file, 'r') as f:
        bars = json.load(f)
    nearest_bar = min(bars['features'], key=lambda bar: (abs(bar['geometry']['coordinates'][0]-longitude),
                                                         abs(bar['geometry']['coordinates'][1]-latitude)))
    return nearest_bar['properties']['Attributes']['Name']


def main():
    try:
        longitude = float(input('Введите долготу: '))
        latitude = float(input('Введите широту: '))
    except ValueError:
        print('Координаты состоят только из чисел')
        exit()
    print(f'Самый большой бар: {get_biggest_bar()}')
    print(f'Самый маленький бар: {get_smallest_bar()}')
    print(f'Ближайший бар: {get_nearest_bar(longitude, latitude)}')


if __name__ == "__main__":
    main()
