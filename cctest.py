import time
import pychromecast

 # List chromecasts on the network, but don't connect
services, browser = pychromecast.discovery.discover_chromecasts()
# Shut down discovery
pychromecast.discovery.stop_discovery(browser)

# Discover and connect to chromecasts named Living Room
chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names=["Gym speaker"])
[cc.device.friendly_name for cc in chromecasts]

cast = chromecasts[0]
# Start worker thread and wait for cast device to be ready
cast.wait()
print(cast.device)

print(cast.status)

mc = cast.media_controller
mc.play_media('http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4', 'video/mp4')
mc.block_until_active()
print(mc.status)

mc.pause()
time.sleep(5)
mc.play()

# Shut down discovery
pychromecast.discovery.stop_discovery(browser)