# import csv
# import json
#
#
# def flattenjson(b, delim):
#     val = {}
#     for i in b.keys():
#         if isinstance(b[i], dict):
#             get = flattenjson(b[i], delim)
#             for j in get.keys():
#                 val[i + delim + j] = get[j]
#         else:
#             val[i] = b[i]
#
#     return val
#
#
# with open(fname, 'wb') as out_file:
#     csv_w = csv.writer(out_file)
#     csv_w.writerow(columns)
#
#     for i_r in input:
#         csv_w.writerow(map(lambda x: i_r.get(x, ""), columns))

import csv
import json
import sys

# if you are not using utf-8 files, remove the next line
# sys.setdefaultencoding("UTF-8")  # set the encode to utf8
# check if you pass the input file and output file
if sys.argv[1] is not None and sys.argv[2] is not None:
    fileInput = sys.argv[1]
    fileOutput = sys.argv[2]
    inputFile = open(fileInput, "r", encoding="utf-8")  # open json file
    outputFile = open(fileOutput, "w")  # load csv file
    # data = json.load(inputFile)  # load json content
    data = json.load(inputFile)["data"]  # load json content
    # data = json.load(inputFile)["data"]["cards"]  # load json content
    print(data)
    print(data[0])
    inputFile.close()  # close the input file

    year = 2018
    region = {
        "id": 50,
        "name": "Новосибирская область",
    }
    months = [3, 3]

    dtp_dict = {"data": {}}
    dtp_dict["data"]["year"] = str(year)
    dtp_dict["data"]["region_code"] = region["id"]
    dtp_dict["data"]["region_name"] = region["name"]
    dtp_dict["data"]["month_first"] = months[0]
    dtp_dict["data"]["month_last"] = months[-1]

    dtp_dict["data"]["cards"] = []

    cards = get_dtp_data(region["id"], region["name"], district["id"], district["name"], months, year)

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

    # output = csv.writer(outputFile)  # create a csv.write
    # # output.writerow(data[0].keys())  # header row
    # for row in data:
    #     # print(row)
    #     output.writerow(row.values())  # values row
    #     # print(row.values())
