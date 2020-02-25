from hw_start import insights
from Google import GoogleInsight, FacebookInsight, SnapchatInsight, TwitterInsight
from BaseInsight import BaseInsight


def ch_api(api):
    # search non None api and return value
    return {
        1: FacebookInsight,
        2: GoogleInsight,
        3: TwitterInsight,
        4: SnapchatInsight,
    }.get(api, BaseInsight)


for insight in insights:
    apishnik = insight['api'] if 'api' in insight else None
    apishnik_for_class = ch_api(apishnik)
    tries = apishnik_for_class(**insight)
    if apishnik is not None:
        print(tries.__dict__)
    else:
        print(f'Sorry api is {apishnik}')
