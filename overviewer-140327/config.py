
#overviewer.py  --rendermodes=smooth_lighting,cave ~/opt/minecraft_server/tutworld /var/www/overviewer-140319

worlds["Our world"] = "~/opt/minecraft_server/tutworld"

renders["normalrender"] = {
    "world": "Our world",
    "title": "Normal Render of CJ, Jenny & Co - WeKnow World 1",
    # "markers": "foobar",
}

renders["caverender"] = {
    "world": "Our world",
    "rendermode": "cave",
    "title": "Cave Render of CJ, Jenny & Co - WeKnow World 1",
}

renders["nightrender"] = {
    "world": "Our world",
    "rendermode": "night",
    "title": "Night Render of CJ, Jenny & Co - WeKnow World 1",
}

renders["netherrender"] = {
    "world": "Our world",
    "dimension": "nether",
    "rendermode": "nether_lighting",
    "title": "Nether Render of CJ, Jenny & Co - WeKnow World 1",
}

renders["nethercaverender"] = {
    "world": "Our world",
    "dimension": "nether",
    "rendermode": "cave",
    "title": "Nether Cave Render of CJ, Jenny & Co - WeKnow World 1",
}



outputdir = "/var/www/overviewer-140504"

def playerIcons(poi):
    if poi['id'] == 'Player':
        poi['icon'] = "http://overviewer.org/avatar/%s" % poi['EntityId']
        return "Last known location for %s" % poi['EntityId']
