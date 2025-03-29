import streamlit as st
import json
from test1 import create_world , generate_quest  
import logging
import sys
import ast

# Configure logging to show in terminal and Streamlit
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),  
        logging.StreamHandler(sys.stderr)   
    ]
)

def game_ui():
    st.title('🎮 Procedural Adventure Game')
    st.markdown("""
    Welcome to the AI-generated adventure!  
    This game creates a unique world every time you play.
    """)
    if 'world_data' not in st.session_state:
        st.session_state['world_data'] = None
    if 'selected_location' not in st.session_state:
        st.session_state['selected_location'] = None
    if 'quest' not in st.session_state:
        st.session_state['quest'] = None
    
    # Sidebar controls
    with st.sidebar:
        st.header("Game Controls")
        generate_btn = st.button("Generate New World")
        locations = ["forest", "tavern", "cave", "castle"]
        select_all = st.checkbox("Select All")
        if select_all:
            selected_locations = st.multiselect(
                "Choose locations:",
                locations,
                default=locations  # Selects all if "Select All" is checked
            )
        else:
            selected_locations = st.multiselect(
                "Choose locations:",
                locations,
                default=None  # No selection by default
            )


    if generate_btn:
        if not selected_locations:
            st.sidebar.warning("Select at least one location ")
        else:
            st.session_state['world_data'] = create_world(selected_locations)
            st.session_state.selected_location = None
            st.json(st.session_state['world_data'])

        # st.write(world_data)
    if st.session_state['world_data']:
        room_list = list(set(st.session_state['world_data'][key]['description'] for key in st.session_state['world_data']))
        st.subheader(f"The available Rooms are {room_list}")
        selected_location = st.selectbox(
            "Select a room:",  
            room_list,             
            index=None,        
            help="Choose one room"  
            )

        logging.info(st.session_state['selected_location'])

        if selected_location:
            st.session_state['selected_location'] = selected_location
            desc = selected_location
            quest = generate_quest(desc)


            st.session_state['quest'] = json.loads(quest)
            if st.button('Lets gooooooo'):
                st.session_state['page'] = 'output'


def game_page():
    st.header("We are on game page")
    st.write(st.session_state['quest'])
    






if __name__ == "__main__":
    if 'page' not in st.session_state:
        st.session_state['page'] = 'input'
    if st.session_state['page'] == 'input':
        game_ui()
    elif st.session_state['page'] == 'output':
        game_page()

    
    