import json
import urllib.request as req
import csv
url="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"

request=req.Request(url)

with req.urlopen(request) as response:
    data=response.read().decode("UTF-8")
data=json.loads(data)
print(type(data))

sites=data["result"]["results"]

with open("data.csv",'w',encoding="UTF-8") as csv_data:
    for site in sites:
        write=csv.writer(csv_data)
        write.writerow([site["stitle"],site["address"][5:8],site["longitude"],site["latitude"],site["file"].lower().split("jpg")[0]+"jpg"])
