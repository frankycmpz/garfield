# franky campuzano
# garfield bot tweet generator
# may 29 2020
# all rights reserved

import random
from urllib.error import HTTPError
from urllib.request import urlretrieve
import urllib.request
import tweepy

#garfield account keys

# **** input account keys here ****


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def urlGenerator():
    prefix = "/media/franky/FDRIVE/garfield_"
    suffix = ".gif"


    #date generator


    #rather than use a built-in date generator, i made my own to account for the weird range in dates
    year = random.randint(1978,2020)


    month = 0
    if year == 1978:
        month = random.randint(7,12)
    elif year == 2020:
        month = random.randint(1,6)
    else: month = random.randint(1,12)

    day = 0
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        day = random.randint(1,31)
    elif month == 4 or month == 6 or month == 9 or month == 11:
        day = random.randint(1,30)
    elif year % 4 == 0:
        day = random.randint(1,29)
    else: day = random.randint(1,28)

    '''


    #specific date input, if you feel like not being random today
    month = 2
    day = 14
    year = 2018

    '''

    url = ""
    url = prefix + url + str(year)+"/garfield"+str(year)

    if day > 9 and month > 9:
        url = url +"-"+str(month)+"-"+str(day)
    elif day > 9 and month < 10:
        url = url +"-0"+str(month)+"-"+str(day)
    elif day < 10 and month < 10:
        url = url +"-0"+str(month)+"-0"+str(day)
    elif day < 10 and month > 9:
        url = url +"-"+str(month)+"-0"+str(day)

    url = url + suffix
    print(url)
    content = [url, month,day, year]
    return content

def statusText(content):
    text = "garfield "+ str(content[1])+"."+ str(content[2])+"."+ str(content[3])
    return text

def tweet():

    content = urlGenerator()

    media_ids = []

    res = api.media_upload(content[0])
    media_ids.append(res.media_id)

    text = statusText(content)

    api.update_status(text, media_ids=media_ids)



if __name__ == '__main__':
    tweet()