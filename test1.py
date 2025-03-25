import random

def main():
    locations = ["forest", "tavern", "cave", "castle"]
    world = {}
    for i in range(5):  # 5 connected rooms
        world[f"room_{i}"] = {
            "description": random.choice(["dark", "spooky", "bright"]) + " " + random.choice(locations),
            "exits": {}  # e.g., {"north": "room_2"}
        }
    print(world)
    return world