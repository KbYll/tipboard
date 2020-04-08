import requests, redis, json
from src.tipboard.app.properties import STEAM_ID, STEAM_API_KEY


def get_vac_steam(tester=None, tile_id='get_vac_steam'):
    a = requests.get('https://api.steampowered.com/ISteamUser/GetPlayerBans/v1/?key=' + STEAM_API_KEY + '&steamids=' + STEAM_ID)
    result = a.json()
    if result['players'][0]['CommunityBanned'] is False:
        result['players'][0]['CommunityBanned'] = "False"
    else:
        result['players'][0]['CommunityBanned'] = "True"

    if result['players'][0]['VACBanned'] is False:
        result['players'][0]['VACBanned'] = "False"
    else:
        result['players'][0]['VACBanned'] = "True"
    r = redis.Redis(host='localhost', port=6379, db=4)
    r.set('get_vac_steam', str(result))


def return_vac_steam():
    r = redis.Redis(host='localhost', port=6379, db=4)
    rdecode = r.get('get_vac_steam').decode()
    str = rdecode.replace("\'", "\"")
    result = json.loads(str)
    return result