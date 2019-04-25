import csv
import json
import sys
from pprint import pprint

# if you are not using utf-8 files, remove the next line
# sys.setdefaultencoding("UTF-8")  # set the encode to utf8
# check if you pass the input file and output file

if sys.argv[1] is not None and sys.argv[2] is not None:
    file_input = sys.argv[1]
    file_output = sys.argv[2]

    with open(file_input, "r", encoding="utf-8") as f:
        data = json.load(f)  # load json content

    all_data = json.loads(data["data"])
    # print(data["data"])
    # print(all_data)
    # pprint(all_data)
    year = all_data["year"]
    region_code = all_data["region_code"]
    region_name = all_data["region_name"]
    month_first = all_data["month_first"]
    month_last = all_data["month_last"]
    print(year)
    print(region_code)
    print(region_name)
    print(month_first)
    print(month_last)

    cards = json.loads(data["data"])["cards"]

    pprint(cards[0])
    pprint(cards[10])
    pprint(cards[20])
    pprint(cards[30])
    pprint(cards[90])

    with open(file_output, "w") as f:
        output = csv.writer(f)  # create a csv.write
        for card in cards:
            # pprint(card)

            district = f", {card['District']}" if card['District'] else ""
            locality = f", {card['infoDtp']['n_p']}" if card['infoDtp']['n_p'] else ""
            location = f"{region_name}{district}{locality}"

            # dtp_dict = {
            #     "DATE": card['date'],
            #     "TIME": card['Time'],
            #     "TYPE": card['DTP_V'],
            #     "LOCATION": location,
            #     "STREET": card['infoDtp']['street'],
            #     "HOUSE_NUMBER": card['infoDtp']['house'],
            #     "ROAD": card['infoDtp']['dor'],
            #     "KILOMETER": card['infoDtp']['km'],
            #     "METER": card['infoDtp']['m'],
            #     "LONGITUDE": card['infoDtp']['COORD_L'],
            #     "LATITUDE": card['infoDtp']['COORD_W'],
            #     "DEATH": card['POG'],
            #     # "DEATH_CHILDREN": card['date'],
            #     "DEATH_CHILDREN": 0,
            #     "INJURY": card['RAN'],
            #     # "INJURY_CHILDREN": card['date'],
            #     "INJURY_CHILDREN": 0,
            #
            #     "LONGITUDE_GEOCODE": '',
            #     "LATITUDE_GEOCODE": '',
            #     "VALID": '',
            #     "VALID_STRICT": '',
            # }
            # pprint(dtp_dict)

            dtp_list = [
                card['date'],
                card['Time'],
                card['DTP_V'],
                location,
                card['infoDtp']['street'],
                card['infoDtp']['house'],
                card['infoDtp']['dor'],
                card['infoDtp']['km'],
                card['infoDtp']['m'],
                card['infoDtp']['COORD_L'],  # LONGITUDE
                card['infoDtp']['COORD_W'],  # LATITUDE
                card['POG'],  # DEATH
                0,  # DEATH_CHILDREN
                card['RAN'],  # INJURY
                0,  # INJURY_CHILDREN
                # '',  # LONGITUDE_GEOCODE
                # '',  # LATITUDE_GEOCODE
                # '',  # VALID
                # '',  # VALID_STRICT
            ]
            # pprint(dtp_list)

            output.writerow(dtp_list)  # values row
