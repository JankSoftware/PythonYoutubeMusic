import pafy
import vlc
from youtube_search import YoutubeSearch

def pause():
    programPause = input("Press any key to exit...")

searchTerms = input('What do you want to hear?')

results = YoutubeSearch(searchTerms, max_results=1).to_dict()

if len(results) > 0:
    print(f'I found { results[0]["title"] }. \nPlaying...')
    # returns a dictionary
    url = results[0]['id']; #looks like "https://www.youtube.com/watch?v=xxxxxxxxxxx"
    video = pafy.new(url)
    best = video.getbest(preftype="mp4")
    playurl = best.url

    Instance = vlc.Instance()
    player = Instance.media_player_new('--no-video')
    Media = Instance.media_new(playurl)
    Media.get_mrl()
    player.set_media(Media)
    player.play()
    pause();
else:
    print("no results")
