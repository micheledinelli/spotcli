import spotipy

def next(token, device_id):
    sp = spotipy.Spotify(auth=token)
    sp.next_track(device_id=device_id)

def previous(token, device_id):
    sp = spotipy.Spotify(auth=token)
    sp.previous_track(device_id=device_id)

def resume(token, device_id):
    sp = spotipy.Spotify(auth=token)
    sp.start_playback(device_id=device_id)

def pause(token, device_id):
    sp = spotipy.Spotify(auth=token)
    sp.pause_playback(device_id=device_id)