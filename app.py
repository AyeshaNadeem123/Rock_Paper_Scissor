import streamlit as st
import random

st.set_page_config(page_title="Rock Paper Scissors", layout="centered")

# Title and instructions
st.title("Rock Paper Scissors!")
st.write("Choose your move and see if you can beat the computer!")

# List of possible moves
moves = ["Rock", "Paper", "Scissors"]

# User selection
user_move = st.radio("Your move:", moves)

# When the user clicks 'Play', the game will simulate the computer move
if st.button("Play"):
    computer_move = random.choice(moves)
    st.write(f"**Computer chose:** {computer_move}")

    # Determine the result
    if user_move == computer_move:
        result = "It's a draw!"
    elif (user_move == "Rock" and computer_move == "Scissors") or \
         (user_move == "Paper" and computer_move == "Rock") or \
         (user_move == "Scissors" and computer_move == "Paper"):
        result = "You win!"
        st.balloons()  # Celebrate the win with balloons
    else:
        result = "You lose."

    # Display the result
    st.subheader(result)
