# 10 major cities are listed below
# import City.py to create City objects

if __name__ == '__main__':

    from City import City

    print('\nRetrieving coordinates of cities....\n')
    KualaLumpur = City('Kuala Lumpur','Malaysia','Kuala Lumpur International Airport','KUL',0,0)
    Chengdu = City('Chengdu','China','Chengdu Shuangliu International Airport','CTU',0,0)
    Delhi = City('Delhi','India','Indira Gandhi International Airport','VIDP',0,0)
    Moscow = City('Moscow','Russia','Sheremetyevo International Airport','SVO',0,0)
    Istanbul = City('Istanbul','Turkey','Istanbul Ataturk Airport','ISL',0,0)
    Berlin = City('Berlin','Germany','Berlin Tegel Airport','TXL',0,0)
    London = City('London','England','Gatwick Airport','LGW',0,0)
    Toronto = City('Toronto','Canada','Toronto Pearson International Airport','YYZ',0,0)
    Los_Angeles = City('Los Angeles','USA','Los Angeles International Airport','LAX',0,0)
    Keflavík = City('Keflavík','Iceland','Keflavík International Airport','BIKF',0,0)




    city = [KualaLumpur,Chengdu,Delhi,Moscow,Istanbul,Berlin,London,Toronto,Los_Angeles,Keflavík]
    latitude_list =[]
    longitude_list =[]

    #retrieve coordinate(latitude, longitude) for each city airport from Geopy
    from geopy.geocoders import Nominatim
    geolocator = Nominatim(user_agent="specify_your_app_name_here")

    # for each city retrieve latitude and longitude and save it to City Object
    for city in city:
        location = geolocator.geocode(city.IATAcode)
        city.latitude = location.latitude
        city.longitude = location.longitude
        city.printCoordinate()
        latitude_list.append(city.latitude)
        longitude_list.append(city.longitude)


    from geopy import distance

    KLCoordinate =(KualaLumpur.latitude,KualaLumpur.longitude)
    ChengduCoordinate = (Chengdu.latitude,Chengdu.longitude)
    DelhiCoordinate = (Delhi.latitude,Delhi.longitude)
    MoscowCoordinate = (Moscow.latitude,Moscow.longitude)
    IstanbulCoordinate = (Istanbul.latitude,Istanbul.longitude)
    BerlinCoordinate = (Berlin.latitude,Berlin.longitude)
    LondonCoordinate = (London.latitude,London.longitude)
    TorontoCoordinate = (Toronto.latitude,Toronto.longitude)
    Los_AngelesCoordinate = (Los_Angeles.latitude,Los_Angeles.longitude)
    KeflavíkCoordinate = (Keflavík.latitude,Keflavík.longitude)

    # getCoordinate works like a switch statement in programming languages
    # no switch statement in python
    def getCoordinate(x):
        return {
            'KualaLumpur': KLCoordinate,
            'Chengdu': ChengduCoordinate,
            'Delhi': DelhiCoordinate,
            'Moscow': MoscowCoordinate,
            'Istanbul': IstanbulCoordinate,
            'Berlin': BerlinCoordinate,
            'London': LondonCoordinate,
            'Toronto': TorontoCoordinate,
            'LosAngeles': Los_AngelesCoordinate,
            'Keflavik': KeflavíkCoordinate
        }[x]


    import findpath
    graph = findpath.Graph()
    edges = [
        ('KualaLumpur', 'Chengdu', distance.distance(KLCoordinate, ChengduCoordinate).km),
        ('KualaLumpur', 'Delhi', distance.distance(KLCoordinate, DelhiCoordinate).km),
        ('Chengdu', 'Moscow', distance.distance(ChengduCoordinate, MoscowCoordinate).km),
        ('Chengdu', 'Istanbul', distance.distance(ChengduCoordinate, IstanbulCoordinate).km),
        ('Delhi', 'Moscow', distance.distance(DelhiCoordinate, MoscowCoordinate).km),
        ('Delhi', 'Istanbul', distance.distance(DelhiCoordinate, IstanbulCoordinate).km),
        ('Moscow', 'Berlin', distance.distance(MoscowCoordinate, BerlinCoordinate).km),
        ('Moscow', 'London', distance.distance(MoscowCoordinate, LondonCoordinate).km),
        ('Istanbul', 'Berlin', distance.distance(IstanbulCoordinate, BerlinCoordinate).km),
        ('Istanbul', 'London', distance.distance(IstanbulCoordinate, LondonCoordinate).km),
        ('Berlin', 'Toronto', distance.distance(BerlinCoordinate, TorontoCoordinate).km),
        ('Berlin', 'LosAngeles', distance.distance(BerlinCoordinate, Los_AngelesCoordinate).km),
        ('Berlin', 'Keflavik', distance.distance(BerlinCoordinate, KeflavíkCoordinate).km),
        ('London', 'Toronto', distance.distance(LondonCoordinate, TorontoCoordinate).km),
        ('London', 'LosAngeles', distance.distance(LondonCoordinate, Los_AngelesCoordinate).km),
        ('London', 'Keflavik', distance.distance(LondonCoordinate, KeflavíkCoordinate).km)

    ]

    # the special syntax * in *edge is used to pass a variable number of arguments to a function
    # it allows to take more arguments in than the number of formal arguments previously defined
    for edge in edges:
        graph.add_edge(*edge)


    destination = input("\nChoose your destination: Toronto , LosAngeles, Keflavik. "
                   "\nReminder: Type exactly as the options as well as case sensitive")

    while(destination!='Toronto'and destination!='LosAngeles' and destination!='Keflavik'):
        destination = input("Please reenter your destination: Toronto , LosAngeles, Keflavik. "
                   "\nReminder: Type exactly as the options as well as case sensitive\n\n")
    else:
        # calculate shortest path
        print('The shortest path from Kuala Lumpur to '+destination +' is:')
        shortestPath = findpath.dijsktra(graph, 'KualaLumpur', destination)
        minDist=0
        for y in range(len(shortestPath)-1):
            minDist += distance.distance(getCoordinate(shortestPath[y]), getCoordinate(shortestPath[y + 1])).km
        print('The shortest path distance is '+str(minDist)+'km')


    shortestLatitudeList =[]
    shortestLongitudeList =[]

    for path in shortestPath:
        if(path=='KualaLumpur'):
            shortestLatitudeList.append(KualaLumpur.latitude)
            shortestLongitudeList.append(KualaLumpur.longitude)
        elif(path=='Chengdu'):
            shortestLatitudeList.append(Chengdu.latitude)
            shortestLongitudeList.append(Chengdu.longitude)
        elif (path == 'Delhi'):
            shortestLatitudeList.append(Delhi.latitude)
            shortestLongitudeList.append(Delhi.longitude)
        elif (path == 'Moscow'):
            shortestLatitudeList.append(Moscow.latitude)
            shortestLongitudeList.append(Moscow.longitude)
        elif (path == 'Istanbul'):
            shortestLatitudeList.append(Istanbul.latitude)
            shortestLongitudeList.append(Istanbul.longitude)
        elif (path == 'Berlin'):
            shortestLatitudeList.append(Berlin.latitude)
            shortestLongitudeList.append(Berlin.longitude)
        elif (path == 'London'):
            shortestLatitudeList.append(London.latitude)
            shortestLongitudeList.append(London.longitude)
        elif (path == 'Toronto'):
            shortestLatitudeList.append(Toronto.latitude)
            shortestLongitudeList.append(Toronto.longitude)
        elif (path == 'LosAngeles'):
            shortestLatitudeList.append(Los_Angeles.latitude)
            shortestLongitudeList.append(Los_Angeles.longitude)
        else:
            shortestLatitudeList.append(Keflavík.latitude)
            shortestLongitudeList.append(Keflavík.longitude)


    # import gmplot package
    import gmplot
    # Place map
    # First two arugments are the geogrphical coordinates .i.e. Latitude and Longitude
    #and the zoom resolution.
    # first map contains all the cities
    gmap1 = gmplot.GoogleMapPlotter(London.latitude, London.longitude, 2)
    gmap1.apikey = "AIzaSyBUgGrFXal2X2CtObxO1sGN49EsJPN8r9g"
    gmap1.heatmap( latitude_list, longitude_list )
    gmap1.draw("citiesMap.html")

    # second map contains path with minimum distance calculated using dijkstra algorithm
    gmap2 = gmplot.GoogleMapPlotter(London.latitude, London.longitude, 2)
    gmap2.heatmap(shortestLatitudeList, shortestLongitudeList)
    gmap2.apikey = "AIzaSyDU_zxVWF4NKQU4sH-wYn2BXi_KJsibu0Q"
    gmap2.plot(shortestLatitudeList, shortestLongitudeList,  'cornflowerblue', edge_width = 2.5)
    gmap2.draw("shortestPathMap.html")



    # open the html map automatically in web browser
    import webbrowser, os
    webbrowser.open('file://' + os.path.realpath("citiesMap.html"))
    webbrowser.open('file://' + os.path.realpath("shortestPathMap.html"))
    print('\nProcessing political sentiment for countries....\n')

    # multiprocessing to calculate political sentiment for each country
    # # calculate word count
    import multiprocessing
    from multiprocessing import Process
    import time,wordcount

    jobs = []
    frequencyDelhi = wordcount.CityWordFreq()
    frequencyChengdu = wordcount.CityWordFreq()
    frequencyLondon = wordcount.CityWordFreq()
    frequencyMoscow = wordcount.CityWordFreq()
    frequencyIstanbul = wordcount.CityWordFreq()
    frequencyBerlin = wordcount.CityWordFreq()

    manager = multiprocessing.Manager()
    mystoplist = manager.dict()
    positivelist = manager.dict()
    negativelist = manager.dict()
    politicalList = manager.dict()

    for news in wordcount.newsList:
        process= Process(target=wordcount.testThread, args=(news, mystoplist, positivelist, negativelist, politicalList))
        jobs.append(process)

    # Start the threads
    for j in jobs:
        j.start()
        time.sleep(1)

    # Ensure all of the threads have finished
    for j in jobs:
        j.join()


    # to get all nodes to the destination
    print("Following are all different paths from %s to %s :" % ('KualaLumpur', destination))
    allpath = findpath.find_all_paths(dict(graph.edges), 'KualaLumpur', destination)

    # calculate probability distrivution for every possible paths
    probability =[]
    total=0
    for paths in allpath:
        # dist to save total distance between nodes in each path
        dist = 0
        political=0
        for y in range(len(paths)-1):
            dist += distance.distance(getCoordinate(paths[y]), getCoordinate(paths[y+1])).km
            # if a location in path contains computed political sentiment, add it into political variable
            if(paths[y] in politicalList):
                political+=politicalList[paths[y]]
        # x compute the probability value for each path which will be used to calculate probability
        x=political/dist
        total+=x
        probability.append(x)

    maxIndex=0
    maxProb=0
    for i in range(len(allpath)):

        prob=probability[i]/total
        if (i == 0):
            maxProb=prob
        print(str(allpath[i])+' Probability: '+str(prob))
        if((probability[i]/total)>maxProb):
            maxIndex=i
            maxProb=prob

    print('\nThe recommended path is '+str(allpath[maxIndex])+' Probability: '+str(maxProb))

    recommendedLatitudeList=[]
    recommendedLongitudeList = []
    for path in allpath[maxIndex]:
        if(path=='KualaLumpur'):
            recommendedLatitudeList.append(KualaLumpur.latitude)
            recommendedLongitudeList.append(KualaLumpur.longitude)
        elif(path=='Chengdu'):
            recommendedLatitudeList.append(Chengdu.latitude)
            recommendedLongitudeList.append(Chengdu.longitude)
        elif (path == 'Delhi'):
            recommendedLatitudeList.append(Delhi.latitude)
            recommendedLongitudeList.append(Delhi.longitude)
        elif (path == 'Moscow'):
            recommendedLatitudeList.append(Moscow.latitude)
            recommendedLongitudeList.append(Moscow.longitude)
        elif (path == 'Istanbul'):
            recommendedLatitudeList.append(Istanbul.latitude)
            recommendedLongitudeList.append(Istanbul.longitude)
        elif (path == 'Berlin'):
            recommendedLatitudeList.append(Berlin.latitude)
            recommendedLongitudeList.append(Berlin.longitude)
        elif (path == 'London'):
            recommendedLatitudeList.append(London.latitude)
            recommendedLongitudeList.append(London.longitude)
        elif (path == 'Toronto'):
            recommendedLatitudeList.append(Toronto.latitude)
            recommendedLongitudeList.append(Toronto.longitude)
        elif (path == 'LosAngeles'):
            recommendedLatitudeList.append(Los_Angeles.latitude)
            recommendedLongitudeList.append(Los_Angeles.longitude)
        else:
            recommendedLatitudeList.append(Keflavík.latitude)
            recommendedLongitudeList.append(Keflavík.longitude)

    # plot map for recommended path
    gmap3 = gmplot.GoogleMapPlotter(London.latitude, London.longitude, 2)
    gmap3.heatmap(recommendedLatitudeList, recommendedLongitudeList)
    gmap3.apikey = "AIzaSyDU_zxVWF4NKQU4sH-wYn2BXi_KJsibu0Q"
    gmap3.plot(recommendedLatitudeList, recommendedLongitudeList, 'cornflowerblue', edge_width=2.5)
    gmap3.draw("recommendedPathMap.html")
    webbrowser.open('file://' + os.path.realpath("recommendedPathMap.html"))



    # plot graphs
    import plotly
    import plotly.graph_objs as go

    plotly.tools.set_credentials_file(username='devilng05108', api_key='QW8bkaovMEl5V8hfXZny')

    x = ['Chengdu', 'Delhi', 'Moscow', 'Istanbul', 'Berlin', 'London']
    y = [mystoplist['Chengdu'], mystoplist['Delhi'], mystoplist['Moscow'], mystoplist['Istanbul'], mystoplist['Berlin'],
         mystoplist['London']]
    y2 = [positivelist['Chengdu'], positivelist['Delhi'], positivelist['Moscow'], positivelist['Istanbul'],
          positivelist['Berlin'], positivelist['London']]
    y3 = [negativelist['Chengdu'], negativelist['Delhi'], negativelist['Moscow'], negativelist['Istanbul'],
          negativelist['Berlin'], negativelist['London']]
    y4= [politicalList['Chengdu'], politicalList['Delhi'], politicalList['Moscow'], politicalList['Istanbul'],
          politicalList['Berlin'], politicalList['London']]

    trace1 = go.Bar(
        x=x,
        y=y,
        text=y,
        textposition='auto',
        name='Stop words count',
        marker=dict(
            color='rgb(158,202,225)',
            line=dict(
                color='rgb(8,48,107)',
                width=1.5),
        ),
        opacity=0.6
    )

    trace2 = go.Bar(
        x=x,
        y=y2,
        text=y2,
        textposition='auto',
        name='Positive words count',
        marker=dict(
            color='rgb(58,200,225)',
            line=dict(
                color='rgb(8,48,107)',
                width=1.5),
        ),
        opacity=0.6
    )

    trace3 = go.Bar(
        x=x,
        y=y3,
        text=y3,
        textposition='auto',
        name='Negative words count',
        marker=dict(
            color='rgb(200,58,58)',
            line=dict(
                color='rgb(8,48,107)',
                width=1.5),
        ),
        opacity=0.6
    )

    trace4 = go.Bar(
        x=x,
        y=y4,
        text=y4,
        textposition='auto',
        name='Political sentiment value',
        marker=dict(
            color='rgb(20,255,58)',
            line=dict(
                color='rgb(8,48,107)',
                width=1.5),
        ),
        opacity=0.6
    )

    # plot graph for positive and negative count
    data = [trace2, trace3]
    # plot graph for stop words count
    data2 = [trace1]
    #plot graph for political sentiment value
    data3 = [trace4]
    layout = go.Layout(
        title='Stop words count for countries',
    )
    layout2 = go.Layout(
        title='Political sentiment value for countries',
    )
    fig = go.Figure(data=data2, layout=layout)
    fig2 = go.Figure(data=data3, layout=layout2)
    plotly.offline.plot(data, filename='positivenegativewordcount.html')
    plotly.offline.plot(fig, filename='stopwordcount.html')
    plotly.offline.plot(fig2, filename='politicalsentiment.html')

