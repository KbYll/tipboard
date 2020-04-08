import time, random, json
from src.tipboard.app.properties import TIPBOARD_URL, COLOR_TAB, LOG
from src.sensors.utils import end, sendUpdateByApi, updateChartJS
from src.sensors.get_stats_csgo import return_stats_csgo


def updateChartJSPistols(nbrDataset=None, nbrLabel=None, colorTabIndataset=False, data=None):
    totalKillPistols = 0
    pistols = ['glock', 'deagle', 'elite', 'fiveseven', 'p250', 'hkp2000', 'tec9']
    pistols_kills = {}
    result = return_stats_csgo()
    for elt in result['playerstats']['stats']:
        for pistol_name in pistols:
            if elt['name'] == f'total_kills_{pistol_name}':
                pistols_kills[pistol_name] = elt['value']
                totalKillPistols += elt['value']
    tileData = dict()
    tileData['title'] = dict(text=f'Total : {totalKillPistols}',
                             color='#FFFFFF',
                             display=True)  # random.choice([True, False]))
    tileData['legend'] = dict(display=True)
    tileData['labels'] = list(pistols_kills.keys())  # [f'{i}' for i in pistols]
    tileData['datasets'] = list()
    tileData['datasets'].append(
        dict(label=f'Pistols',
             data=list(pistols_kills.values()),
             # if data is None else data,
             backgroundColor=COLOR_TAB,
             borderColor='#626262'))
    tileData['options'] = {
        "plugins": {
            "labels": {
                "render": "value"
            }
        }
    }
    return tileData


def updateChartJSAssaultRifles(nbrDataset=None, nbrLabel=None, colorTabIndataset=False, data=None):
    totalKillAssaultRifles = 0
    assaultRifles = ['awp', 'ak47', 'aug', 'famas', 'g3sg1', 'sg556', 'scar20', 'ssg08', 'm4a1', 'galilar']
    assaultRifles_kills = {}
    result = return_stats_csgo()
    for elt in result['playerstats']['stats']:
        for assaultRifles_name in assaultRifles:
            if elt['name'] == f'total_kills_{assaultRifles_name}':
                assaultRifles_kills[assaultRifles_name] = elt['value']
                totalKillAssaultRifles += elt['value']
    tileData = dict()
    tileData['title'] = dict(text=f'Total : {totalKillAssaultRifles}',
                             color='#FFFFFF',
                             display=True)  # random.choice([True, False]))
    tileData['legend'] = dict(display=True)
    tileData['labels'] = list(assaultRifles_kills.keys())  # [f'{i}' for i in assaultRifles]
    tileData['datasets'] = list()
    tileData['datasets'].append(
        dict(label=f'Assault Rifles',
             data=list(assaultRifles_kills.values()),  # if data is None else data,
             backgroundColor=COLOR_TAB,
             borderColor='#626262'))
    tileData['options'] = {
        "plugins": {
            "labels": {
                "render": "value"
            }
        }
    }
    return tileData


def sonde16Pistols(tester=None, tile_id='pistols_doughnut_ex'):
    start_time = time.time()
    data = updateChartJSPistols(colorTabIndataset=True)
    tipboardAnswer = sendUpdateByApi(data=data, tileTemplate='doughnut_chart', tileId=tile_id, tester=tester)
    end(title=f'sensors3 -> {tile_id}', startTime=start_time, tipboardAnswer=tipboardAnswer, tileId=tile_id)


def sonde16AssaultRifles(tester=None, tile_id='assaultRifles_doughnut_ex'):
    start_time = time.time()
    data = updateChartJSAssaultRifles(colorTabIndataset=True)
    tipboardAnswer = sendUpdateByApi(data=data, tileTemplate='doughnut_chart', tileId=tile_id, tester=tester)
    end(title=f'sensors3 -> {tile_id}', startTime=start_time, tipboardAnswer=tipboardAnswer, tileId=tile_id)
