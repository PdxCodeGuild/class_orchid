import csv
import json


def make_json():
    data = {}
    with open('./airports.csv') as f:
        reader = csv.DictReader(f)
        for rows in reader:
            key = rows['airport']
            data[key] = rows

    with open('./airports.json', 'w') as jf:
        jf.write(json.dumps(data, indent=4))


make_json()
