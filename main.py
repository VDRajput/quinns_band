from albumSection import *

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


def main():    
    message = """Hello Quinn,
    Select main area to check the details.
    1. Albums
    2. Media
    3. Venue
    4. Records Sellings
    5. Exit
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