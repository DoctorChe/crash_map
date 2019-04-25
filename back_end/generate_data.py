# encoding: utf-8

import consts
import csv
import json

with open('../data/input_verified.csv', encoding='utf-8', mode='r') as input, open('../data/data.js', encoding='utf-8',
                                                                                   mode='w') as output:
    # open csv files
    csv_input = csv.reader(input, delimiter=',')

    json_output = []

    for row in csv_input:
        row_typed = [row[consts.DATE],
                     row[consts.TIME],
                     row[consts.TYPE],
                     row[consts.LOCATION].replace(consts.MARI_EL + ', ', ''),
                     row[consts.STREET],
                     row[consts.HOUSE_NUMBER],
                     row[consts.ROAD]]
        try:
            row_typed.append(int(row[consts.KILOMETER]))
        except:
            row_typed.append(0)
        try:
            row_typed.append(int(row[consts.METER]))
        except:
            row_typed.append(0)
        try:
            row_typed.append(float(row[consts.LONGITUDE]))
        except:
            row_typed.append(0)
        try:
            row_typed.append(float(row[consts.LATITUDE]))
        except:
            row_typed.append(0)
        # print(row)
        # print(consts.LONGITUDE_GEOCODE)
        # print(row[consts.LONGITUDE_GEOCODE])
        # print(row[0])
        row_typed.append(int(row[consts.DEATH]))
        row_typed.append(int(row[consts.DEATH_CHILDREN]))
        row_typed.append(int(row[consts.INJURY]))
        row_typed.append(int(row[consts.INJURY_CHILDREN]))
        row_typed.append(float(row[consts.LONGITUDE_GEOCODE]))
        row_typed.append(float(row[consts.LATITUDE_GEOCODE]))
        row_typed.append(int(row[consts.VALID]))
        row_typed.append(int(row[consts.VALID_STRICT]))
        json_output.append(row_typed)

    output.write('var data=')
    output.write(json.dumps(json_output, ensure_ascii=False))
    output.write(';')
