from hw_start import insights

def insight_builder(insight):
    list_insight_network = []
    for insight in insights:
        if "api" in insight.keys():
            list_insight_network.append(insight_chooser(el["api"])(**el))
    return list_insight_network
