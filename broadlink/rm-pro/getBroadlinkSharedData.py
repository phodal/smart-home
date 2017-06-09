# -*- coding: utf-8 -*-

'''
This script will "parse" the broadlink e-Control Android application "SharedData" json files and dump the IR / RF codes for selected accessories into a text file which can be later used with broadlink-python to send the codes to the RM PRO hub
NO ROOT ACCESS REQUIRED

Just connect your Android device to your computer and browse the SD card / External Storage folder "/broadlink/newremote/SharedData/"
You need to get the following files:

jsonSubIr
jsonButton
jsonIrCode

and put them in the same folder as this script.

run: python getBroadlinkSharedData.py

'''

import simplejson as json


buttonIDS = []
buttonNames = []


jsonSubIr = open("jsonSubIr").read()
jsonSubIrData = json.loads(jsonSubIr)


for i in range(0, len(jsonSubIrData)):
    print "ID:", jsonSubIrData[i]['id'], "| Name:", jsonSubIrData[i]['name']


choice = input("Select accessory ID: ")

for i in range(0, len(jsonSubIrData)):
    if jsonSubIrData[i]['id'] == choice:
        accessory_name = jsonSubIrData[i]['name']
        print "[+] You selected: ", accessory_name


jsonButton = open("jsonButton").read()
jsonButtonData = json.loads(jsonButton)


for i in range(0, len(jsonButtonData)):
    if jsonButtonData[i]['subIRId'] == choice:
        buttonIDS.append(jsonButtonData[i]['id'])
        buttonNames.append(jsonButtonData[i]['name'])


jsonIrCode = open("jsonIrCode").read()
jsonIrCodeData = json.loads(jsonIrCode)


print "[+] Dumping codes to " + accessory_name + ".txt"
codesFile = open(accessory_name + '.txt', 'w')

for i in range(0, len(jsonIrCodeData)):
    for j in range(0, len(buttonIDS)):
        if jsonIrCodeData[i]['buttonId'] == buttonIDS[j]:
            code = ''.join('%02x' % (i & 0xff) for i in jsonIrCodeData[i]['code'])
            result = "Button Name: " + buttonNames[j] + " | Button ID: " + str(jsonIrCodeData[i]['buttonId']) + " | Code: " + code
            codesFile.writelines(result.encode('utf-8'))
