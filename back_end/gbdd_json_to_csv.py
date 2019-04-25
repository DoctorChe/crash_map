import csv
import json
import sys

# if you are not using utf-8 files, remove the next line
# sys.setdefaultencoding("UTF-8")  # set the encode to utf8
# check if you pass the input file and output file
from pprint import pprint

if sys.argv[1] is not None and sys.argv[2] is not None:
    fileInput = sys.argv[1]
    fileOutput = sys.argv[2]
    inputFile = open(fileInput, "r", encoding="utf-8")  # open json file
    data = json.load(inputFile)  # load json content
    inputFile.close()  # close the input file

    cards = json.loads(data["data"])["cards"]
    pprint(cards[0])

    card = cards[0]

    dtp_dict = {
        "DATE": card['date'],
        "TIME": card['Time'],
        "TYPE": card['DTP_V'],
        "LOCATION": card['District'],
        "STREET": card['infoDtp']['k_ul'],
        "HOUSE_NUMBER": card['infoDtp']['house'],
        "ROAD": card['infoDtp']['dor'],
        "KILOMETER": card['infoDtp']['km'],
        "METER": card['infoDtp']['m'],
        "LONGITUDE": card['infoDtp']['COORD_L'],
        "LATITUDE": card['infoDtp']['COORD_W'],
        "DEATH": card['POG'],
        # "DEATH_CHILDREN": card['date'],
        "INJURY": card['RAN'],
        # "INJURY_CHILDREN": card['date'],

        # "LONGITUDE_GEOCODE": card['date'],
        # "LATITUDE_GEOCODE": card['date'],
        # "VALID": card['date'],
        # "VALID_STRICT": card['date'],
    }

    pprint(dtp_dict)

    # print(data[0])


    # year = 2018
    # region = {
    #     "id": 50,
    #     "name": "Новосибирская область",
    # }
    # months = [3, 3]
    #
    # dtp_dict = {"data": {}}
    # dtp_dict["data"]["year"] = str(year)
    # dtp_dict["data"]["region_code"] = region["id"]
    # dtp_dict["data"]["region_name"] = region["name"]
    # dtp_dict["data"]["month_first"] = months[0]
    # dtp_dict["data"]["month_last"] = months[-1]
    #
    # dtp_dict["data"]["cards"] = []

    # cards = get_dtp_data(region["id"], region["name"], district["id"], district["name"], months, year)

    # for card in cards:
    #     # получение карточек ДТП
    #     log_text = "Обрабатываются данные для {0} ({1}) за {2}-{3}.{4}".format(region["name"],
    #                                                                            district["name"],
    #                                                                            months[0],
    #                                                                            months[-1],
    #                                                                            year)
    #     print(log_text)
    #     write_log(log_text)
    #     cards = get_dtp_data(region["id"], region["name"], district["id"], district["name"], months, year)

    outputFile = open(fileOutput, "w")  # load csv file
    # output = csv.writer(outputFile)  # create a csv.write
    # # output.writerow(data[0].keys())  # header row
    # for row in data:
    #     # print(row)
    #     output.writerow(row.values())  # values row
    #     # print(row.values())
