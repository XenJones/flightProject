# this is my python cli game
import os
import json
import csv
import random
import math

def icaoSearch():
    airport = input('What airport do you want to search for?').upper()
    with open('icao.csv', 'r', encoding='utf-8') as readObj:
        f = csv.reader(readObj)
        for row in f:
            if airport in row[4].upper():
                returnAirport = row[3]
                break
            else:
                returnAirport = 'Not Found!'
    return returnAirport


def affordAircraft():
    with open("aircraftInfo.json", "r") as aircraftInfo:
        data = json.load(aircraftInfo)
        for i in range(len(data)):
            for j in data[i].get("Aircraft"):
                if j.get("price") < userDict.get("money"):
                    print(j)


def purchaseAircraft(name):
    with open("aircraftInfo.json", "r+") as aircraftInfo:
        data = json.load(aircraftInfo)
        for i in range(len(data)):
            for j in data[i].get("Aircraft"):
                if j.get("price") < userDict.get("money"):
                    if j.get("model") == name:
                        userDict['money'] -= j.get("price")
                        print(f"you have bought {j.get('model')}, for {j.get('price')}")
                        userDict['ownedAircraft'][name] +=1
                        print(userDict)

def saveUserInfo():
    with open('userInfo.json', 'w') as jsonFile:
        jsonObject = json.dumps(userDict)
        jsonFile.write(jsonObject)

def distance(origin, destination):
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 3440.065 # nm

    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c

    return d

def planRoute(ICAO1, ICAO2):
    csvFile = open('icao.csv', 'r', encoding='utf-8')
    f = csv.reader(csvFile)
    for row in f:
        if ICAO1 == row[3]:
            print('fuck you')
            ICAO1Lat = float(row[5])
            ICAO1Long = float(row[6])
        if ICAO2 == row[3]:
            ICAO2Lat = float(row[5])
            ICAO2Long = float(row[6])

    plane = input('please choose a plane for this route')
    if userDict['ownedAircraft'][plane] > 0:
        with open('aircraftInfo.json', 'r') as jsonFile:
            data = json.load(jsonFile)
            for i in range(len(data)):
                for j in data[i].get("Aircraft"):
                    if j.get('model') == plane:
                        planeRange = j.get('range')

    routeDistance = distance((ICAO1Lat, ICAO1Long), (ICAO2Lat, ICAO2Long))
    if routeDistance <= planeRange:
        with open('routes.json', 'w') as routesFile:
            routeDict = {'ICAO1': ICAO1, 'ICAO2' : ICAO2, 'length' : routeDistance, 'plane' : plane}
            data = json.dumps(routeDict)
            routesFile.write(data)

# startup menu
print(
    '''Welcome to the game!
    In this game, you will be able to run your own airline!
    Your responsibilities will include:
        - Buying planes
        - Running routes
        - Scheduling maintainence
    I hope you enjoy!
    '''
)
input('Press any key to continue...')

os.system('cls')

menu = int(input(
    '''Please select an option to start!
    1. start a new game
    2. resume a saved game
    3. exit the game
    '''
))

os.system('cls')

if menu == 1:
    userInfo = open('userInfo.json', 'w')
    tutorialOption = 'hehe'
    while tutorialOption != 'Y' and tutorialOption != 'N':
        tutorialOption = (
            input('Would you like a breif tutorial on some of the terms used in this game? (Y/n)')).upper()

    if tutorialOption == 'Y':
        print('''
        Here is a quick guide on some of the terminology used in this game:
        in this game we will be using the standardised ICAO system for naming airports
        you can find these online or in the ICAO.txt file in the main directory
        there will also be prompts to search for codes whenever one needs entering

        an ICAO code consits of 4 letters
        the first letter denotes the general area (for example, E is for Europe, K is for the states)
        the second letter then denotes the country (or territory) in the general area (eg EG for the united kingdom)
        Finally the last two letters are specific to the airport for example EGKK is london gatwick''')
        input('Press any key to continue...')
        os.system('cls')

    print('starting profile creation...')
    firstName = input('What is your name?')
    lastName = input('What is your last name?')
    choice = input('Do you need to search for an ICAO code? (Y/n) ')
    if choice.upper() == 'Y':
        print(f'your ICAO code is {icaoSearch()}')
    hubAirport = input('Please enter the ICAO code for the hub airport of your choice')
    userPass = random.randint(100000, 999999)
    print(f'your 6 digit code is {userPass} please keep this safe as you will need it next time you log in!')
    userDict = {
        'firstName': firstName,
        'lastName': lastName,
        'userpass': userPass,
        'hubAirport': hubAirport,
        'money': 40000000,
        'ownedAircraft': {
            "A320neo": 0,
            "A321": 0,
            "A330-300": 0,
            "737-800": 0,
            "737-900ER": 0,
            "747-400": 0,
            "777-200LR": 0,
            "CRJ200": 0,
            "CRJ900": 0,
            "E175": 0

        }
    }

    os.system('cls')
    # game first steps
    print('you have been given a very generous starting grant of $40,000,000')
    print("you can afford the following aircraft: ")
    affordAircraft()
    aircraftToPurchase = input("Enter the name of the aircraft you would like to buy")
    purchaseAircraft(aircraftToPurchase)
    print('Well done, you have just purchased your first aircraft!')

    saveUserInfo()

    os.system('cls')

    print('lets plan your first route!')
    print('you need to choose a start and end airport, ')
    print('if you are having difficulties finding one look here https://ourairports.com/world.html')
    ICAO1 = input('please enter the ICAO of your first airport')
    ICAO2 = input('please enter the ICAO of your second airport')
    planRoute(ICAO1, ICAO2)
    print('Well done, you just planned your first route, we are now going to return you to the main menu.')
    print('From there, you can begin to fly routes and earn money, good luck and have fun!')