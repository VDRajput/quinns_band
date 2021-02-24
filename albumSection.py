import os.path
import json
from pathlib import Path

def addNewAlbum():
    checkAlbumfile()
    main_album = dict()
    album_content = open('files/albums.txt','r+')
    if os.stat('files/albums.txt').st_size == 0:
        main_album["albums"] = []
    else:
        main_album = json.load(album_content)
        album_content.seek(0)
    print("Please mention following details:")
    albumName = input("Album Name: ")
    albumYear = input("Album Year: ")
    albumSongs = input("Tracks count: ")
    albumDetails = {
        "name": albumName,
        "year": albumYear,
        "songs": albumSongs
    }
    checkDuplicate = True
    for x in main_album["albums"]:
        for k,v in x.items():
            if v == albumDetails["name"] and k == "name":
                print("we have existing album")
                print(x)
                checkDuplicate = False
    if checkDuplicate:
        album_content.truncate()
        main_album["albums"].append(albumDetails)
        album_content.write(json.dumps(main_album))

def updateAlbum():
    checkAlbumfile()
    album_content = open('files/albums.txt','r+')
    if os.stat('files/albums.txt').st_size == 0:
        print("No records found to update the album details")
        exit()
    else:
        main_album = json.load(album_content)
        album_content.seek(0)
        album_content.truncate
    alName = input("Mention the album name want to update: ")
    checkStatus = checkExistance(alName, main_album)
    if checkStatus:
        updatedAlbumYear = input("updated Album Year: ")
        updatedAlbumSongs = input("updated tracks count: ")
        for x in main_album["albums"]:
            if x["name"] == alName:
                x["year"] = updatedAlbumYear
                x["songs"] = updatedAlbumSongs
        album_content.write(json.dumps(main_album))
    else:
        print("Sorry, such album details is not available")

def deleteAlbum():
    checkAlbumfile()
    album_content = open('files/albums.txt','r+')
    if os.stat('files/albums.txt').st_size == 0:
        print("No records found for album details")
        exit()
    else:
        main_album = json.load(album_content)
        album_content.seek(0)
    alName = input("Mention the album name want to delete: ")
    checkStatus = checkExistance(alName, main_album)
    if checkStatus:
        for index, item in enumerate(main_album["albums"]):
            if item["name"] == alName:
                main_album["albums"].pop(index)
                break
        album_content.truncate()
        album_content.write(json.dumps(main_album))
    else:
        print("Sorry, such album details is not available")

def listAllAlbums():
    if not(Path('files/albums.txt').is_file):
        print("file does not exists!")
        exit()
    if os.stat('files/albums.txt').st_size == 0:
        print("no records found.")
    else:
        album_content = open('files/albums.txt','r')
        album_data = json.load(album_content)
        print(album_data)
        wid = 15
        keys_list = list(album_data["albums"][0].keys())
        print("{}| {}| {}".format((keys_list[0].upper()).ljust(wid), (keys_list[1].upper()).ljust(wid),(keys_list[2].upper()).ljust(wid)))
        for x in album_data["albums"]:
            print("{}| {}| {}".format(x["name"].ljust(wid), x["year"].ljust(wid),x["songs"].ljust(wid)))

def checkAlbumfile():
    if os.path.isfile("files/albums.txt"):
        print("File found")
    else:
        fileOpen = open("files/albums.txt")
        fileOpen.close()

def checkExistance(alName,album_content):
    status = False
    for x in album_content["albums"]:
        if x["name"] == alName:
            status = True
            break
    return status

def getAllAlbumsList():
    list_of_albums = set()
    if not(Path('files/albums.txt').is_file):
        print("file does not exists!")
        exit()
    if os.stat('files/albums.txt').st_size == 0:
        print("no records found.")
    else:
        album_content = open('files/albums.txt','r')
        album_data = json.load(album_content)
        for x in album_data["albums"]:
            list_of_albums.add(x["name"])
    return list(list_of_albums)