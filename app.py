import streamlit as st
import subprocess

st.title('Rock, Paper, Scissors, Lizard, Spock')

st.text("Hello, let's play a game. Choose your fate:")


def run_game(user_choice):
    cmd = ['python', 'game_test.py']
    output = subprocess.check_output(cmd, input=user_choice, text=True).strip()
    return output


col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if st.button('Rock'):
        results = run_game('rock')
        st.write(results)

with col2:
    if st.button('Paper'):
        results = run_game('paper')
        st.write(results)

with col3:
    if st.button('Scissors'):
        results = run_game('scissors')
        st.write(results)

with col4:
    if st.button('Lizard'):
        results = run_game('lizard')
        st.write(results)

with col5:
    if st.button('Spock'):
        results = run_game('spock')
        st.write(results)
