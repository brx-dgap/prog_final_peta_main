import random

# Stylized rooster art
def display_rooster_art():
    rooster_art = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣤⣴⣿⣧⣴⡆⠀⠀
⠀⠀⠀⠀⠠⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⢿⠟⢋⣡⢌⠉⠉⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠙⢿⣿⣷⣦⢰⣧⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣷⠺⠿⢷⡀⠀⠀
⠀⠀⠀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⢸⣿⣇⠐⣶⡀⠀⠀⠀
⠀⠀⠀⠁⣠⠶⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⢀⣼⣿⣿⣦⣈⡁⠀⠀⠀
⠀⠀⠀⠀⢠⣾⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⠀⡾⠿⢿⣿⢿⣿⣿⣷⠀⠀⠀
⠀⠀⠀⠀⠘⠁⣴⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢀⣤⡄⠘⢁⠘⠏⣁⠛⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡿⠁⢾⡟⠉⠻⣿⣿⣿⣿⣿⣿⣿⣿⣷⣴⣿⡄⣴⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠘⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣿⡿⠟⠋⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠿⠿⠿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣶⣠⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢉⣿⣿⡏⣿⡶⣤⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠈⠁⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """
    print(rooster_art)

# Initialize roosters
ROOSTER_DATABASE = [
    {"name": "Fighter", "attack": 19, "defense": 5, "level": 1},
    {"name": "Speeder", "attack": 16, "defense": 4, "level": 1},
    {"name": "Tank", "attack": 18, "defense": 8, "level": 1},
    {"name": "Champion", "attack": 20, "defense": 7, "level": 1}
]

# Function to display rooster stats
def display_rooster(rooster):
    print(f"\nYour Rooster: {rooster['name']}")
    print(f"  Level: {rooster['level']}")
    print(f"  Attack: {rooster['attack']}")
    print(f"  Defense: {rooster['defense']}\n")

# Simulate a fight with interactive choices
def fight(rooster, opponent):
    print(f"\nThe fight begins! {rooster['name']} vs {opponent['name']}\n")
    display_rooster_art()  # Show rooster art before the fight

    rooster_health = 100
    opponent_health = 100
    block_count = 5
    rooster_blocking = False

    while rooster_health > 0 and opponent_health > 0:
        # Player's turn
        print(f"\nYour turn!\n 1. Attack\n 2. Block (Remaining: {block_count})")
        choice = input("Choose your action (1 or 2): ").strip()

        if choice == "1":
            damage = max(1, rooster['attack'] - opponent['defense'])
            opponent_health -= damage
            print(f"You attack {opponent['name']} for {damage} damage!")
            rooster_blocking = False
        elif choice == "2":
            if block_count > 0:
                print(f"You prepare to block the next attack!")
                rooster_blocking = True
                block_count -= 1
            else:
                print("You are out of blocks! You lose your turn.")
                rooster_blocking = False
        else:
            print("Invalid choice, please enter either 1 or 2!")
            rooster_blocking = False
            continue  # Ask for a valid input again

        # Check if opponent is defeated
        if opponent_health <= 0:
            print(f"\n{opponent['name']} is defeated! {rooster['name']} wins!\n")
            return True

        # Opponent's turn with random damage
        opponent_damage = random.randint(1, opponent['attack'])
        damage = max(1, opponent_damage - (rooster['defense'] + 3 if rooster_blocking else rooster['defense']))
        rooster_health -= damage
        print(f"{opponent['name']} attacks you for {damage} damage!")

        # Check if player is defeated
        if rooster_health <= 0:
            print(f"\n{rooster['name']} is defeated! {opponent['name']} wins!\n")
            return False

        # Display health stats
        print(f"\n{rooster['name']} Health: {rooster_health}")
        print(f"{opponent['name']} Health: {opponent_health}\n")

# Championship logic where you fight all opponents
def play_game():
    print("Welcome to Rooster Fight Championship!\n")

    print("Choose your rooster:")
    for i, rooster in enumerate(ROOSTER_DATABASE):
        print(f"  {i + 1}. {rooster['name']} (Attack: {rooster['attack']}, Defense: {rooster['defense']})")

    choice = int(input("Enter the number of your chosen rooster: ")) - 1
    player_rooster = ROOSTER_DATABASE[choice]

    team = [player_rooster]

    display_rooster(player_rooster)
    display_rooster_art()  # Display rooster art after choosing

    print("\nYou enter the championship arena!\n")

    remaining_opponents = [r for r in ROOSTER_DATABASE if r != player_rooster]

    wins = 0

    while wins < 10:
        opponent = random.choice(remaining_opponents)
        print(f"Your opponent is {opponent['name']} (Attack: {opponent['attack']}, Defense: {opponent['defense']})\n")

        # Start the fight
        won = fight(player_rooster, opponent)

        if not won:
            print("Better luck next time!\n")
            break

        wins += 1
        print(f"You have defeated {opponent['name']}!\n")

        # Level up the player's rooster
        player_rooster['level'] += 1
        player_rooster['attack'] += 5
        display_rooster(player_rooster)
        display_rooster_art()  # Display rooster art after leveling up

        # Offer to steal the defeated rooster
        while True:
            choice = input(f"Do you want to take {opponent['name']} into your team? (yes/no): ").strip().lower()
            if choice == "yes":
                team.append(opponent)
                print(f"{opponent['name']} has joined your team!\n")
                break
            elif choice == "no":
                print(f"{opponent['name']} will not join your team.\n")
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

        # Choose rooster for next fight
        print("Choose your rooster for the next battle:")
        for i, rooster in enumerate(team):
            print(f"  {i + 1}. {rooster['name']} (Attack: {rooster['attack']}, Defense: {rooster['defense']})")

        choice = int(input("Enter the number of your chosen rooster: ")) - 1
        player_rooster = team[choice]

    if wins >= 10:
        print("Congratulations! You are the champion of the tournament!\n")

# Start the game
play_game()
