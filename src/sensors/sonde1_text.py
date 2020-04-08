import requests, time, random, lorem, json, redis
from src.tipboard.app.properties import TIPBOARD_URL
from src.sensors.utils import end
from src.tipboard.app.DefaultData.defaultTileControler import getDefaultText


def executeScriptToGetData(tile_id=None, tile_template=None):
    """ Replace getFakeText with your script to GET text tile data """
    tile = getDefaultText()
    tile['tile_id'] = tile_id
    tile['tile_template'] = tile_template
    tile['data']['text'] = f'Last malware detedted: <br>' \
        f'<h2> {"".join([random.choice("0123456789abcdef") for x in range(32)])}</h2>'
    return tile


def executeScriptToGetDataTest(tile_id=None, tile_template=None):
    """ Replace getFakeText with your script to GET text tile data """
    r = redis.Redis(host='localhost', port=6379, db=4)
    result = r.get('test_get_stats_csgo')
    tile = {}
    tile['tile_id'] = tile_id
    tile['tile_template'] = tile_template
    tile['data'] = {}
    tile['data']['text'] = f'{result.decode()}'
    return tile

def sendDataToTipboard(data=None, tile_template=None, tile_id='', tester=None):
    configTile = dict(tile_id=tile_id, tile_template=tile_template, data=json.dumps(data['data']['text']))
    if tester is None:
        return requests.post(TIPBOARD_URL + '/push', data=configTile)
    else:
        return tester.fakeClient.post(TIPBOARD_URL + '/push', data=configTile)


def sonde1Test(tester=None, tile_id='kbyl', tile_template='text'):
    start_time = time.time()
    data = executeScriptToGetData()
    #data['data']['text'] = f'Last malware detedted: <br>' \
    #    f'<h2> {"".join([random.choice("0123456789abcdef") for x in range(32)])}</h2>'
    tipboardAnswer = sendDataToTipboard(data, tile_template=tile_template, tile_id=tile_id, tester=tester)
    end(title=f'sensors1 -> {tile_id}', startTime=start_time, tipboardAnswer=tipboardAnswer, tileId=tile_id)


def sonde1CSGO(tester=None, tile_id='csgo_txt', tile_template='text'):
    start_time = time.time()
    data = executeScriptToGetData()
    data['data']['text'] = '\nGame is CSGO\nApp Id is 730\n player name is Kbyl'
    tipboardAnswer = sendDataToTipboard(data, tile_template=tile_template, tile_id=tile_id, tester=tester)
    end(title=f'sensors1 -> {tile_id}', startTime=start_time, tipboardAnswer=tipboardAnswer, tileId=tile_id)

"""
def sonde1CSGOTest(tester=None, tile_id='test_csgo_txt', tile_template='text'):
    start_time = time.time()
    data = executeScriptToGetDataTest()
    #data['data']['text'] = '\nGame is CSGO\nApp Id is 730\n player name is Kbyl'
    tipboardAnswer = sendDataToTipboard(data, tile_template=tile_template, tile_id=tile_id, tester=tester)
    end(title=f'sensors1 -> {tile_id}', startTime=start_time, tipboardAnswer=tipboardAnswer, tileId=tile_id)
"""
