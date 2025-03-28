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

        if generate_btn:
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
            world_data = create_world(selected_locations)

            st.display(world_data)


if __name__ == "__main__":
    game_ui()

    
    