import random
from groq import Groq
from dotenv import load_dotenv
import logging


load_dotenv()
client = Groq(api_key="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")


def create_world(locations):
    world = {}
    for i in range(5):  # 5 connected rooms
        world[f"room_{i}"] = {
            "description": random.choice(["dark", "spooky", "bright"]) + " " + random.choice(locations),
            "exits": {}  # e.g., {"north": "room_2"}
        }
    logging.info(world)
    return world

def generate_quest(location):

    response = client.chat.completions.create(
            model= "deepseek-r1-distill-llama-70b",
            messages=[
            {"role": "system", "content": "Generate a 1-sentence quest."},
            {"role": "user", "content": f"Location: {location}"}
        ],
        max_tokens=50,
    )
    return response.choices[0].message.content

# def main():
#     player_loc = "tavern"
#     while True:
#         print("\n" + locations[player_loc]["desc"])
        
#         if player_loc == "tavern":
#             print(f"Quest: {generate_quest(player_loc)}")
        
#         cmd = input("> ").lower()
#         if cmd == "quit":
#             break
#         elif cmd.startswith("go "):
#             dest = cmd.split("go ")[1]
#             if dest in locations[player_loc]["exits"]:
#                 player_loc = dest
#             else:
#                 print("Can't go there!")
#         else:
#             print("Try 'go [place]' or 'quit'.")



    


