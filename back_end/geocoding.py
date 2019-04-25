# encoding: utf-8

import consts
import csv
import json
import urllib.parse
import urllib.request

# import quopri

GEOCODING_URL_BASE = 'https://geocode-maps.yandex.ru/1.x/?format=json&geocode='


def get_address(row):
    for old, new in consts.STREET_REPLACE_DICTIONARY.items():
        row[consts.STREET] = row[consts.STREET].replace(old, new)
        # print(f"{' '.join([row[consts.LOCATION], row[consts.STREET], row[consts.HOUSE_NUMBER]])}")
        # response = urllib.parse.quote(' '.join([row[consts.LOCATION], row[consts.STREET], row[consts.HOUSE_NUMBER]]))
        # # print(response)
        # q = response
        # q = bytes(q.replace('%', '='), 'UTF-8')
        # # print(q)
        # b = quopri.decodestring(q)
        # print(b.decode('UTF-8'))

    return urllib.parse.quote(' '.join([row[consts.LOCATION], row[consts.STREET], row[consts.HOUSE_NUMBER]]))


def make_request(input, url):
    with urllib.request.urlopen(url) as response:
        try:
            json_response = json.loads(response.read().decode('utf-8'))['response']['GeoObjectCollection'][
                'featureMember']
        except KeyError:
            return make_request(input, url)

        # print(json_response)

        for object in json_response:
            if object['GeoObject']['metaDataProperty']['GeocoderMetaData']['kind'] == consts.HOUSE_YANDEX:
                location = object['GeoObject']['Point']['pos'].split()
                row.extend([location[0], location[1]])
                break

        if len(row) < consts.LONGITUDE_GEOCODE + 1:
            row.extend([0, 0])


with open('../data/input.csv', encoding='utf-8', mode='r') as input, open('../data/input_geocoded.csv',
                                                                          encoding='utf-8', newline="\n",
                                                                          mode='w') as geocoding_output:
    # open csv files
    input = csv.reader(input, delimiter=',')
    output = csv.writer(geocoding_output, delimiter=',')

    for row in input:
        if row[consts.STREET] != '':
            url = GEOCODING_URL_BASE + get_address(row)
            # print(url)

            make_request(input, url)
        else:
            row.extend([0, 0])

        output.writerow(row)
        # print(row)
