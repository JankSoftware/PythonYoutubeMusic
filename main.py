import pafy
import time
import vlc
from youtube_search import YoutubeSearch

def pause():
    programPause = input("Press any key to exit...")

searchTerms = input('What do you want to hear? ')

results = YoutubeSearch(searchTerms, max_results=5).to_dict()

if len(results) > 0:
    print("Here are the top 5 matches I found:")
    for x in range(0, len(results)):
        print(f'{ x+1 }.{ results[x]["title"] }')
    selection = 0
    while(selection not in [1,2,3,4,5]):
        selection = int(input("\nWhich would you like to play? "))

    print(f'Selected: { results[selection-1]["title"] }. \nSpinning up audio stream...')
    # returns a dictionary
    videoId = results[selection-1]['id']; #the code of the video marked in x here "https://www.youtube.com/watch?v=xxxxxxxxxxx"
    video = pafy.new(videoId)
    best = video.getbestaudio(preftype="m4a")
    if best == None:
        print("unable to find audio only stream, deafaulting to video")
        best = video.getbest(preftype="mp4")
    playurl = best.url

    Instance = vlc.Instance()
    player = Instance.media_player_new('--no-video')
    Media = Instance.media_new(playurl)
    Media.get_mrl()
    player.set_media(Media)
    player.play()
    time.sleep(2)
    duration = round(player.get_length() / 1000, 0)
    while player.get_state() == vlc.State.Playing:
        currentTime = round(player.get_time() / 1000, 0)
        print(f"▶️  ({currentTime}/{duration})", end = "\r")
        time.sleep(1)
else:
    print("no results")
