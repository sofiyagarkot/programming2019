import folium
from tqdm import tqdm
import geocoder

def read_file(path):
    ''' (str) -> list[tuple(str,str,str)]
    Reads the file and returns the list of tuples. Each tuple contains string, that are : name of film,
    year it was made and location.
    '''
    f = open(path,encoding = "ISO-8859-1")
    lines = f.readlines()
    res = []
    lines = lines[14:]
    for line in lines:
        new = line.split("\t")
        if new[-1].startswith("("):
            res.append((new[0].split("(")[0][1:-2],new[0].split("(")[1][:4],new[-2]))
        else:
            try:
                res.append((new[0].split("(")[0][1:-2],new[0].split("(")[1][:4], new[-1][:-1]))
            except:
                continue
    f.close()
    return res


def number_generator(lst):
    ''' (list[tuple(str,str)]) -> dictionary
    Returns dictionary, where keys are locations (last element of the tuple) and values are numbers of films,
    that were filmed on this location.
    '''
    dct = {}
    i=0
    for tup in tqdm(lst):
        if i <= 1000:
            if tup[-1] not in dct.keys():
                dct[tup[-1]] = 1
            else:
                dct[tup[-1]] += 1
        i+=1
    return dct



def color_creator(number):
    '''(int) -> str
    Returns colour depending on number.
    >>> color_creator(3)
    'green'
    '''
    if number < 5:
        return "green"
    elif 5 <= number <= 20:
        return "yellow"
    else:
        return "red"


def map_population(json_file):
    '''(str) -> folium.map.FeatureGroup
    Returns new layer of the map depending on the data given in json file.
    '''
    fg_pp = folium.FeatureGroup(name="Population")
    fg_pp.add_child(folium.GeoJson(data=open(json_file, 'r',
                                             encoding='utf-8-sig').read(),
                                   style_function=lambda x: {'fillColor': 'green'
                                   if x['properties']['POP2005'] < 10000000
                                   else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000
                                   else 'red'}))
    return(fg_pp)

def marker_film_location(lst):
    ''' (list[tuple(str,str,str)]) -> folium.map.FeatureGroup
    Returns new layer of the map, that is locations of the movies, filmed in some year, that user has typed.
    '''
    fg_film = folium.FeatureGroup(name="Films")
    i = 0
    while i < 5:
        try:
            user_wish = int(input("Enter a year, you want films to be displayed on the map : "))
            break
        except:
            i+=1
    user_wish = str(user_wish)
    def detect(tup):
        return tup[1] == user_wish

    res1 = list(filter(detect, lst))
    if len(res1) > 500:
        res1 = res1[:500]
    index_of_location = 0
    for point in tqdm(list(t[-1] for t in res1)):
        location = geocoder.arcgis(point).latlng
        if location:
            fg_film.add_child(folium.Marker(location=location, popup=res1[index_of_location][0], icon=folium.Icon()))
        index_of_location += 1
    return(fg_film)


def point_film(dct):
    '''(dictionary) -> folium.map.FeatureGroup
    Returns a new layer of the map. There are circle markerson it, coloured in different colours, depending on number
    of movies(values), that were filmed in current location(keys).
    '''
    fg_num = folium.FeatureGroup(name="Numbers")
    for key in tqdm(dct.keys()):
        location = geocoder.arcgis(key).latlng
        if location:
            fg_num.add_child(folium.CircleMarker(location=location,
                                                 radius=10,
                                                 popup=str(dct.get(key)),
                                                 fill_color=color_creator(dct.get(key)),
                                                 color='red',
                                                 fill_opacity=0.5))
    return(fg_num)

if __name__ == "__main__":
    map = folium.Map(location=[46.8, 8.33])
    map.add_child(map_population("world.json"))
    map.add_child(marker_film_location(read_file("locations.list")))
    map.add_child(point_film(number_generator(read_file("locations.list"))))
    map.add_child(folium.LayerControl())
    map.save("Sofia.html")