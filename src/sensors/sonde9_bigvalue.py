import time, random
from src.sensors.utils import end, sendUpdateByApi
from src.tipboard.app.properties import BACKGROUND_TAB
from src.sensors.get_stats_csgo import return_stats_csgo


def executeScriptToGetDataRatio():
    """ Simulate some actions for text tile exemple """
    result = return_stats_csgo()
    ulv = result['playerstats']['stats'][0]['value']
    urv = result['playerstats']['stats'][1]['value']
    bv = ulv / urv
    return {
        'title': None,
        'description': 'Kills / Deaths',
        'big-value': round(bv, 3),
        'upper-left-label': 'Total Kills:',
        'upper-left-value': ulv,
        'lower-left-label': '',
        'upper-right-label': 'Total Deaths:',
        'upper-right-value': urv,
        'lower-right-label': '',
    }


def executeScriptToGetDataHeadshot():
    """ Simulate some actions for text tile exemple """
    result = return_stats_csgo()
    ulv = result['playerstats']['stats'][25]['value']
    urv = result['playerstats']['stats'][0]['value']
    bv = ulv * 100 / urv
    return {
        'title': None,
        'description': 'Headshot Percentage',
        'big-value': f'{round(bv, 2)}%',
        'upper-left-label': 'Total Kills Headshot:',
        'upper-left-value': ulv,
        'lower-left-label': '',
        'upper-right-label': 'Total Kills:',
        'upper-right-value': urv,
        'lower-right-label': '',
    }


def sonde9RatioCSGO(tester=False, tile_id='ratio_bv_ex'):
    start_time = time.time()
    data = executeScriptToGetDataRatio()
    meta = dict(big_value_color=BACKGROUND_TAB[0] if data['big-value'] >= 1 else BACKGROUND_TAB[1], fading_background=False if data['big-value'] >= 1 else True)
    tipboardAnswer = sendUpdateByApi(tileId=tile_id, data=data, tileTemplate='big_value', tester=tester, meta=meta)
    end(title=f'sensors9 -> {tile_id}', startTime=start_time, tipboardAnswer=tipboardAnswer, tileId=tile_id)


def sonde9HeadshotCSGO(tester=False, tile_id='headshot_bv_ex'):
    start_time = time.time()
    data = executeScriptToGetDataHeadshot()
    meta = dict(big_value_color=BACKGROUND_TAB[0], fading_background=False)
    tipboardAnswer = sendUpdateByApi(tileId=tile_id, data=data, tileTemplate='big_value', tester=tester, meta=meta)
    end(title=f'sensors9 -> {tile_id}', startTime=start_time, tipboardAnswer=tipboardAnswer, tileId=tile_id)
