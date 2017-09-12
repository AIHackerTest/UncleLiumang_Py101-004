#-*-encoding:utf-8-*-

def search_weather(my_search):
    if my_search in city_weather:
        print (city_weather[my_search])
    else:
        print('There is no weather data about %s' % my_search)

def search_help():
    print ('which city do you like, just try it! For example 北京.\n Now is only including city in China, we will expand more later~')

city_weather = {}
my_search_list = []
with open('weather_info.txt','r') as f:
    for line in f.readlines():
        line = line.rstrip('\n')    #去掉换行
        #print (line)
        weather_data = line.split(',')
        #print (weather_data)
        city_weather[weather_data[0]] = weather_data [1]
        #print (city_weather[weather_data[0]])

while True:
    my_search = input('entre the city you want to know the weather: \n (\'h\'for help,\'q\'for quit) \n')

    if my_search == 'h':
        search_help()
    elif my_search == 'q':
        print ('You have searched ', len(my_search_list) ,'cities. They are :', my_search_list )
        print ('See you later!')
        exit()
    else:
        my_search_list.append(my_search)
        search_weather(my_search)
