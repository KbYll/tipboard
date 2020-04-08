import requests, redis, json
from src.tipboard.app.properties import STEAM_ID, STEAM_API_KEY, CSGO_APP_ID


def get_achievements_csgo(tester=None, tile_id='get_achievements_csgo'):
    a = requests.get('https://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v1/?key=' + STEAM_API_KEY + '&steamid=' + STEAM_ID + '&appid=' + CSGO_APP_ID)
    result = a.json()
    r = redis.Redis(host='localhost', port=6379, db=4)
    r.set('get_achievements_csgo', str(result))


def return_achievements_csgo():
    r = redis.Redis(host='localhost', port=6379, db=4)
    rdecode = r.get('get_achievements_csgo').decode()
    str = rdecode.replace("\'", "\"")
    result = json.loads(str)
    return result
