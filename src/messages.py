#!/usr/bin/python

# Forms posts for the stoned denver clock

from __future__ import print_function

import random
import datetime
import pytz


randomness_laughs = 0.1
randomness_lotsa_laughs = 0.04
randomness_video = 0.04

laughs = ['ha','ha!','haha','haha!','heh','Ha!','hehe','ha ha!','hehehe']
videos = [
    ('So AMAZING!!!','https://www.youtube.com/watch?v=wOaXTg3nAuY'), # Dead Touch of Grey
    ("Let's get funky!!",'https://www.youtube.com/watch?v=XacvydVrhuI'), # Dead Friend of the Devil
    ('OMG so awesome','https://www.youtube.com/watch?v=pafY6sZt0FE'), # Dead Truckin
    ('The hour is totally getting late:', 'https://www.youtube.com/watch?v=TLV4_xaYynY'), # Hendrix Watchtower
    ('Excuse me while I kiss this guy.', 'https://www.youtube.com/watch?v=fjwWjx7Cw8I'), # Hendrix Purple Haze
    ('Trippy:','https://www.youtube.com/watch?v=17GLE-16_3g'), # Dave Matthews Ants Marching 4 guys
    ("I'm not goin anywhere. I'm a tower. Where you goin?",'https://www.youtube.com/watch?v=qjykrjAS5bQ'), # Dave Matthews Where are you Going
    ('This is just amazing!! OMG Aamazing!','https://www.youtube.com/watch?v=URTq-94fZ6w'), # Dave Matthews Two Step
    ("I'm watching Watchtower... I'm watching it and I'm a tower. I'm a watching tower!",'https://www.youtube.com/watch?v=fOaMQ-R9YGM'), # Dave Matthews Watchtower
    ('OMG so awesome!! You need to watch this!','https://www.youtube.com/watch?v=9K5JHT1iMZ0') # Dave Matthews Jimi Thing
    # Need to add Phish.
]


def get_denver_hour():
    """
    Return the hour in mountain time.
    """
    mountain = pytz.timezone('US/Mountain')
    hour = long(datetime.datetime.now(mountain).strftime('%H')) % 12
    if hour == 0:
        hour = 12
    return hour


def standard_message():
    """
    Create the standard 'BONG BONG ... BONG' message.
    """
    return ' '.join(['BONG' for i in range(get_denver_hour())])


def random_laugh():
    """
    Generates a laugh at random or returns an empty string.
    """
    if random.random() < randomness_laughs:
        return ' ' + laughs[random.randrange(0,len(laughs))]
    else:
        return ''


def message_with_laughs():
    """
    Inserts random laughs into a message.
    """
    return ' '.join([m + random_laugh() for m in standard_message().split()])
    

def message_with_lotsa_laughs():
    """
    Make a post with mostly laughs.
    """
    return 'BONG ' + ' '.join([laughs[random.randrange(0,len(laughs))] for i in range(random.randint(6,14))])


def message_with_video():
    """
    Make a post with a video.
    """
    video = videos[random.randint(0,len(videos)-1)]
    return '%s %s' % (video[0], video[1])


def make_message():
    """
    Creates a message for a Twitter post.
    """
    if random.random() < randomness_lotsa_laughs:
        msg = message_with_lotsa_laughs()
    else:
        msg = message_with_laughs()
    print("message for tweet: %s" % msg)
    return msg



