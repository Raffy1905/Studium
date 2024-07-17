rooms = ["L102", "L103", "L104", "L108", "L109", "L110", "L111", "L113", "L114", "L115", "L117", "L120", "L121"]

pairs = [(a,b) for idx, a in enumerate(rooms) for b in rooms[idx + 1:]]

for pair in pairs:
    print(pair);