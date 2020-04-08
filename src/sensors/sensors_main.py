import time, datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from src.sensors.sonde6_listing import sonde6StatsCSGO, sonde6UserSteam, sonde6VacSteam
from src.sensors.sonde9_bigvalue import sonde9RatioCSGO, sonde9HeadshotCSGO
from src.sensors.sonde16_dougnutchart import sonde16Pistols, sonde16AssaultRifles
from src.sensors.get_stats_csgo import get_stats_csgo
from src.sensors.get_achievements_csgo import get_achievements_csgo
from src.sensors.get_user_info_steam import get_user_info_steam
from src.sensors.get_steam_level import get_steam_level
from src.sensors.get_vac_steam import get_vac_steam
from src.sensors.utils import end


def addSchedule(scheduler, sonde, second, args=None):
    scheduler.add_job(sonde, 'interval', seconds=second, args=args, next_run_time=datetime.datetime.now())


def test_sensors(tester):
    get_user_info_steam(tester, 'get_user_info_steam')
    get_steam_level(tester, 'get_steam_level')
    get_vac_steam(tester, 'get_vac_steam')
    get_stats_csgo(tester, 'get_stats_csgo')
    get_achievements_csgo(tester, 'get_achievements_csgo')
    sonde6StatsCSGO(tester, 'csgo_stats')
    sonde6UserSteam(tester, 'user_steam')
    sonde6VacSteam(tester, 'vac_steam')
    sonde9RatioCSGO(tester, 'ratio_bv_ex')
    sonde9HeadshotCSGO(tester, 'headshot_bv_ex')
    sonde16Pistols(tester, 'pistols_doughnut_ex')
    sonde16AssaultRifles(tester, 'assaultRifles_doughnut_ex')


def scheduleYourSensors(scheduler=None, tester=None):
    if not scheduler.running:
        addSchedule(scheduler, get_user_info_steam, 1800, args=[tester, 'get_user_info_steam'])
        addSchedule(scheduler, get_steam_level, 1800, args=[tester, 'get_steam_level'])
        addSchedule(scheduler, get_vac_steam, 1800, args=[tester, 'get_vac_steam'])
        addSchedule(scheduler, get_stats_csgo, 1800, args=[tester, 'get_stats_csgo'])
        addSchedule(scheduler, get_achievements_csgo, 1800, args=[tester, 'get_achievements_csgo'])
        addSchedule(scheduler, sonde6StatsCSGO, 30, args=[tester, 'csgo_stats'])
        addSchedule(scheduler, sonde6UserSteam, 30, args=[tester, 'user_steam'])
        addSchedule(scheduler, sonde6VacSteam, 30, args=[tester, 'vac_steam'])
        addSchedule(scheduler, sonde9RatioCSGO, 90, args=[tester, 'ratio_bv_ex'])
        addSchedule(scheduler, sonde9HeadshotCSGO, 90, args=[tester, 'headshot_bv_ex'])
        addSchedule(scheduler, sonde16Pistols, 30, args=[tester, 'pistols_doughnut_ex'])
        addSchedule(scheduler, sonde16AssaultRifles, 30, args=[tester, 'assaultRifles_doughnut_ex'])
        print(f"(+) Tipboard starting schedul task", flush=True)
        scheduler.start()
    return scheduler


def stopTheSensors(localScheduler):
    if localScheduler is not None:
        localScheduler.shutdown()


if __name__ == "__main__":
    print(f"(+) Tipboard  sensors initialisation", flush=True)
    start_time = time.time()
    scheduleYourSensors(BlockingScheduler())  # If you need actualized data :)
    end(title="startUp", startTime=start_time)
