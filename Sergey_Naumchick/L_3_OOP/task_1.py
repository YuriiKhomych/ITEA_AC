def set_period(api):
    if api in range(1, 4):
        return {
            1: 3,
            2: 7,
            3: 10,
        }.get(api)
    else:
        return 30


def collect_val_network(api):
    return {
        1: "facebook",
        2: "google_insights",
        3: "twiter_insights",
        4: "snachatinsight",
    }.get(api)
