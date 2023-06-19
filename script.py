import os
import django

#sys.path.append(your_djangoproject_home)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TestApp.settings')
django.setup()

from api.models import Data

import csv
# import the csv file
dataReader = csv.reader(open("data.csv"), delimiter=',', quotechar='"')
ctr = 1
# loop through the csv list
for row in dataReader:
    if ctr == 1:
        ctr += 1
        continue
    # create and save the data
    data=Data()
    data.id=row[0]
    data.date=row[1]
    data.user=row[2]
    data.department=row[3]
    data.software=row[4]
    data.seats=row[5]
    data.amount=row[6]
    data.save()