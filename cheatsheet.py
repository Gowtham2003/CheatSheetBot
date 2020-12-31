import requests
import re

BASE_URL = "http://cht.sh/"

# def learn(language):
    # r = requests.get(BASE_URL+ language+"/:learn?QT")
    # return r.text

def querySh(language,query):
    r = requests.get(BASE_URL+language+"/"+query +"?QT")
    return r.text

