import os
import sys
import json
import glob


ghq_root = "/Users/skato/Dropbox/ghq"

query = sys.argv[1]

reps = [rep for rep in glob.glob(os.path.join(ghq_root, "**/**/*"))
        if query in rep]

items = []
for rep in reps:
    values = rep.split("/")
    user = values[-2]
    name = values[-1]
    arg = "/".join(values[-3:])
    items.append({
        "uid": rep,
        "type": "file",
        "title": name,
        "subtitle": arg,
        "arg": user + "/" + name,
        "autocomplete": arg,
        "icon": {
            "type": "fileicon",
            "path": rep
        }
    })

outjson = {
    "items": items
}

sys.stdout.write(json.dumps(outjson))
