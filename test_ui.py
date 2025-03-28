import streamlit as st
from test1 import main  # Assuming main() returns your game world

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
        reset_btn = st.button("Reset Game")
    
    # Session state to persist the world
    if 'world' not in st.session_state or generate_btn or reset_btn:
        st.session_state.world = main()
        st.session_state.player_location = list(st.session_state.world.keys())[0]  # Start in first location
    
    # Display current location
    current_loc = st.session_state.player_location
    st.subheader(f"📍 {current_loc}")
    st.write(st.session_state.world[current_loc]['description'])
    
    # Show exits
    exits = st.session_state.world[current_loc].get('exits', {})
    if exits:
        st.markdown("### Exits:")
        cols = st.columns(3)
        for i, (direction, room) in enumerate(exits.items()):
            if cols[i % 3].button(f"Go {direction}"):
                st.session_state.player_location = room
                st.rerun()
    
    # Display world JSON (collapsible)
    with st.expander("Debug: View Raw World Data"):
        st.json(st.session_state.world)

if __name__ == "__main__":
    game_ui()