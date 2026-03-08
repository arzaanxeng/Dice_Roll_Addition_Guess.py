# 🎲 Python Dice Game

A fun terminal-based dice game built with Python. Pick three unique numbers, roll against the computer, and track your wins across multiple rounds!

---

## 🎮 Demo

```
       __________WELCOME TO THE DICE GAME__________
🎲  🎲  🎲  🎲  🎲  🎲  🎲  🎲  🎲  🎲  🎲  🎲  🎲  🎲

  📖 RULES:
     • Pick 3 different numbers, each between 1 and 6
     • Computer rolls 3 random dice
     • Highest total SUM wins!
     • Your numbers must all be unique — computer's can repeat

  ------------ROUND: 1---------------
  Guess first number (1-6): 2
  Guess second number (1-6): 5
  Guess third number (1-6): 6

  Your roll  : 2, 5, 6  →  Sum: 13
  Computer   : 4, 4, 1  →  Sum: 9

  🎉 YOU WIN this round!

  ───────────────────────────────────
          📊  SCOREBOARD
  ───────────────────────────────────
  Wins    : 1
  Losses  : 0
  Draws   : 0
  Rounds  : 1
  Win Rate: 100.0%
  ───────────────────────────────────

  Play again? (Y / Q):
```

---

## ✨ Features

- 🎯 Player picks 3 unique numbers between 1 and 6
- 🤖 Computer randomly rolls 3 dice (duplicates allowed for computer)
- 🏆 Win if your total sum is greater than the computer's
- 🤝 Draw detection when sums are equal
- 📊 Live scoreboard after every round showing Wins, Losses, Draws, Rounds, and Win Rate
- 🔢 Round counter to track how many rounds you've played
- 🔁 Play again or quit after every round
- ✅ Full input validation — handles letters, duplicates, and out-of-range values

---

## 📏 Rules

| Rule | Detail |
|------|--------|
| Number range | All 3 numbers must be between **1 and 6** |
| All different | Your 3 numbers must all be **unique** |
| Computer | Computer can roll **duplicate** values |
| Win | Your sum is **greater than** the computer's |
| Draw | Both sums are **equal** |
| Lose | Your sum is **less than** the computer's |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed on your machine

### Run the game

```bash
python3 dice_game.py
```

No extra libraries needed — uses only Python's built-in `random` module!

---

## 🕹️ How to Play

1. **Read the rules** — displayed at the start of the game
2. **Pick 3 numbers** — each must be between 1 and 6 and all different from each other
3. **Computer rolls** — the computer generates its 3 random dice values
4. **Compare sums** — whoever has the higher total wins the round!
5. **Check the scoreboard** — your updated stats are shown after every round
6. **Play again** — press `Y` to continue or `Q` to quit and see your final score

---

## 📊 Scoreboard

After every round the game displays your running stats:

| Stat | Description |
|------|-------------|
| Wins | Total rounds you won |
| Losses | Total rounds the computer won |
| Draws | Total rounds that ended in a tie |
| Rounds | Total rounds played |
| Win Rate | Your win percentage across all rounds |

---

## 🧠 How It Works

**Player Input**
The game asks for 3 numbers one at a time and validates that all inputs are whole numbers, all values are between 1 and 6, and no two numbers are the same.

**Computer Roll**
Uses `random.randint(1, 6)` three times independently — so the computer can roll duplicates.

**Win Logic**
Both totals are compared after every spin:
- `player_sum > comp_sum` → Player wins 🎉
- `player_sum == comp_sum` → Draw 🤝
- `player_sum < comp_sum` → Computer wins ☹️

**Score Tracking**
A global dictionary tracks wins, losses, and draws across all rounds. Win rate is calculated as `(wins / total_rounds) × 100`.

---

## 📁 Project Structure

```
dice-game/
└── dice_game.py    ← main game file
```

---

## 🛠️ Built With

- Python 3
- `random` module (standard library — no installs needed!)

---


## 👨‍💻 Author

**Arzaan**
Made with 🎲 and Python
