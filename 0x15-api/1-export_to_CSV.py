#!/usr/bin/python3
"""Export data into the CSV format"""


import csv
import requests
import sys

if __name__ == '__main__':
    endpoint = "https://jsonplaceholder.typicode.com/"
    USER_ID = sys.argv[1]
    user = requests.get(endpoint + 'users/{}'.format(USER_ID)).json()
    todo = requests.get(endpoint + 'todos?userId={}'.format(USER_ID)).json()

    with open("{}.csv".format(USER_ID), 'w', newline='') as csvfile:
        write_to_file = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todo:
            write_to_file.writerow([int(USER_ID), user.get(
                'USERNAME'), task.get('TASK_COMPLETED_STATUS'), 
                task.get('TASK_TITLE')])
