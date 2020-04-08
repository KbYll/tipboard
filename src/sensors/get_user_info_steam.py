import requests, redis, json
from src.tipboard.app.properties import STEAM_ID, STEAM_API_KEY


def get_user_info_steam(tester=None, tile_id='get_user_info_steam'):
    a = requests.get('https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/?key=' + STEAM_API_KEY + '&steamids=' + STEAM_ID)
    result = a.json()
    r = redis.Redis(host='localhost', port=6379, db=4)
    r.set('get_user_info_steam', str(result))


def return_user_info_steam():
    r = redis.Redis(host='localhost', port=6379, db=4)
    rdecode = r.get('get_user_info_steam').decode()
    str = rdecode.replace("\'", "\"")
    result = json.loads(str)
    return result
