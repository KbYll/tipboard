import requests, redis, json
from src.tipboard.app.properties import STEAM_ID, STEAM_API_KEY, CSGO_APP_ID


def get_stats_csgo(tester=None, tile_id='get_stats_csgo'):
    a = requests.get('https://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v2/?key=' + STEAM_API_KEY + '&appid=' + CSGO_APP_ID + '&steamid=' + STEAM_ID)
    result = a.json()
    r = redis.Redis(host='localhost', port=6379, db=4)
    r.set('get_stats_csgo', str(result))


def return_stats_csgo():
    r = redis.Redis(host='localhost', port=6379, db=4)
    rdecode = r.get('get_stats_csgo').decode()
    str = rdecode.replace("\'", "\"")
    result = json.loads(str)
    return result
