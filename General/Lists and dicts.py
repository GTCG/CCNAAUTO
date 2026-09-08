 
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