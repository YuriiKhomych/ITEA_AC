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
    apisnik = insight['api'] if 'api' in insight else None
    apisnik_for_class = ch_api(apisnik)
    tries = apisnik_for_class(**insight)
    if apisnik != None:
        print(tries.__dict__)
    else:
        print(f'Sorry api is {apisnik}')

