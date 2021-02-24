from venueSection import getAllVenueList
from albumSection import getAllAlbumsList
import os.path
from pathlib import Path
import json


def addNewRecord():
    checkRecordsfile()
    addRecordDetails = dict()
    list_of_venues = getAllVenueList()
    print("select one of the venue")
    for index, x in enumerate(set(list_of_venues)):
        print(str(index+1) + ". " + x)
    Vselection = input("please select the venue: ")
    try:
        Vselection = int(Vselection) - 1
    except:
        print("please mention the number")
    addRecordDetails["venue"] = list_of_venues[Vselection]
    if len(list_of_venues) > 0:
        venue_content = open("files/venue.txt", "r")
        venue_details = json.load(venue_content)
        list_of_dates_for_selected_venue = []
        for x in venue_details["venue"]:
            if x["venue_title"] == list_of_venues[Vselection]:
                list_of_dates_for_selected_venue.append(x["venue_date"])
    print("We have following dates for selected venue")
    for index, x in enumerate(set(list_of_dates_for_selected_venue)):
        print(str(index+1) + ". " + x)
    vDateSelection = input(
        "please select the date of purchase(mention the number): ")
    try:
        vDateSelection = int(vDateSelection)-1
    except:
        print("please mention the number")
    addRecordDetails["date"] = list_of_dates_for_selected_venue[vDateSelection]
    list_of_albums = getAllAlbumsList()
    print("We have list of albums:")
    for index, x in enumerate(list_of_albums):
        print(str(index+1) + ". " + x)
    albumOpt = input("select the album: ")
    try:
        albumOpt = int(albumOpt) - 1
    except:
        print("Please mention the number")
    addRecordDetails["album"] = list_of_albums[albumOpt]
    message = """select one of the media.
    1. VinylDisc
    2. MP3
    3. FLAC
    4. Cloud
    Please select the media type: """
    mSelection = input(message)
    try:
        mSelection = int(mSelection)
    except:
        print("please mention the number")
    if mSelection == 1:
        addRecordDetails["type"] = "VinylDisc"
    elif mSelection == 2:
        addRecordDetails["type"] = "MP3"
    elif mSelection == 3:
        addRecordDetails["type"] = "FLAC"
    elif mSelection == 4:
        addRecordDetails["type"] = "Cloud"
    print(addRecordDetails)
    recordsSold = input("Please mention the number of records sold for such " + addRecordDetails["type"] + " in " + str(
        addRecordDetails["venue"]) + " on " + str(addRecordDetails["date"]) + ": ")
    try:
        recordsSold = int(recordsSold)
    except:
        print("Please mention the count in integer format")
    addRecordDetails["records_count"] = recordsSold
    records_details = dict()
    records_content = open("files/records.txt", "r+")
    if os.stat("files/records.txt").st_size == 0:
        records_details["records"] = []
    else:
        records_details = json.load(records_content)
        records_content.seek(0)
        records_content.truncate()
    records_details["records"].append(addRecordDetails)
    records_content.write(json.dumps(records_details))


def deleteExistingRecord():
    checkRecordsfile()
    records_content = open("files/records.txt", "r+")
    if os.stat("files/records.txt").st_size == 0:
        print("No records found")
        exit()
    else:
        records_details = json.load(records_content)
        records_content.seek(0)
    list_of_venues = getAllVenuesFromdb(records_details)
    for index, v in enumerate(list_of_venues):
        print(str(index+1) + ". " + v)
    venuesel = input("from which venue you want to delete record?: ")
    try:
        venuesel = int(venuesel) - 1
    except:
        print("please mention the number")
    list_of_dates = getAllDatesofVenueFromdb(
        list_of_venues[venuesel], records_details)
    print("we have following dates for selected venue: ")
    for index, v in enumerate(list_of_dates):
        print(str(index+1) + ". "+v)
    dateSel = input("from which date you want to delete the record?: ")
    try:
        dateSel = int(dateSel) - 1
    except:
        print("please mention the number")
    list_of_albums = getAllAlbumsFromdb(
        list_of_venues[venuesel], list_of_dates[dateSel], records_details)
    for index, v in enumerate(list_of_albums):
        print(str(index+1) + ". " + v)
    alSel = input("which album's record you want to delete?: ")
    try:
        alSel = int(alSel) - 1
    except:
        print("Please mention the number")
    list_of_total_records = getAllrecordsFromdb(
        list_of_venues[venuesel], list_of_dates[dateSel], list_of_albums[alSel], records_details)
    print("We have foud following records: ")
    for index,x in enumerate(list_of_total_records):
        print(str(index+1)+ ". " +"on {} at {} album {} sold {} of type {}".format(x["date"],x["venue"],x["album"],x["records_count"],x["type"]))
    delSel = input("which entry you want to delete?: ")
    try:
        delSel = int(delSel) - 1
    except:
        print("Please mention the number")
    if delSel < len(list_of_total_records):
        records_details = removeSelectedEntry(list_of_total_records[delSel],records_details)
        records_content.truncate()
        records_content.write(json.dumps(records_details))
    else:
        print("please mention the number in range")

def listAllRecords():
    if not(Path('files/records.txt').is_file):
        print("Data not found!")
    if os.stat("files/records.txt").st_size == 0:
        print("No records found!")
    else:
        records_content = open("files/records.txt","r")
        records_details = json.load(records_content)
        wid = 10
        keys_list = list(records_details["records"][0].keys())
        print("{} | {}| {}| {}| {}".format((keys_list[0].upper()).ljust(wid), (keys_list[1].upper()).ljust(wid),(keys_list[2].upper()).ljust(wid),(keys_list[3].upper()).ljust(wid),(keys_list[4].upper()).ljust(wid)))
        for x in records_details["records"]:
            print("{} | {}| {}| {}| {}".format(x["venue"].ljust(wid), x["date"].ljust(wid), x["album"].ljust(wid), x["type"].ljust(wid), str(x["records_count"]).ljust(wid)))

def checkRecordsfile():
    if os.path.isfile("files/records.txt"):
        print('file found')
    else:
        fileOpen = open("files/records.txt", "a")
        fileOpen.close()


def getAllVenuesFromdb(records_details):
    records_list = set()
    for x in records_details["records"]:
        records_list.add(x["venue"])
    return list(records_list)


def getAllDatesofVenueFromdb(venueSel, records_details):
    dates_list = set()
    for x in records_details["records"]:
        if x["venue"] == venueSel:
            dates_list.add(x["date"])
    return list(dates_list)


def getAllAlbumsFromdb(venueSel, dateSel, records_details):
    albumList = set()
    for x in records_details["records"]:
        if x["venue"] == venueSel and x["date"] == dateSel:
            albumList.add(x["album"])
    return list(albumList)

def getAllrecordsFromdb(venueSel,dateSel,alSel,records_details):
    recordsList = []
    for x in records_details["records"]:
        if x["venue"] == venueSel and x["date"] == dateSel and x["album"] == alSel:
            recordsList.append(x)
    return recordsList

def removeSelectedEntry(delSel, records_details):
    for index, item in enumerate(records_details["records"]):
            if item["venue"] == delSel["venue"] and item["date"] == delSel["date"] and item["album"] == delSel["album"] and item["type"] == delSel["type"]:
                records_details["records"].pop(index)
                break
    return records_details