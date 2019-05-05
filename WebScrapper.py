import requests
from bs4 import BeautifulSoup

page = requests.get("http://apps.bexar.org/CMAGSearchList/")
soup = BeautifulSoup(page.text, 'html.parser')
for element in soup.find_all("tr")[1:]:
    record = element.text.rstrip().split()

    #Print Record!
    name = " ".join(record[:-4])
    race = record[-4]
    age = record[-3]
    sid = record[-2]
    intakeNum = record[-1]

    print("Name: {}\nRace: {}\nAge: {}\nSID: {}\nIntake Number: {}\n".format(name, race, age, sid, intakeNum))
