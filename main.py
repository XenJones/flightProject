# this is my python cli game
import os
import json
import csv
from csv import reader


def icaoSearch():
    airport = input('What airport do you want to search for?')
    with open('icao.csv', 'r') as readObj:
        f = reader(readObj)
        print(f)
        for row in f:
            print(row)
            if row[4].capitalize() in row:
                return airport[3]
            else:
                return ('Airport Not Found!!!')


icaoSearch()

# startup menu
print(
    '''Welcome to the game!
    In this game, you will be able to run your own airline!
    Your respinsibilities will include:
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
    print(icaoSearch())
    hubAirport = input('Please enter the ICAO code for the hub airport of your choice')

print('git sucks balls')
# test innnit