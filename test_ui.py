import streamlit as st
from test1 import create_world , generate_quest  

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

    if generate_btn:
        world_data = create_world(selected_locations)
        # st.write(world_data)
        room_list = []
        for key in world_data.keys():
            room_list.append(key)
        
    select_location = st.selectbox(
        "Select a room:",  # Label
        room_list,             # List of options
        index=None,        # No default selection (optional)
        help="Choose one room"  # Help text
    )
    selected_location = st.button(f"select {select_location}")
    if selected_location:
        quest = generate_quest(selected_location) 

        st.write(quest)





if __name__ == "__main__":
    game_ui()

    
    