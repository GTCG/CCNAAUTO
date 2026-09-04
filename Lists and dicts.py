"""
Parses and validates the 'Science' data structure.
 
Structure to trace carefully:
    Science                       -> LIST of subjects
      [0]                         -> DICT for one subject (e.g. Chemistry)
        ["type"]                  -> string
        ["eyes"]                  -> LIST of color groups
          [0]                     -> DICT for one color group
            ["color"]             -> sometimes a LIST (["blue","green"]),
                                      sometimes a STRING ("brown")  <-- trap
            ["students"]          -> LIST of names
 
The inconsistent "color" type is the deliberate trap here: code that assumes
"color" is always a list will crash (or silently misbehave) on the "brown"
entries, because iterating over a string iterates over its characters.
"""
 
Science = [
    {
        "type": "Chemistry",
        "eyes": [
            {
                "color": ["blue", "green"],
                "students": ["Michael", "Debbie"]
            },
            {
                "color": "brown",
                "students": ["Stephanie", "Lynda"]
            }
        ]
    },
    {
        "type": "Physics",
        "eyes": [
            {
                "color": ["blue", "green"],
                "students": ["Kimberly", "Paul"]
            },
            {
                "color": "brown",
                "students": ["Xavier", "Alexander"]
            }
        ]
    },

    {
        "type": "Physics",
        "eyes": [
            {
                    "color": ["blue", "green", "grey"],
                    "students": ["John", "Eric"]
            },
            {
                    "color": ["Yellow"],
                    "students": ["Bart", "Homer"]
            }
        ]
    }
]


#print(list(filter(lambda x: x["type"]=="Physics", Science))[0]["eyes"][0]["color"])
print(list(filter(lambda x: x["type"]=="Physics", Science))[0]["eyes"][0]["color"][0])
#print(list(filter(lambda x: x["type"]=="Physics", Science))[0]["eyes"][0]["color"][0][0])
print(list(filter(lambda x: x["type"]=="Physics", Science))[1]["eyes"][1]["color"][0])