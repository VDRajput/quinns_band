from albumSection import *
from venueSection import *
from recordsSellingsSection import *

def albumArea():
    message = """Hello Quinn,
    What do you want to do in Album section?
    1. Add new Album
    2. Update Album details
    3. Delete Album
    4. List all Albums.
    Enter selection number: """
    alOpt = input(message)
    try:
        alOpt = int(alOpt)
    except:
        print("Please mention the number")
        albumArea()
    if alOpt == 1:
        addNewAlbum()
    elif alOpt == 2:
        updateAlbum()
    elif alOpt == 3:
        deleteAlbum()
    elif alOpt == 4:
        listAllAlbums()
    else:
        print("Please enter valid number (1,2,3 or 4)")
        albumArea()

def mediaArea():
    print("Thinking on it")

def venueArea():
    message = """Hello Quinn,
    Welcome to Venue section.
    1. Add new Venue details
    2. Update venue details
    3. Delete venue details
    4. List all Venue schedules
    Enter the selection: """
    vOpt = input(message)
    try:
        vOpt = int(vOpt)
    except:
        print("Please mention the number")
        venueArea()
    if vOpt == 1:
        addVenueDetails()
    elif vOpt == 2:
        updateVenueDetails()
    elif vOpt == 3:
        deleteVenuedetails()
    elif vOpt == 4:
        listAllVenueDetails()
    else:
        print("invalid selection")
        venueArea()

def recordsSellingsArea():
    message = """Hello Quinn,
    Welcome to Records collections section.
    1. Add new sales entry
    2. Delete sales entry
    3. List out collection
    Please enter the selection: """
    optSelection = input(message)
    try:
        optSelection = int(optSelection)
    except:
        print("Please mention the number")
        recordsSellingsArea()
    if optSelection == 1:
        addNewRecord()
    elif optSelection == 2:
        deleteExistingRecord()
    elif optSelection == 3:
        listAllRecords()
    else:
        print("Please mention the number 1,2 or 3")
        recordsSellingsArea()

def main():    
    message = """Hello Quinn,
    Select main area to check the details.
    1. Albums
    2. Media
    3. Venue
    4. Records Sellings
    5. Popular records at each venue
    6. Exit
    Enter selection number: """
    selOpt = input(message)
    try:
        selOpt = int(selOpt)
    except:
        print("Please mention the number")
        main()
    if selOpt == 1:
        albumArea()
    elif selOpt == 2:
        mediaArea()
    elif selOpt == 3:
        venueArea()
    elif selOpt == 4:
        recordsSellingsArea()
    elif selOpt == 5:
        exit()
    else:
        print("Please enter valid number (1,2,3,4 or 5) ")
        main()

if __name__ == "__main__":
    main()