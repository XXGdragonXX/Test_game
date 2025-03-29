import random
from groq import Groq
from dotenv import load_dotenv
import json
import re



load_dotenv()
client = Groq(api_key="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")


def create_world(locations):
    world = {}
    for i in range(5):  # 5 connected rooms
        world[f"room_{i}"] = {
            "description": random.choice(["dark", "spooky", "bright"]) + " " + random.choice(locations),
            "exits": {}  # e.g., {"north": "room_2"}
        }
    return world


def generate_prompt(location):
    message = [
    {
        'role': 'system',
        'content': '''
        You are a master fantasy quest designer. Generate compelling, game-ready quests that follow EXACTLY the specified JSON format.
        - Use rich fantasy vocabulary
        - Include surprising twists
        - Balance challenge levels
        - Suggest unique rewards
        - NEVER deviate from the required structure
        '''
    },
    {
        'role': 'user',
        'content': f'''
        Generate an immersive quest for: {location}
        
        REQUIREMENTS:
        1. Strictly use this EXACT format (no extra fields/comments):
        {{
            "quest_title": "Creative title (7 words max)",
            "main_objective": "1 clear sentence objective",
            "side_objectives": [
                "Optional objective 1 (12 words max)",
                "Optional objective 2 (12 words max)",
                "Optional objective 3 (12 words max)"
            ],
            "encounters_challenges": [
                "Challenge 1 (with unique mechanic)",
                "Challenge 2 (with unique mechanic)",
                "Challenge 3 (boss encounter)"
            ],
            "rewards": [
                "Primary reward (powerful/unique)",
                "Secondary reward (utility)",
                "Hidden reward (optional discovery)"
            ]
        }}
        
        2. Must include:
        - At least one moral dilemma
        - One environmental puzzle
        - One combat encounter
        - One social challenge
        
        3. Location Theme: Amplify the {location}'s inherent characteristics
        
        4. Twist: Include one unexpected story revelation

        5. Give the output in dictionary format so I can easily convert it into json format
        
        DON'T:
        - Add explanations
        - Include markdown
        - Vary from the structure
        '''
    }
    ]

    return message

def generate_quest(location):

    response = client.chat.completions.create(
            model= "deepseek-r1-distill-llama-70b",
            messages= generate_prompt(location)
    )
    response =  response.choices[0].message.content
    clean_response = re.sub(r'<think>.*?</think>', '', response, flags=re.DOTALL).strip()
    json_match = re.search(r'\{.*\}', clean_response, re.DOTALL)
    if json_match:
        return json.loads(json_match.group())
    else:
        return clean_response

        


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



    


