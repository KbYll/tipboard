import time, random, redis, json
from src.sensors.utils import end, sendUpdateByApi
from src.sensors.get_stats_csgo import return_stats_csgo
from src.sensors.get_user_info_steam import return_user_info_steam
from src.sensors.get_steam_level import return_steam_level
from src.sensors.get_vac_steam import return_vac_steam


def getItemExemple(index):
    if index % 2 == 0:
        return {
            'items':
                [f'Leader: {random.randrange(1, 5)}',
                 f'Product Owner: {random.randrange(1, 2)}',
                 f'Scrum Master: {random.randrange(1, 2)}',
                 f'Developer: {random.randrange(1, 5)}'
                 ]
        }
    return {
        'items':
            [f'Major incident: {random.randrange(1, 5)}',
             f'N2 incident: {random.randrange(2, 50)}',
             f'+3month incident: {random.randrange(10, 59)}',
             f'Resolved incident: {random.randrange(1, 50)}'
             ]
    }


def getItemsUserSteam():
    result = return_user_info_steam()
    result2 = return_steam_level()
    return {
        'items':
            [f'SteamApp Name: Counter-Strike Global Offensive',
             f"Player Name : {result['response']['players'][0]['personaname']}",
             f"Steam ID : {result['response']['players'][0]['steamid']}",
             f"Profile : <a href={result['response']['players'][0]['profileurl']} target='_blank'>{result['response']['players'][0]['profileurl']}</a>",
             f"Steam Level : {result2['response']['player_level']}",
             f"Country : {result['response']['players'][0]['loccountrycode']}",
             ]
    }


def getItemsVacSteam():
    result = return_vac_steam()
    return {
        'items':
            [f"Community Banned : {result['players'][0]['CommunityBanned']}",
             f"Vac Banned : {result['players'][0]['VACBanned']}",
             f"Number of Vac Bans : {result['players'][0]['NumberOfVACBans']}",
             f"Days since Last Ban : {result['players'][0]['DaysSinceLastBan']}",
             f"Number of Game Bans : {result['players'][0]['NumberOfGameBans']}",
             f"Economy Ban : {result['players'][0]['EconomyBan']}",
             ]
    }


def getItemsStatsCSGO():
    result = return_stats_csgo()
    return {
        'items':
            [f"Wins : {result['playerstats']['stats'][5]['value']}",
             f"kills : {result['playerstats']['stats'][0]['value']}",
             f"deaths : {result['playerstats']['stats'][1]['value']}",
             f"Kills Headshot : {result['playerstats']['stats'][25]['value']}",
             f"Headshot Percentage : {round(result['playerstats']['stats'][25]['value'] * 100 / result['playerstats']['stats'][0]['value'], 2)}",
             f"Average Damage Per Shot : {round(result['playerstats']['stats'][6]['value'] / result['playerstats']['stats'][47]['value'], 2)}",
             f"Average Shot Per Hit : {round(result['playerstats']['stats'][48]['value'] / result['playerstats']['stats'][47]['value'], 2)}"
             ]
    }


def executeScriptToGetData():
    """ Simulate some actions for text tile exemple"""
    return getItemExemple(random.randrange(0, 3))


def sonde6Test(tester=False, tile_id='kbyl_list'):
    start_time = time.time()
    data = executeScriptToGetData()
    tipboardAnswer = sendUpdateByApi(data=data, tileTemplate='listing', tileId=tile_id, tester=tester)
    end(title=f'sensors6 -> {tile_id}', startTime=start_time, tipboardAnswer=tipboardAnswer, tileId=tile_id)


def sonde6StatsCSGO(tester=False, tile_id='csgo_stats'):
    start_time = time.time()
    data = getItemsStatsCSGO()
    tipboardAnswer = sendUpdateByApi(data=data, tileTemplate='listing', tileId=tile_id, tester=tester)
    end(title=f'sensors6 -> {tile_id}', startTime=start_time, tipboardAnswer=tipboardAnswer, tileId=tile_id)


def sonde6UserSteam(tester=False, tile_id='user_steam'):
    start_time = time.time()
    data = getItemsUserSteam()
    tipboardAnswer = sendUpdateByApi(data=data, tileTemplate='listing', tileId=tile_id, tester=tester)
    end(title=f'sensors6 -> {tile_id}', startTime=start_time, tipboardAnswer=tipboardAnswer, tileId=tile_id)


def sonde6VacSteam(tester=False, tile_id='vac_steam'):
    start_time = time.time()
    data = getItemsVacSteam()
    tipboardAnswer = sendUpdateByApi(data=data, tileTemplate='listing', tileId=tile_id, tester=tester)
    end(title=f'sensors6 -> {tile_id}', startTime=start_time, tipboardAnswer=tipboardAnswer, tileId=tile_id)