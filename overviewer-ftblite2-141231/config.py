
#overviewer.py  --rendermodes=smooth_lighting,cave ~/opt/minecraft_server/tutworld /var/www/overviewer-140319
#texturepath = "/usr/share/mapcrafter/textures/"
#texturepath = "/mnt/data/home/cj/.minecraft"
texturepath = "/home/cj/.minecraft/versions/1.7.9/1.7.9.jar"
outputdir = "/var/www/html/overviewer-ftblite2-141231"

worlds["Our world"] = "~minecraft/ssd/ftblite2/Kastanj"
#worlds["Our world nether"] = "~minecraft/craftbukkit/tutworld_nether"
#worlds["From Flames"] = "~minecraft/craftbukkit/fromflames"
#worlds["From Ashes"] = "~minecraft/craftbukkit/fromashes"
#worlds["City World"] = "~minecraft/craftbukkit/cityworld"
#worlds["Creative"] = "~minecraft/craftbukkit/creative"

def signFilter(poi):
    if poi['id'] == 'Sign':
        return "\n".join([poi['Text1'], poi['Text2'], poi['Text3'], poi['Text4']])

def chestFilter(poi):
    if poi['id'] == "Chest":
        return ("Chest", "Chest with %d items" % len(poi['Items']))

def townFilter(poi):
    if poi['id'] == 'Town':
        try:
            return (poi['name'], poi['description'])
        except KeyError:
            return poi['name'] + '\n'

def playerIcons(poi):
    if poi['id'] == 'Player':
        poi['icon'] = "http://overviewer.org/avatar/%s" % poi['EntityId']
        return "Last known location for %s" % poi['EntityId']

#rendersfoo['myrender'] = {
#    'world':'myworld',
#    'title':'Example',
#    'manualpois':[
#                   {'id':'Town',
#                    'x':200,
#                    'y':64,
#                    'z':200,
#                    'name':'Foo'},
#                   {'id':'Town',
#                    'x':-300,
#                    'y':85,
#                    'z':-234,
#                    'name':'Bar'}],
#    'markers': [dict(name="Towns", filterFunction=townFilter)],
#}

#rendersbar['myrender'] = {
#    'world':'myworld',
#    'title':'Example',
#    'manualpois':[
#                   {'id':'Town',
#                    'x':200,
#                    'y':64,
#                    'z':200,
#                    'name':'Foo',
#                    'description':'Best place to eat hamburgers'},
#                   {'id':'Town',
#                    'x':-300,
#                    'y':85,
#                    'z':-234,
#                    'name':'Bar'}],
#    'markers': [dict(name="Towns", filterFunction=townFilter, icon="icons/marker_town.png")],
#    ### Note: The 'icon' parameter allows you to specify a custom icon, as per
#    ###       standard markers. This icon must exist in the same folder as your
#    ###       custom webassets or in the same folder as the generated index.html
#    ###       in this case, we use the marker_town.png icon which comes with
#    ###       the Overviewer by default, located in a subdirectory of web_assets.
#}


#renderscar['myrender'] = {
#        'world': 'myworld',
#        'title': "Example",
#        'markers': [dict(name="All signs", filterFunction=signFilter),
#                    dict(name="Chests", filterFunction=chestFilter, icon="chest.png", createInfoWindow=False)]
#}

renders["normalrender"] = {
    "world": "Our world",
    "title": "Our World",
    "markers": [dict(name="Chests", filterFunction=chestFilter),
                dict(name="All signs", filterFunction=signFilter),
                dict(name="Players", filterFunction=playerIcons)]
}

renders["caverender"] = {
    "world": "Our world",
    "rendermode": "cave",
    "title": "Cave Render of our world",
    "markers": [dict(name="Chests", filterFunction=chestFilter),
		dict(name="All signs", filterFunction=signFilter)]
}
#renders["nightrender"] = {
#    "world": "Our world",
#    "rendermode": "night",
#    "title": "Night Render of our world",
#}

#renders["netherrender"] = {
#    "world": "Our world nether",
#    "dimension": "nether",
#    "rendermode": "nether_lighting",
#    "title": "Our Nether world",
#}
#renders["nethercaverender"] = {
#    "world": "Our world nether",
#    "dimension": "nether",
#    "rendermode": "cave",
#    "title": "Cave render of Our Nether World"
#}

#renders["fromflamesrender"] = {
#    "world": "From Flames",
#    "title": "From Flames",
#}
#renders["fromflamescaverender"] = {
#    "world": "From Flames",
#    "title": "Cave Render of From Flames",
#    "rendermode": "cave",
#}
#renders["fromflamesnightrender"] = {
#    "world": "From Flames",
#    "rendermode": "night",
#    "title": "Night render of From Flames",
#}

#renders["fromashesrender"] = {
#    "world": "From Ashes",
#    "title": "From Ashes",
#}
#renders["fromashescaverender"] = {
#    "world": "From Ashes",
#    "title": "Cave Render of From Ashes",
#    "rendermode": "cave",
#}
#renders["fromflamesnightrender"] = {
#    "world": "From Flames",
#    "rendermode": "night",
#    "title": "Night render of From Flames",
#}
#renders["cityworldrender"] = {
#    "world": "City World",
#    "title": "City World by Rulle & Juko",
#    # "markers": "foobar",
#}

#renders["creativerender"] = {
#    "world": "Creative",
#    "title": "Creative",
#}

