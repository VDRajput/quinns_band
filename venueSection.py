import os.path
from pathlib import Path
import json


def addVenueDetails():
    checkVenuefile()
    venue_details = dict()
    venue_content = open("files/venue.txt","r+")
    if os.stat("files/venue.txt").st_size == 0:
        venue_details["venue"] = []
    else:
        venue_details = json.load(venue_content)
        venue_content.seek(0)
        venue_content.truncate()
    print("Please mention the venue details")
    vTitle = input("Venue Title: ")
    vAddress = input("Venue Address: ")
    vDate = input("Date of Performance (dd/mm/yyyy): ")
    vDetails = {
        "venue_title" : vTitle,
        "venue_address" : vAddress,
        "venue_date": vDate
    }
    venue_details["venue"].append(vDetails)
    venue_content.write(json.dumps(venue_details))

def updateVenueDetails():
    checkVenuefile()
    venue_content = open("files/venue.txt","r+")
    if os.stat("files/venue.txt").st_size == 0:
        print("No records found for venue")
        exit()
    else:
        venue_details = json.load(venue_content)
        venue_content.seek(0)
        venue_content.truncate()
    venueUpdate = print("Please mention the title for udpating venue details:")
    checkStatus = checkVenueExistsance(venueUpdate, venue_details)
    if checkStatus:
        updatedAddress = input("Updated Address : ")
        updatedDate = input("Updated Date (dd/mm/yyyy): ")
        for x in venue_details["venue"]:
            if x["venue_title"] == venueUpdate:
                x["venue_address"] = updatedAddress
                x["venue_date"] = updatedDate
        venue_content.write(json.dumps(venue_details))
    else:
        print("Sorry, such title is not available in database.")

def deleteVenuedetails():
    checkVenuefile()
    venue_content = open("files/venue.txt","r+")
    if os.stat("files/venue.txt").st_size == 0:
        print("No records found for venue")
        exit()
    else:
        venue_details = json.load(venue_content)
        venue_content.seek(0)
    venueTitle = input("Please mention the title of venue: ")
    checkStatus = checkVenueExistsance(venueTitle, venue_details)
    if checkStatus:
        for index, item in enumerate(venue_details["venue"]):
            if item["venue_title"] == venueTitle:
                print(index)
                venue_details["venue"].pop(index)
                break
        venue_content.truncate()
        venue_content.write(json.dumps(venue_details))
    else:
        print("No such venue available in database")

def checkVenuefile():
    if os.path.isfile("files/venue.txt"):
        print('file found')
    else:
        fileOpen = open("files/venue.txt","a")
        fileOpen.close()

def listAllVenueDetails():
    if not(Path('files/venue.txt').is_file):
        print("Data not found!")
    if os.stat("files/venue.txt").st_size == 0:
        print("No records found!")
    else:
        venue_content = open("files/venue.txt","r+")
        venue_details = json.load(venue_content)
        wid = 10
        keys_list = list(venue_details["venue"][0].keys())
        print("{} | {} | {}".format((keys_list[0].upper()).ljust(wid), (keys_list[1].upper()).ljust(wid),(keys_list[2].upper()).ljust(wid)))
        for x in venue_details["venue"]:
            print("{}| {}| {}".format(x["venue_title"].ljust(wid), x["venue_address"].ljust(wid),x["venue_date"].ljust(wid)))


def checkVenueExistsance(venueUpdate,venue_details):
    checkStatus = False
    for x in venue_details["venue"]:
        if x["venue_title"] == venueUpdate:
            checkStatus = True
            break
    return checkStatus