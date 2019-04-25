BIRD_LIST = {
    "Eurasian three-toed woodpecker": {
        "name": "Eurasian three-toed woodpecker",
        "wingspan": 35,
        "nest": {
            "type": "universal",
            "terrain": "universal",
        },
    },
    "Common stork": {
        "name": "Common stork",
        "wingspan": 175,
        "nest": {
            "type": "platform",
            "terrain": "swamp",
        },
    },
    "Common pigeon": {
        "name": "Common pigeon",
        "wingspan": 60,
        "nest": {
            "type": "universal",
            "terrain": "universal",
        },
    },
    "Bee hummingbird": {
        "name": "Eurasian three-toed woodpecker",
        "wingspan": 6,
        "nest": {
            "type": "cavity",
            "terrain": "forest",
        },
    },
}


def get_all() -> dict:
    birds = [bird for bird in BIRD_LIST.values()]
    return {"birds": birds}


def get_one(bird_name: str) -> dict:
    try:
        bird = BIRD_LIST[bird_name]
        return {"bird": bird}
    except KeyError:
        raise Exception("No bird in DB")

