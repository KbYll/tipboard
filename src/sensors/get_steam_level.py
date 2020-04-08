import requests, redis, json
from src.tipboard.app.properties import STEAM_ID, STEAM_API_KEY


def get_steam_level(tester=None, tile_id='get_steam_level'):
    a = requests.get('https://api.steampowered.com/IPlayerService/GetSteamLevel/v1/?key=' + STEAM_API_KEY + '&steamid=' + STEAM_ID)
    result = a.json()
    r = redis.Redis(host='localhost', port=6379, db=4)
    r.set('get_steam_level', str(result))


def return_steam_level():
    r = redis.Redis(host='localhost', port=6379, db=4)
    rdecode = r.get('get_steam_level').decode()
    str = rdecode.replace("\'", "\"")
    result = json.loads(str)
    return result