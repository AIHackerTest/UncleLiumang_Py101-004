# -*- coding: utf-8 -*-

import requests
import json


def fetch_weather(location):
    result = requests.get('https://api.seniverse.com/v3/weather/daily.json', params={
            'key': '3hpzcfzavrreebzh',
            'location': location,
            'language': 'zh-Hans',
            'unit': 'c'
        }, timeout=20)
    return result.json()

'''
print json.dumps(weather_day, ensure_ascii=False)
'''

def show_weather(result):
    try:
        result = result['results'][0]['daily']
        for i in range(0,len(result)): #返回好几天天气，list形式
            now = result[i]
            date = now['date']
            weather_day = now['text_day']
            weather_night = now['text_night']
            low = now['low']
            high = now['high']

            print 'Date:',date
            print 'weather in the day:',weather_day
            print 'weather in the night:', weather_night
            print 'temperature range:',low, 'to',high
            print '\n'

    except KeyError: #报错处理
        problem_reason = result['status']
        print problem_reason,'\n'

def search_help():
    print 'input the name of city, and you\'ll know the newest weather.'

my_search_list=[]
while True:
    my_search = raw_input('entre the city you want to know the weather: \n (\'h\'for help,\'q\'for quit) \n')

    if my_search == 'h':
        search_help()
    elif my_search == 'q':
        print 'You have searched ', len(my_search_list) ,'cities. They are :'
        for item in my_search_list:
            print item,
        print '\nSee you later!'
        exit()
    else:
        my_search_list.append(my_search)
        print 'The weather in %s is:'%my_search
        result = fetch_weather(my_search)
        show_weather(result)
