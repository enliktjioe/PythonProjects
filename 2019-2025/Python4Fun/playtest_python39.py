# Reference: https://realpython.com/python39-new-features/

# Proper Time Zone Support
def proper_timezone():
    from datetime import datetime, timezone
    print(datetime.now(tz=timezone.utc))

    from zoneinfo import ZoneInfo
    print(ZoneInfo("America/Vancouver"))

    print(datetime.now(tz=ZoneInfo("Europe/Tallinn")))
    print(datetime.now(tz=ZoneInfo("Europe/Dublin")))


# Simpler Updating of Dictionaries
def simpler_dict():
    pycon = {2016: "Portland", 2018: "Cleveland"}
    europython = {2017: "Rimini", 2018: "Edinburgh", 2019: "Basel"}
    # 2018 - Cleveland will be replaced wtih 2018 - Edinburgh 
    
    # Method 1 - Simpler
    print({**pycon, **europython})

    # Method 2 - Old ways
    merged = pycon.copy()
    for key, value in europython.items():
        merged[key] = value

    print(merged)

    # Based on PEP 584, the new version of Python introduces two new operators 
    # for dictionaries: union (|) and in-place union (|=). You can use | to merge 
    # two dictionaries, while |= will update a dictionary in place:
    print(pycon | europython)
    pycon |= europython
    print(pycon)
    # print(europython)

    # In this example, you update libraries from a list of 2-tuples. When there are overlapping 
    # keys in two dictionaries that you want to merge, the last value is kept:
    asia = {"Georgia": "Tbilisi", "Japan": "Tokyo"}
    usa = {"Missouri": "Jefferson City", "Georgia": "Atlanta"}
    print(asia | usa)
    print(usa | asia)


# Call function
# proper_timezone()
simpler_dict()