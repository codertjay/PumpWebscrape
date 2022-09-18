import json
import os
import sys
import django

#  set the location of django settings to enable using the model
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PumpWebscrape.settings")
sys.path.append(os.path.join(os.path.realpath(os.path.dirname(__file__)), "..", ".."))
django.setup()

from corporation.models import Corporation


def CreateCorperationWitJsonFile():
    #  open the json file
    with open("./petrol_pumps.json", "r+") as f:
        for item in json.load(f):
            name = item.get("name")
            address = item.get("address")
            phone = item.get("phone")
            open_hours = item.get("open_hours")
            link = item.get("link")
            #  not all has decription since i dont need to webscrape all
            description = item.get("description", "No Description")
            try:
                #  create the cooperating
                Corporation.objects.create(
                    name=name,
                    address=address,
                    phone=phone,
                    open_hours=open_hours,
                    link=link,
                    description=description,
                )
            except Exception as a:
                print(a)


CreateCorperationWitJsonFile()
