from halo import Halo

import modules.utils as utils
import modules.nerd_commands as nerd_commands
import modules.player as player

import inquirer

import webbrowser

import modules.player as player

def search(sp, query, limit=10):
    with Halo(text='Fetching songs', spinner='dots'):
        # Retrieve information about song search
        results = sp.search(q=query, limit=limit)
        
        # Process the json
        songs_dict = results['tracks']
        song_items = songs_dict['items']
    
        name_uri_dict = {}
        for i, item in enumerate(song_items): 
            song_name = item['name']               
            artist_name = item["artists"][0]["name"]
            name_uri_dict[song_name + " - " + artist_name] = item['external_urls']['spotify']
    
    questions = [
        inquirer.List(
            "tracks",
            message="Which song do you want to play?",
            choices=name_uri_dict.keys(),
        ),
    ]

    answer = inquirer.prompt(questions)
    track_name = answer['tracks']
    device_list = nerd_commands.get_devices(sp, show=False)
    device_id = None
    for i, device in enumerate(device_list):
        if device["is_active"]:
            device_id = device_list[0]['id']   
            break

    uri = name_uri_dict[track_name]

    # Play or queue
    choices = ["Play", "Queue"]
    questions = [
        inquirer.List(
            "play or queue",
            message="What do you want to do",
            choices=choices,
        ),
    ]

    answer = inquirer.prompt(questions)

    ## Play
    if answer == choices[0]:
        if device_id is None:
            # TODO: complete this feat
            print("No active device found")
            webbrowser.open(uri)
        else:
            player.queue(sp=sp, device_id=device_id, uri=uri)
            player.next(sp=sp, device_id=device_id)
    elif answer == choices[1]:
        if device_id is None:
            # TODO: complete this feat
            print("No active device found")
            webbrowser.open(uri)
        else:
            player.queue(sp=sp, device_id=device_id, uri=uri)
    else:
        print("OK")

    