# Python Terminal Blackjack 🎲

## Overview
A simple terminal-based Blackjack game written in Python, where a player competes against the computer using classic Blackjack rules.

The game runs entirely in the command line and focuses on core Python concepts such as control flow, recursion, user input handling, and randomization.

---

## Problem Statement
Blackjack is a popular card game that requires decision-making, probability handling, and rule-based outcomes.  
This project simulates the game logic in a terminal environment without any external libraries or GUI frameworks.

---

## Solution
The game:
- Randomly deals cards to the player and the computer
- Allows the player to **Hit** or **Pass**
- Automatically handles the computer’s turn
- Determines the winner based on Blackjack rules

The logic is implemented using Python functions and recursion to manage turns dynamically.

---

## Features
- Terminal-based interactive gameplay
- Player decision input (Hit / Pass)
- Computer-controlled opponent
- Automatic win/loss detection
- Random card dealing
- Immediate game termination on win/loss conditions

---

## Tech Stack
- **Language:** Python
- **Libraries:** `random`, `sys`
- **Environment:** Terminal / Command Line

---

## Game Rules (Simplified)
- Cards are randomly drawn from a predefined list
- Face cards are treated as value `10`
- Ace is treated as `11`
- If total exceeds `21`, the player busts
- Closest score to `21` without exceeding wins

---

## Setup & Installation

### Prerequisites
- Python 3.x installed

### Run the Game
```bash
git clone https://github.com/<your-username>/Python-terminal-blackjack.git
cd Python-terminal-blackjack
python blackjack.py
