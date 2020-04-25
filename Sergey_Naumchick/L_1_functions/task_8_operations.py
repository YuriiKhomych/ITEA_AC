def sorting_by(insights, key):
    result = []
    for elemen in insights:
        if key in elemen.keys():
            result.append(elemen)
    result.sort(key=lambda x: x[key])

    for elemen in insights:
        if key not in elemen.keys():
            result.append(elemen)
    return result
