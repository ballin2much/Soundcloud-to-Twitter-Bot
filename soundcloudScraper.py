import soundcloud, config

client = soundcloud.Client(client_id=config.CLIENT_ID)

def writeAllTracks(id):
    tracks = client.get('/tracks', user_id = id)
    for track in tracks:
        with open('tracklist.txt', 'a') as myfile:
            myfile.write(track.permalink_url + '\n')
            myfile.close()

def writeCurrentTrack(newTrack):
        with open('tracklist.txt', 'a') as myfile:
            myfile.write('\n' + newTrack.permalink_url)
            myfile.close()

def getNewestTrackNameandURL(id):
    nameandURL = []
    tracks = client.get('/tracks', user_id = id, limit = 1)
    for track in tracks:
        if checkNew(track.permalink_url):
            nameandURL.append(track.title)
            nameandURL.append(track.permalink_url)
            writeCurrentTrack(track)
            return nameandURL

def checkNew(URL):
    with open('tracklist.txt') as f:
        ourString = f.read()
    subString = ourString.split('\n')
    for trackURL in subString:
        if trackURL == URL:
            return False
    return True