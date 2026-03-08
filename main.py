import random

# ── Score Tracker ─────────────────────────────────────────────────────────────
score = {
    "wins":   0,
    "losses": 0,
    "draws":  0,
}

# ── Input Helpers ─────────────────────────────────────────────────────────────
def user_guess():
    """Ask the player for 3 unique numbers between 1 and 6."""
    while True:
        try:
            nums = []
            for i in ["first", "second", "third"]:
                nums.append(int(input(f"  Guess {i} number (1-6): ")))

            a, b, c = nums

            if a == b or a == c or b == c:
                print("  ⚠️  All three numbers must be DIFFERENT. Try again.\n")
                continue
            if not all(1 <= n <= 6 for n in nums):
                print("  ⚠️  All numbers must be between 1 and 6. Try again.\n")
                continue

            return a, b, c

        except ValueError:
            print("  ⚠️  Please enter whole numbers only!\n")


def comp_guess():
    """Computer randomly rolls 3 dice."""
    return random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)


# ── Score Display ─────────────────────────────────────────────────────────────
def print_scoreboard():
    total = score["wins"] + score["losses"] + score["draws"]
    win_rate = (score["wins"] / total * 100) if total > 0 else 0

    print("\n" + "─" * 35)
    print("        📊  SCOREBOARD")
    print("─" * 35)
    print(f"Wins    : {score['wins']}")
    print(f"Losses  : {score['losses']}")
    print(f"Draws   : {score['draws']}")
    print(f"Rounds  : {total}")
    print(f"Win Rate: {win_rate:.1f}%")
    print("─" * 35 + "\n")


# ── Main Game ─────────────────────────────────────────────────────────────────
def main():
    print("       __________WELCOME TO THE DICE GAME__________")
    print(" 🎲 " * 14)
    print("""
  📖 RULES:
     • Pick 3 different numbers, each between 1 and 6
     • Computer rolls 3 random dice
     • Highest total SUM wins!
     • Your numbers must all be unique — computer's can repeat
""")

    round_num = 0

    while True:
        round_num += 1
        print(f"  ------------ROUND: {round_num}---------------")

        # Player input
        a, b, c = user_guess()
        player_sum = a + b + c

        # Computer roll
        x, y, z = comp_guess()
        comp_sum  = x + y + z

        # Results
        print(f"\n  Your roll  : {a}, {b}, {c}  →  Sum: {player_sum}")
        print(f"  Computer   : {x}, {y}, {z}  →  Sum: {comp_sum}\n")

        if player_sum > comp_sum:
            print("  🎉 YOU WIN this round!")
            score["wins"] += 1
        elif player_sum == comp_sum:
            print("  🤝 It's a DRAW!")
            score["draws"] += 1
        else:
            print("  ☹️ Computer wins this round!")
            score["losses"] += 1

        # Show updated scoreboard after every round
        print_scoreboard()

        # Play again?
        while True:
            choice = input("  Play again? (Y / Q): ").strip().lower()
            if choice in ("y", "q"):
                break
            print("  ⚠️  Please press Y to play again or Q to quit.")

        if choice == "q":
            print("\n  👋 Thanks for playing! Final scoreboard:")
            print_scoreboard()
            print("🎲 " * 14 + "\n")
            break


if __name__ == "__main__":
    main()
