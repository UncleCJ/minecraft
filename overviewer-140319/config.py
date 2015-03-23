
#overviewer.py  --rendermodes=smooth_lighting,cave ~/opt/minecraft_server/tutworld /var/www/overviewer-140319

worlds["My world"] = "~/opt/minecraft_server/tutworld"

renders["normalrender"] = {
    "world": "My world",
    "title": "Normal Render of My World",
    // "markers": "foobar",
}

renders["caverender"] = {
    "world": "My world",
    "rendermode": "cave",
    "title": "Cave Render of My World",
}

renders["nightrender"] = {
    "world": "My world",
    "rendermode": "night",
    "title": "Night Render of My World",
}

renders["netherrender"] = {
    "world": "My world",
    "dimension": "nether",
    "rendermode": "nether_lighting",
    "title": "Nether Render of My World",
}

renders["nethercaverender"] = {
    "world": "My world",
    "dimension": "nether",
    "rendermode": "cave",
    "title": "Nether Cave Render of My World",
}



outputdir = "/var/www/overviewer-140320"

def playerIcons(poi):
    if poi['id'] == 'Player':
        poi['icon'] = "http://overviewer.org/avatar/%s" % poi['EntityId']
        return "Last known location for %s" % poi['EntityId']
