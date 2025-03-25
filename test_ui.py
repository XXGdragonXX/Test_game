import streamlit as st
from test1 import main


def test_ui():
    st.title('Streamlit Game test')
    world = main()
    st.json(world)
    st.write('Game world created!')


test_ui()