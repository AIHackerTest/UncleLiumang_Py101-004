# -*- coding: utf-8 -*-


from flask import Flask, render_template
from flask import request
import json
import requests

app = Flask(__name__)
my_search_list=[]

def search_help():
    message = []
    message.append( 'Input the name of city, and you\'ll know the newest weather.')
    return message

def fetch_weather(location):
    result = requests.get('https://api.seniverse.com/v3/weather/daily.json', params={
            'key': '3hpzcfzavrreebzh',
            'location': location,
            'language': 'zh-Hans',
            'unit': 'c'
        }, timeout=20)
    return result.json()

def show_weather(result):
    message = []
    try:
        result = result['results'][0]['daily']
        for i in range(0,len(result)): #返回好几天天气，list形式
            now = result[i]
            date = now['date']
            weather_day = now['text_day']
            #weather_night = now['text_night']
            low = now['low']
            high = now['high']
            message.append('日期：'+date + ' 天气：'+weather_day + ' 温度：'+low +' to ' + high)
    except KeyError: #报错处理
        problem_reason = result['status']
        message.append(problem_reason)
    return message

@app.route('/', methods=['POST','GET'])
def search_weather():
    message = []
    if request.method == 'POST':
        if request.form['action'] == u'帮助':
            message = search_help()
        elif request.form['action'] == u'记录':
            message = my_search_list
        else:
            my_search = request.form['city']
            result = fetch_weather(my_search)
            message = show_weather(result)
            my_search_list.append(my_search +'天气'+ message[0])
    return render_template('home.html', message = message )

if __name__ == '__main__':
    app.run(debug=True)
