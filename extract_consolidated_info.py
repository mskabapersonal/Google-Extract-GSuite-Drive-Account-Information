import requests
import csv
import json
import pygsheets
import os
from datetime import datetime, timezone
from dotenv import load_dotenv
import glob


def main():

    result_file = open('result.res', 'w')

    files = glob.glob("*.csv")
    for file in files:
        subscription = file.split(".")
        print("Running: "+subscription[0])
        with open(file) as csv_file:

            current_dic = {}
            csv_reader = csv.reader(csv_file)
            count_lines = 0
            for row in csv_reader:
                count_lines = count_lines+1
                if count_lines == 1:
                    continue
                if not(row[0] in current_dic):
                    current_dic[row[0]] = {}
                    current_dic[row[0]]["count"] = 0
                    current_dic[row[0]]["size"] = 0

                current_dic[row[0]]["count"] += 1
                current_dic[row[0]]["size"] += int(row[2])
        for user in current_dic:
            print (subscription[0]+","+user+","+str(current_dic[user]["count"])+","+str(current_dic[user]["size"]), file=result_file)
                                 
                                 


main()