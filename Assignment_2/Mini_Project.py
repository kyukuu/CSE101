# Group Members:
# Parth Garg (2022351)
# Shagun Yadav (2022466)
# Swarnima Prasad (2022525)

import requests
try:
    # first letter of every word should be capital
    API_KEY = "e82a3eac1a45d908733a4dee786ac302"
    artist = input("Enter Artist Name: ").title()
    # url has plus sign instead of space
    artist = artist.replace(' ', '+')

    resp = requests.get(
        f"http://ws.audioscrobbler.com/2.0/?method=artist.gettoptracks&artist={artist}&api_key={API_KEY}&format=json"
    )
    toptrack = resp.json()
    song_list = []
    for song in toptrack["toptracks"]["track"]:     # list of top songs
        song_list.append(song["name"])
    for i in range(len(song_list)):     # url has plus sign instead of space
        song_list[i] = song_list[i].replace(" ", "+")

    print()
    print('Songs sung by', artist.replace('+', ' ')+':')
    print('--------------'+('-'*(len(artist)+1)))
    for i in song_list:
        print(i.replace('+', ' '))

    print()
    print('Songs and their metadata:')
    print('-------------------------')
    i = 1
    for song in song_list:      # extracting song data
        resp = requests.get(
            f'http://ws.audioscrobbler.com/2.0/?method=track.getInfo&api_key={API_KEY}&artist={artist}&track={song}&format=json'
        )
        song_data = resp.json()
        try:
            name = song.replace('+', ' ')
            release_date = song_data["track"]["wiki"]["published"]
            summary = song_data["track"]["wiki"]["summary"]
            url = song_data["track"]["url"]
            print(str(i)+')', name+',',
                  artist.replace('+', ' ')+',', release_date)
            i += 1
            print()
            print('Song Trivia:')
            print('------------')
            print(summary)
            print()
            print('Song URL:')
            print('---------')
            print(url)
            print()
            print()
        except:
            print('No metadata exists for', name)
            continue
except:
    print('Artist Not Found')
