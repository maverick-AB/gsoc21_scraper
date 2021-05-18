import csv
import requests

url= 'https://summerofcode.withgoogle.com/api/program/current/project/'


with open('gsoc2021.csv','w', encoding='utf-8', newline='') as csv_file:
    field_names = ['Name', 'Organization','Project']
    writer = csv.DictWriter(csv_file, fieldnames=field_names)
    writer.writeheader()

    for i in range(1,66):
        params = (
            ('page', str(i)),
            ('page_size', '20'),
        )
        response = requests.get(url=url, params=params).json()
        data = response.get("results")
        for ele in data:
            vals = dict()
            vals['Name'] = ele.get("student").get("display_name")
            vals['Organization'] = ele.get('organization').get('name')
            vals['Project'] = ele.get("title")
            writer.writerow(vals)
            