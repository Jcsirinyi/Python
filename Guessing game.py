import random

difficulties = {
    "Easy": (1, 10, None),
    "Medium": (1, 50, 7),
    "Hard": (1, 100, 10),
}

def get_difficulty():
    print("🎮 Choose a difficulty: Easy / Medium / Hard")
    choice = input("Enter difficulty: ").capitalize()
    if choice in difficulties:
        print(f"✅ You chose {choice} mode.")
        return difficulties[choice]
    else:
        print("⚠️ Invalid choice. Defaulting to Easy mode.")
        return difficulties["Easy"]

def give_hint(secret, guess):
    distance = abs(secret - guess)
    if distance == 0:
        return "🎉 Correct!"
    elif distance <= 3:
        return "🔥 You're very hot!"
    elif distance <= 10:
        return "🌡️ You're warm."
    else:
        return "🥶 You're cold."

def play_game():
    min_val, max_val, max_attempts = get_difficulty()
    secret_number = random.randint(min_val, max_val)
    attempts = 0
    print(f"\nI'm thinking of a number between {min_val} and {max_val}.")
    if max_attempts:
        print(f"You have {max_attempts} attempts to guess it.")
    else:
        print("You have unlimited attempts. Good luck!")
    while True:
        guess = input("\n👉 Make a guess: ")
        if not guess.isdigit():
            print("⚠️ Please enter a valid number.")
            continue
        guess = int(guess)
        if guess < min_val or guess > max_val:
            print(f"⚠️ Your guess must be between {min_val} and {max_val}.")
            continue
        attempts += 1
        if guess == secret_number:
            print(f"🎉 You got it in {attempts} attempt(s)! The number was {secret_number}.")
            break
        else:
            print(give_hint(secret_number, guess))
            if max_attempts and attempts >= max_attempts:
                print("❌ You're out of attempts! Game Over.")
                print(f"The correct number was {secret_number}.")
                break

while True:
    play_game()
    play_again = input("\n🔁 Do you want to play again? (yes/no): ").lower()
    if play_again not in ("yes", "y"):
        print("👋 Thanks for playing! Goodbye.")
        break