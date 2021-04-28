import pafy
import vlc
from youtube_search import YoutubeSearch

def pause():
    programPause = input("Press any key to exit...")

searchTerms = input('What do you want to hear?')

results = YoutubeSearch(searchTerms, max_results=1).to_dict()

if len(results) > 0:
    print(f'I found { results[0]["title"] }. Playing...')
    # returns a dictionary
    url = results[0]['id']; #"https://www.youtube.com/watch?v=cCq0P509UL4"
    video = pafy.new(url)
    best = video.getbest(preftype="mp4")
    playurl = best.url

    Instance = vlc.Instance()
    player = Instance.media_player_new()
    Media = Instance.media_new(playurl)
    Media.get_mrl()
    player.set_media(Media)
    player.play()
    pause();
else:
    print("no results")
