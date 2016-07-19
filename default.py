# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Youtube Channel
# (c) 2015 - Simple TechNerd
# Based on code from youtube addon
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.KiSaKuLutube'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')


channellist=[
        ("Jacy and Kacy", "user/JacyandKacy", 'https://yt3.ggpht.com/-QyIDLvH__ic/AAAAAAAAAAI/AAAAAAAAAAA/ICg5SwukIi4/s900-c-k-no-rj-c0xffffff/photo.jpg'),
		
		("Cosmic Kids Yoga", "user/CosmicKidsYoga", 'https://yt3.ggpht.com/-R8qBuZD3mvY/AAAAAAAAAAI/AAAAAAAAAAA/UoJoanFKpsQ/s900-c-k-no-rj-c0xffffff/photo.jpg'),
		
		("TheDiamondMinecart - DanTDM", "user/TheDiamondMinecart", 'https://yt3.ggpht.com/-KEJYjuwz0-c/AAAAAAAAAAI/AAAAAAAAAAA/ScEc76PWvak/s900-c-k-no-rj-c0xffffff/photo.jpg'),
		
        ("Eckhart Tolle", "user/EckhartTeachings", 'https://yt3.ggpht.com/-yNVptYofVwk/AAAAAAAAAAI/AAAAAAAAAAA/_2CzvRtUfQQ/s900-c-k-no-rj-c0xffffff/photo.jpg'),
		
        ("lecturesbeyondbeyond", "user/lecturesbeyondbeyond", 'https://yt3.ggpht.com/-D9XNzAEMsAQ/AAAAAAAAAAI/AAAAAAAAAAA/13BerxR_wL0/s900-c-k-no-rj-c0xffffff/photo.jpg'),
		
		("Pathways of Light – ACIM Insights, Ministers, and Courses", "user/aciminsights", 'https://yt3.ggpht.com/-Q7edPn7MyDE/AAAAAAAAAAI/AAAAAAAAAAA/cysFmWYGNQU/s900-c-k-no-rj-c0xffffff/photo.jpg'),
		
		("FndtnACIM", "user/FndtnACIM", 'https://yt3.ggpht.com/-kFQFoOlVork/AAAAAAAAAAI/AAAAAAAAAAA/CoFPtxvJlL8/s900-c-k-no-rj-c0xffffff/photo.jpg'),
		
        ("Tommy Rosen", "user/tommyrosen", 'https://yt3.ggpht.com/-vxxLt1GXjFc/AAAAAAAAAAI/AAAAAAAAAAA/od0sMh3U6Dk/s900-c-k-no-rj-c0xffffff/photo.jpg'),
		
		("GabrielleBernstein", "user/GabrielleBernstein", 'https://yt3.ggpht.com/-pFpCtphDCtk/AAAAAAAAAAI/AAAAAAAAAAA/qND9aRr9p84/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
		
		("Mighty Companion", "user/TheBarefootBarrister", 'https://yt3.ggpht.com/-3JBkthj-l6c/AAAAAAAAAAI/AAAAAAAAAAA/ql7uQI5Xr_o/s900-c-k-no-rj-c0xffffff/photo.jpg'),
		
		("Mooji", "user/Moojiji", 'https://yt3.ggpht.com/-RP-p6vXMiqI/AAAAAAAAAAI/AAAAAAAAAAA/cW2unOJTh2E/s900-c-k-no-rj-c0xffffff/photo.jpg'),
		
		("Ron Lukasik", "user/rluke14", 'https://yt3.ggpht.com/-KfI5ARBsttc/AAAAAAAAAAI/AAAAAAAAAAA/JyUF8pLg2U0/s900-c-k-no-rj-c0xffffff/photo.jpg'),
		
        ("The Football Source", "user/TheFootballSource", 'https://yt3.ggpht.com/-I8UPPwSxCcc/AAAAAAAAAAI/AAAAAAAAAAA/k1B7xjEHYnw/s900-c-k-no-rj-c0xffffff/photo.jpg')]



# Entry point
def run():
    plugintools.log("youtubeAddon.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("youtubeAddon.main_list "+repr(params))

for name, id, icon in channellist:
	plugintools.add_item(title=name,url="plugin://plugin.video.youtube/"+id+"/",thumbnail=icon,folder=True )



run()