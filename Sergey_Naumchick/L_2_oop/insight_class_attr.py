from BaseInsight import BaseInsight
from hw_start import insights
from classes import *


def adding_attr(api):
    return {
        1: facebook,
        2: google_insights,
        3: twitter_insights,
        4: snapchatinsight,
    }.get(api, BaseInsight)
