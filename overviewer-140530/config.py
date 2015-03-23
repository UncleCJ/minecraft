
#overviewer.py  --rendermodes=smooth_lighting,cave ~/opt/minecraft_server/tutworld /var/www/overviewer-140319
#texturepath = "/usr/share/mapcrafter/textures/"
#texturepath = "/mnt/data/home/cj/.minecraft"
texturepath = "/home/cj/.minecraft/versions/1.7.9/1.7.9.jar"

worlds["Our world"] = "~minecraft/craftbukkit/tutworld"
worlds["Our world nether"] = "~minecraft/craftbukkit/tutworld_nether"
worlds["From Flames"] = "~minecraft/craftbukkit/fromflames"
worlds["From Ashes"] = "~minecraft/craftbukkit/fromashes"
worlds["City World"] = "~minecraft/craftbukkit/cityworld"
worlds["Creative"] = "~minecraft/craftbukkit/creative"

renders["normalrender"] = {
    "world": "Our world",
    "title": "Our World",
    # "markers": "foobar",
}
renders["caverender"] = {
    "world": "Our world",
    "rendermode": "cave",
    "title": "Cave Render of our world",
}
renders["nightrender"] = {
    "world": "Our world",
    "rendermode": "night",
    "title": "Night Render of our world",
}

renders["netherrender"] = {
    "world": "Our world nether",
    "dimension": "nether",
    "rendermode": "nether_lighting",
    "title": "Our Nether world",
}
renders["nethercaverender"] = {
    "world": "Our world nether",
    "dimension": "nether",
    "rendermode": "cave",
    "title": "Cave render of Our Nether World"
}

renders["fromflamesrender"] = {
    "world": "From Flames",
    "title": "From Flames",
}
renders["fromflamescaverender"] = {
    "world": "From Flames",
    "title": "Cave Render of From Flames",
    "rendermode": "cave",
}
renders["fromflamesnightrender"] = {
    "world": "From Flames",
    "rendermode": "night",
    "title": "Night render of From Flames",
}

renders["fromashesrender"] = {
    "world": "From Ashes",
    "title": "From Ashes",
}
renders["fromashescaverender"] = {
    "world": "From Ashes",
    "title": "Cave Render of From Ashes",
    "rendermode": "cave",
}
renders["fromflamesnightrender"] = {
    "world": "From Flames",
    "rendermode": "night",
    "title": "Night render of From Flames",
}
renders["cityworldrender"] = {
    "world": "City World",
    "title": "City World by Rulle & Juko",
    # "markers": "foobar",
}

renders["creativerender"] = {
    "world": "Creative",
    "title": "Creative",
}


outputdir = "/var/www/html/overviewer-140530"

def playerIcons(poi):
    if poi['id'] == 'Player':
        poi['icon'] = "http://overviewer.org/avatar/%s" % poi['EntityId']
        return "Last known location for %s" % poi['EntityId']
