from flask import Flask, render_template
import urllib, json
from datetime import datetime
now = datetime. now(). time()
print("now =", now)
print("type(now) =", type(now))

def card():
    u = urllib.request.urlopen('https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1')
    response = u.read()
    data = json.loads(response)
    print(data['deck_id'])

card()
