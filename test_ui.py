import streamlit as st
from test1 import create_world , generate_quest  
import logging

def game_ui():
    st.title('🎮 Procedural Adventure Game')
    st.markdown("""
    Welcome to the AI-generated adventure!  
    This game creates a unique world every time you play.
    """)
    
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
    st.session_state['world_data'] = None

    if generate_btn:
        if not selected_locations:
            st.sidebar.warning("Select at least one location ")
        else:
            st.session_state['world_data'] = create_world(selected_locations)
            st.session_state['selected_location'] = None
        # st.write(world_data)
        if st.session_state['world_data']:
            room_list = []
            for key in st.session_state['world_data'].keys():
                room_list.append(key)
            st.subheader(f"The available Rooms are {room_list}")
            selected_location = st.selectbox(
                "Select a room:",  # Label
                room_list,             # List of options
                index=None,        # No default selection (optional)
                help="Choose one room"  # Help text
                )

            logging.info(st.session_state['selected_location'])

            if selected_location:
                st.session_state['selected_location'] = selected_location
                quest = generate_quest(st.session_state['selected_location'])
                st.subheader(f"Quest in {st.session_state['selected_location'].capitalize()}")
                st.write(quest)

            else:
                st.warning('Select a destination first')

    






if __name__ == "__main__":
    game_ui()

    
    