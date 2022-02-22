import keyboard
import os
import pafy
import time
import pychromecast
from pychromecast.controllers.youtube import YouTubeController
import vlc
from youtube_search import YoutubeSearch
from ProgressBar import ProgressBar

clear = lambda: os.system('cls')

def pause():
    programPause = input("Press any key to exit...")

continueProgram = True

while continueProgram == True:
    isVideoStream = False
    audioCast =  'n' #input("cast the audio to a google device? y/n")

    searchTerms = input('What do you want to hear? ')

    results = YoutubeSearch(searchTerms, max_results=5).to_dict()

    if len(results) > 0:
        print("Here are the top 5 matches I found:")
        for x in range(0, len(results)):
            print(f'{ x+1 }.{ results[x]["title"] }')
        selection = 0
        while(selection not in [1,2,3,4,5]):
            selection = int(input("\nWhich would you like to play? "))

        if audioCast == 'y':
            #  # List chromecasts on the network, but don't connect
            services, browser = pychromecast.discovery.discover_chromecasts()
            # # Shut down discovery
            # pychromecast.discovery.stop_discovery(browser)

            # # Discover and connect to chromecasts named Living Room
            # chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names=["Gym speaker"])
            # [cc.device.friendly_name for cc in chromecasts]

            # cast = chromecasts[0]
            # # Start worker thread and wait for cast device to be ready
            # cast.wait()
            # print(cast.device)
            # print(cast.status)

            # cast.media_controller.play_media('"https://www.youtube.com/watch?v='+results[selection-1]['id']+'"', "audio/mp3")

            # player_state = None
            # t = 30
            # has_played = False
            # while True:
            #     try:
            #         if player_state != cast.media_controller.status.player_state:
            #             player_state = cast.media_controller.status.player_state
            #             print("Player state:", player_state)
            #         if player_state == "PLAYING":
            #             has_played = True
            #         if cast.socket_client.is_connected and has_played and player_state != "PLAYING":
            #             has_played = False
            #             cast.media_controller.play_media('"https://www.youtube.com/watch?v='+results[selection-1]['id']+'"', "audio/mp3")

            #         time.sleep(0.1)
            #         t = t - 0.1
            #     except KeyboardInterrupt:
            #         break

            # # Shut down discovery
            # pychromecast.discovery.stop_discovery(browser)
        else:
            print(f'Spinning up audio stream...')
            videoId = results[selection-1]['id']; #the code of the video marked in x here "https://www.youtube.com/watch?v=xxxxxxxxxxx"
            video = pafy.new(videoId)
            best = video.getbestaudio(preftype="m4a")
            if best == None:
                print("unable to find audio only stream, deafaulting to video")
                best = video.getbest(preftype="mp4")
                isVideoStream = True
            playurl = best.url

            Instance = vlc.Instance()
            player = Instance.media_player_new('--no-video')
            Media = Instance.media_new(playurl)
            Media.get_mrl()
            player.set_media(Media)
            player.play()
            time.sleep(2)

            duration = round(player.get_length() / 1000, 0)
            durationString = time.strftime('%H:%M:%S', time.gmtime(duration))
                
            bar = ProgressBar(40, int(duration))
            bar.ChangeLRChar('[', ']')
            bar.ChangeEmptyChar('-')
            bar.ChangeFilledChar('=') 
            bar.show_percentage = False
            
            clear()
            print(' __________________________________________________________________')
            print('|                                                                  |')
            print(f'|🔊 { results[selection-1]["title"] }')
            print(f'|Channel: { results[selection-1]["channel"] }')
            print(f'|Views: { results[selection-1]["views"] }')
            print(f'|Uploaded: { results[selection-1]["publish_time"] }')
            while player.get_state() == vlc.State.Playing:
                if isVideoStream == False:
                    currentTime = round(player.get_time() / 1000, 0)
                    bar.Update(int(currentTime))
                    print(f"| ▶({time.strftime('%H:%M:%S', time.gmtime(int(currentTime)))}){bar.display_string} ■[{durationString}]|", end='\r')
                else:
                    print(f"| ▶(🔴LIVE)", end='\r')
                time.sleep(0.5)
                # if keyboard.is_pressed('space'):
                #         player.stop()
            bar.Update(int(duration)+10)
        
    else:
        print("no results")
    
    print('\n')
    newSongCheck = ''
    while newSongCheck not in ['y','n']:
        newSongCheck = input("Would you like to play something else? [y/n]\n")
    
    continueProgram = newSongCheck == 'y'
