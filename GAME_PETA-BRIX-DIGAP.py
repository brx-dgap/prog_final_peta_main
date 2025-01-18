import random

def display_rooster_art():
    rooster_art = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣤⣴⣿⣧⣴⡆⠀⠀
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
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢉⣿⣿⡏⣿⡶⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠈⠁⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """
    print(rooster_art)

#mga unang pagpipiliian na manok
ROOSTER_DATABASE = [
    {"name": "Fighter", "attack": 19, "defense": 5, "level": 1},
    {"name": "Speeder", "attack": 16, "defense": 4, "level": 1},
    {"name": "Tank", "attack": 18, "defense": 8, "level": 1},
    {"name": "Champion", "attack": 20, "defense": 7, "level": 1}
]

#stats ng mga manok
def display_rooster(rooster):
    print(f"\nYour Rooster: {rooster['name']}")
    print(f"  Level: {rooster['level']}")
    print(f"  Attack: {rooster['attack']}")
    print(f"  Defense: {rooster['defense']}\n")

#coice ng player kung ano ang gagawin sa laban
def fight(rooster, opponent):
    print(f"\nThe fight begins! {rooster['name']} vs {opponent['name']}\n")
    display_rooster_art()  #para print ang manok bago laban

    rooster_health = 100
    opponent_health = 100
    block_count = 5
    rooster_blocking = False

    while rooster_health > 0 and opponent_health > 0:
        #para sa player
        print(f"\nYour turn!\n 1. Attack\n 2. Block (Remaining: {block_count})")
        try:
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
                continue  #continue para kuha ulit ng input
            
        except KeyboardInterrupt: #sir na trauma ako sa exam kaya nilagyan ko na rin here BWAHAHAAHAHHAAHAHHAHA
            print("\nThe game was interrupted by the user.")
            return False

        
        if opponent_health <= 0: #nag check if patay na kalaban
            print(f"\n{opponent['name']} is defeated! {rooster['name']} wins!\n")
            return True

        #kalaban naman ang aatake muna
        opponent_damage = random.randint(1, opponent['attack'])
        damage = max(1, opponent_damage - (rooster['defense'] + 3 if rooster_blocking else rooster['defense']))
        rooster_health -= damage
        print(f"{opponent['name']} attacks you for {damage} damage!")

        #check if patay na ba manok muuuu
        if rooster_health <= 0:
            print(f"\n{rooster['name']} is defeated! {opponent['name']} wins!\n")
            return False

        #para sa health ng manok mo anti kung hanggang kelan pa mabubuhay
        print(f"\n{rooster['name']} Health: {rooster_health}")
        print(f"{opponent['name']} Health: {opponent_health}\n")
        

#dito na yung labannnnnn 
def play_game():
    print("Welcome to Rooster Fight Championship!\n")

    print("Choose your rooster:")
    for i, rooster in enumerate(ROOSTER_DATABASE):
        print(f"  {i + 1}. {rooster['name']} (Attack: {rooster['attack']}, Defense: {rooster['defense']})")

    try:
        choice = int(input("Enter the number of your chosen rooster: ")) - 1
        if choice < 0 or choice >= len(ROOSTER_DATABASE):
            print("Invalid rooster number! Exiting the game.")
            return
        
    except ValueError: #pati dito sa peta sir nag oover think nako kaya lahat na i try except BWHAHAAHAHHAAHAH
        print("Invalid input! Please enter a valid number.")
        return

    player_rooster = ROOSTER_DATABASE[choice]

    team = [player_rooster]

    display_rooster(player_rooster)
    display_rooster_art()  #display ulit manok bakit ba para may style mwehehhehe

    print("\nYou enter the championship arena!\n")

    remaining_opponents = [r for r in ROOSTER_DATABASE if r != player_rooster]

    wins = 0

    while wins < 10:
        opponent = random.choice(remaining_opponents)
        print(f"Your opponent is {opponent['name']} (Attack: {opponent['attack']}, Defense: {opponent['defense']})\n")

        #dito na nag start labanssss
        won = fight(player_rooster, opponent)

        if not won:
            print("Better luck next time!\n")
            break

        wins += 1
        print(f"You have defeated {opponent['name']}!\n")

        # Level up ng manok mo
        player_rooster['level'] += 1
        player_rooster['attack'] += 5
        display_rooster(player_rooster)
        display_rooster_art()  #manok art ulits

        #here naman choice if want mo ba kunin manok ng kalaqban or hindi
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

        #pag nag steal ka o hindi dito ka mamimili ng manok na gagamitin mo sa labsn
        print("Choose your rooster for the next battle:")
        for i, rooster in enumerate(team):
            print(f"  {i + 1}. {rooster['name']} (Attack: {rooster['attack']}, Defense: {rooster['defense']})")

        try:
            choice = int(input("Enter the number of your chosen rooster: ")) - 1
            if choice < 0 or choice >= len(team):
                print("Invalid rooster number! Exiting the game.")
                break
            player_rooster = team[choice]
            
        except ValueError:#para sure na sure na talaga BWAHAHAHAH
            print("Invalid input! Please enter a valid number.")
            break

    if wins >= 10:#pag nanalo ka 1o beses panalo ka na sa championship
        print("Congratulations! You are the champion of the tournament!\n")


play_game()
