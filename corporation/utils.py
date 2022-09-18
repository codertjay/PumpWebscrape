import json
import os
import sys
import django
from celery import shared_task
from django.core.files import File

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Gimsap.settings")
sys.path.append(os.path.join(os.path.realpath(os.path.dirname(__file__)), "..", ".."))
django.setup()

from .models import Corporation


def CreateCoorperationWitJsonFile():
    with open("./petrol_pumps.json", "r") as f:
        for item in json.load(f):
            name = item.get("name")
            address = item.get("address")
            phone = item.get("phone")
            open_hours = item.get("open_hours")
            link = item.get("link")
            description = item.get("description")
            try:
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
