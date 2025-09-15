import random, copy
from colorist import Color
from colorist import BgColor


class Cards:
    def __init__(self, title, description, energy_requirement, damage_to_enemy, health_to_player):
        self.title = title
        self.description = description
        self.energy_requirement = energy_requirement
        self.damage_to_enemy = damage_to_enemy
        self.health_to_player = health_to_player

    def __str__(self):
        return f"{self.title}"


placeholder_damage_to_enemy = 0
placeholder_health_to_player = 0

# Format:
# CX=Cards("Title",
#       "Description",
#       energy, damage_to_enemy (Positive int), health_to_player)
C1 = Cards("Apprentice",
           f"{Color.CYAN}Multiplies{Color.OFF} the effects of the next card by {Color.CYAN}2{Color.OFF} for {Color.YELLOW}2 energy{Color.OFF}.",
           2, 0, 0)
C2 = Cards("Soldier",
           f"Deals {Color.RED}4 damage{Color.OFF} for {Color.YELLOW}3 energy{Color.OFF}.",
           3, 4, 0)
C3 = Cards("Minion",
           f"Deals {Color.RED}2 damage{Color.OFF} for {Color.YELLOW}1 energy{Color.OFF}.",
           1, 2, 0)
C4 = Cards("Feral Dog",
           f"{Color.MAGENTA}50% chance{Color.OFF} of attacking enemy for {Color.RED}12 damage{Color.OFF}. {Color.MAGENTA}50% chance{Color.OFF} of attacking self for {BgColor.RED}2 health{Color.OFF}. Costs {Color.YELLOW}4 energy{Color.OFF}.",
           4, placeholder_damage_to_enemy, placeholder_health_to_player)
C5 = Cards("Goblin",
           f"{Color.RED}Steals{Color.OFF} {Color.GREEN}1 health{Color.OFF} from enemy for {Color.YELLOW}1 energy{Color.OFF}.",
           1, 1, 1)
C6 = Cards("Bomb",
           f"Deals {Color.RED}10 damage{Color.OFF} to enemy and {BgColor.RED}5 damage{Color.OFF} to self. Costs {Color.YELLOW}1 energy{Color.OFF}. One-time use.",
           1, 10, -5)
C7 = Cards("Archer",
           f"{Color.MAGENTA}50% chance{Color.OFF} of dealing {Color.RED}2 damage{Color.OFF}. {Color.MAGENTA}25% chance{Color.OFF} chance of dealing {Color.RED}5 damage{Color.OFF}. {Color.MAGENTA}25% chance{Color.OFF} chance of missing. Costs {Color.YELLOW}2"
           f" energy{Color.OFF}.",
           2, placeholder_damage_to_enemy, 0)
C8 = Cards("Fairy",
            f"Restores {Color.GREEN}3 health{Color.OFF} for {Color.YELLOW}2 energy{Color.OFF}.",
            2, 0, 3)
C9 = Cards("Sorcerer",
            f"Restores {Color.YELLOW}1 energy{Color.OFF} at the cost of {Color.RED}4 health{Color.OFF}.",
            -1, 0, -4)
C10 = Cards("Mage",
           f"{Color.CYAN}Multiplies{Color.OFF} the effects of the next card by {Color.CYAN}2{Color.OFF} and deals {Color.RED}1 damage{Color.OFF}. Costs {Color.YELLOW}1 energy{Color.OFF}.",
           1, 1, 0)
C11 = Cards("Warrior",
           f"Deals {Color.RED}7 damage{Color.OFF} for {Color.YELLOW}4 energy{Color.OFF}.",
           4, 7, 0)
C12 = Cards("Tamed Dog",
            f"{Color.MAGENTA}75% chance{Color.OFF} chance of attacking enemy for {Color.RED}12 damage{Color.OFF}. Costs {Color.YELLOW}3 energy{Color.OFF}.",
            3, placeholder_damage_to_enemy, 0)
C13 = Cards("Robber",
            f"{Color.RED}Steals{Color.OFF} {Color.GREEN}4 health{Color.OFF} from enemy for {Color.YELLOW}3 energy{Color.OFF}.",
            3, 4, 4)
C14 = Cards("Witch",
            f"{Color.MAGENTA}75% chance{Color.OFF} chance to heal {Color.GREEN}8 health{Color.OFF} for {Color.YELLOW}2 energy{Color.OFF}.",
            2, 0, placeholder_health_to_player)
C15 = Cards("Warlock",
            f"{Color.MAGENTA}75% chance{Color.OFF} chance to deal {Color.RED}8 damage{Color.OFF} for {Color.YELLOW}2 energy{Color.OFF}.",
            2, placeholder_damage_to_enemy, 0)
C16 = Cards("Knight",
            f"Deals {Color.RED}15 damage{Color.OFF} for {Color.YELLOW}5 energy{Color.OFF}.",
            5, 15, 0)
C17 = Cards("Ranger",
            f"Deals {Color.RED}3 damage{Color.OFF} for {Color.YELLOW}1 energy{Color.OFF}.",
            1, 3, 0)
C18 = Cards("Assassin",
            f"Deals {Color.RED}13 damage{Color.OFF} for {Color.YELLOW}2 energy{Color.OFF}. One-time use.",
            2, 13, 0)
C19 = Cards("Loyal Dog",
            f"{Color.MAGENTA}100% chance{Color.OFF} of attacking enemy for{Color.RED} 12 damage{Color.OFF}. {Color.MAGENTA}50% chance{Color.OFF} to heal self for {Color.GREEN}3 health{Color.OFF}. Costs {Color.YELLOW}2 energy{Color.OFF}.",
            3, 12, placeholder_health_to_player)
C20 = Cards("Martyr",
            f"Sacrifices {Color.RED}5 health{Color.OFF} to deal {Color.RED}18 damage{Color.OFF} for {Color.YELLOW}4 energy{Color.OFF}.",
            4, 18, -5)
C21 = Cards("Wizard",
            f"{Color.CYAN}Multiplies{Color.OFF} the effects of the next card by {Color.CYAN}3{Color.OFF} at the cost of {Color.YELLOW}3 energy{Color.OFF} and {BgColor.RED}5 health{Color.OFF}.",
            3, 0, -5)
# This is an Easter egg where the title will be revealed after the player selects and uses the card.
C22 = Cards("???",
            "???",
            3, 10, 10)


class Levels:
    def __init__(self, description, enemies, max_enemy_health, base_attack, cards):
        self.description = description
        self.enemies = enemies
        self.max_enemy_health = max_enemy_health
        self.base_attack = base_attack
        self.cards = cards

    def __str__(self):
        return f"{self.description}"


# Format:
# LX=Levels("Description",
#       ["enemies"],
#       [max_enemy_health], [base_attack], [cards])
L1 = Levels("You are at the bridge. There is a watchman here.",
            ["The Watchman"],
            [18], [3], [C9, C10, C11, C12, C13])
L2 = Levels(
    "With no guard, you can cross the bridge. Now, you are at the entrance hall. There are some confused visitors here.\n"
    "They mention something about a dragon, but they stop talking as soon as they spot you.",
    ["Ambassador Alphys", "Barron Beard", "Count Cornball"],
    [6, 6, 6], [1, 1, 1], [C9, C10, C11, C12, C13, C14, C15])
L3 = Levels(
    'You approach the stairs but are stopped by a gangly teenager. "You'"'re not allowed in here yet. You have to take a number." '"\n'
    "You shudder, knowing you have to cut this innocent child's life short. He takes out a gun and his smile twists wider.\n"
    "Never mind, let's kill this kid.",
    ["The Teenager"],
    [7], [10], [C9, C10, C11, C12, C13, C14, C15])
L4 = Levels('After the slaughter, you make your way up the stairway.\n'
            'You hear "seize them!" and you find you are being chased by a general and his right hand man!',
            ["The General", "The Right Hand Man"],
            [20, 18], [3, 2], [C10, C11, C12, C13, C14, C15, C16, C17])
L5 = Levels("Whew. After the fight, you can safely climb the stairs.\n"
            "You search each room for the king, but find his advisor in his office instead.\n"
            "When he looks at you, he suspiciously buries the notes he was reading in some other papers.\n"
            "He takes out a knife.",
            ["The Advisor"],
            [16], [5], [C11, C12, C13, C14, C15, C16, C17, C18])
L6 = Levels(
    "That advisor was surprisingly tough. As you catch your breath, you find a cat, trembling in fear under the advisor's desk.",
    ["The Cat"],
    [1], [1], [C13, C14, C15, C16, C17, C18, C19])
L8 = Levels("You see the notes the advisor was trying to hide and decide to pocket them. After some more searching, you find the king's bedroom.\n"
            "Unfortunately, it's blocked by two heavily armored guards.",
            ["Guard #1", "Guard #2"],
            [22, 22], [2, 2], [C14, C15, C16, C17, C18, C19, C20])
L7 = Levels(" Before you enter, you pause. What's that rumbling in the distance?",
            ["Backup #1", "Backup #2", "Backup #3", "Backup #4", "Backup #5"],
            [9, 9, 9, 9, 9], [2, 2, 2, 2, 2], [C15, C16, C17, C18, C19, C20])
L9 = Levels("You enter the room and see the king isn't there. But the queen is. And she's very, very angry.",
            ["The Queen"],
            [25], [8], [C17, C18, C19, C20, C21])
L10 = Levels("After the fight, you decide to rest and read the notes you've gotten from the advisor's office.\n"
             "You discover that there's a dragon headed to the kingdom, due to arrive any minute now.\n"
             "Instead of telling the public, he embezzled funds to fortify the basement of the castle.\n"
             "He planned to hide in the dungeons while the dragon burned the kingdom above him.\n"
             "You rush back down the stairs to find him and teach him a lesson. He finds you first.",
             ["The King"],
             [35], [7], [C18, C19, C20, C21, C22])
L11 = Levels("The king is dead. There is one more thing to do to keep the kingdom safe.",
             ["The Dragon"],
             [40], [10], [C18, C19, C20, C21, C22])


# These functions take the card and the current buff and returns the change in health.
def enemy_health_change(self, buff):
    change = self.damage_to_enemy * buff
    if change != 0:
        print(f"You hit the enemy for {Color.RED}{change} damage{Color.OFF}.\n")
    return change


def player_health_change(self, buff):
    change = self.health_to_player * buff
    if change < 0:
        print(f"You hit yourself for {BgColor.RED}{-1 * change} damage{Color.OFF}.\n")
    elif change > 0:
        print(f"You healed yourself for {Color.GREEN}{change} health{Color.OFF}.\n")
    return change


# This is a function that is called when the player needs to make an input.
def get_input(number_of_options):
    # This makes a list of valid inputs
    valid_options = set()
    for j in range(0, number_of_options):
        valid_options.add(str(j + 1))

    # Ensures the player inputs a valid option and prints a message if they don't put a valid input.
    player_input = input()
    while player_input not in valid_options:
        if number_of_options == 1:
            message = "the number 1"
        elif number_of_options == 2:
            message = "the number 1 or the number 2"
        else:
            message = f"a number 1 through {number_of_options}"
        print(f"I don't understand that input. Please type {message}.")
        player_input = input()

    # After the player escapes the while loop, return their valid input.
    return player_input


# This is the start of the game loop.
game = 1
while game:
    print(
        "The kingdom is crippled from lack of funds. You suspect the king is embezzling money for his own selfish interests. \n"
        "You assemble a team of revolutionaries (and one stray dog) to invade the castle and get some answers.\n")
    print(f"You will gain {Color.YELLOW}3 energy{Color.OFF} each turn. You can save unlimited energy.\n"
          "You can play as many cards as you want each turn, as long as you have the energy to play them.\n"
          "After you play a card it will be discarded, and a new card will be drawn and added to the bottom of your hand.\n"
          "If the draw pile is empty, all discarded cards will be added to the draw pile.\n"
          "Some cards will give buffs to the next card played. These stack and stay between turns, but not between levels.\n"
          "As you progress through the castle, you may choose to recruit new cards, which represent new units to fight for you.\n"
          "Or, you may dismiss units that will hold you back from your quest. Or, you can choose to improve yourself.\n\n"
          "Now, let's take this castle.\n")

    max_player_health = 15
    player_death_check = 0
    cat_check = 0
    bennett_check = 0
    max_hand_size = 5
    hand = []
    discard = [C1, C2, C3, C4, C5, C6, C7, C8]
    draw = []

    # This is the start of the level loop.
    for level_number in range(1, 12):
        level = eval("L" + str(level_number))
        print(f"You are on Level {level_number}.\n")
        print(f"{level.description}\n")

        # Loading enemy information into these lists allows for enemies to be deleted when killed.
        current_enemies = copy.deepcopy(level.enemies)
        current_enemy_health = copy.deepcopy(level.max_enemy_health)
        current_enemy_attack = copy.deepcopy(level.base_attack)
        player_health = max_player_health
        player_win_check = 0

        energy = 0
        buff = 1
        turn = 1

        # This is the start of the turn loop.
        while turn:
            energy = energy + 3
            players_turn = 1

            # This is the start of the player's turn loop. It is a loop because players can play multiple cards per turn.
            while players_turn == 1:
                i = 0
                for enemy in range(0, len(current_enemies)):
                    print(f"{current_enemies[i]} Health: {Color.GREEN}{current_enemy_health[i]}{Color.OFF}")
                    i = i + 1
                print(f"Your Health: {Color.GREEN}{player_health}/{max_player_health}{Color.OFF}.")
                print(f"Your Energy: {Color.YELLOW}{energy}{Color.OFF}.\n")

                # If draw is empty, shuffle discard and switch piles.
                if not draw:
                    random.shuffle(discard)
                    draw = discard
                    discard = []
                if len(hand) < max_hand_size:
                    cards_drawn_number = max_hand_size - len(hand)
                    hand = hand + draw[:cards_drawn_number]
                    del draw[:cards_drawn_number]

                # This is where the player chooses a card
                print("You may:")
                print("1. Play a card.")
                print("2. End your turn.")

                # Checking if it's the special cat level.
                if level_number == 6:
                    print("3... Pet the cat?")
                    player_main_input = get_input(3)
                    if player_main_input == "3":
                        print("You reach for the cat. They seems friendly, so you pet them. You feel...enlightened.")
                        print(f"Your max health has gone up by {Color.GREEN}10{Color.OFF}.")

                        # The cat check will result in a different message at the end of the game.
                        cat_check = 1
                        players_turn = 0
                        turn = 0
                        player_win_check = 1
                        max_player_health = max_player_health + 10
                        break
                else:
                    player_main_input = get_input(2)
                if player_main_input == "1":
                    print("Here is your hand. Type which card to play.")

                    # Printing every card in the hand.
                    i = 0
                    for card in hand:
                        i = i + 1
                        print(f"{i}. {card}: {card.description}")

                    # Getting player's input for which card to play.
                    player_card_input = get_input(max_hand_size)
                    picked_card = hand[int(player_card_input) - 1]

                    # Checking if the played card's energy requirements doesn't exceed current energy
                    if picked_card.energy_requirement > energy:
                        print(
                            "That card costs more energy than you currently have. You'll be taken back to the previous choice.\n")
                        # The player will return to the start of the loop.
                        continue
                    elif picked_card.energy_requirement > 0:
                        energy = energy - picked_card.energy_requirement

                    # Sorcerer has negative energy since it gives energy to the player. It is affected by buffs.
                    else:
                        print(f"The Sorcerer drained {Color.RED}4 health{Color.OFF} and restored {Color.YELLOW}1 energy{Color.OFF}.\n")
                        energy = energy - picked_card.energy_requirement * buff

                    # Some cards use randomness so they need to be changed.
                    # The function inputs the card played and changes the property of the card if necessary.
                    random_number = random.randint(0, 3)
                    if picked_card.title == "Feral Dog":
                        if random_number == 0 or random_number == 1:
                            picked_card.damage_to_enemy = 12
                            picked_card.health_to_player = 0
                        else:
                            picked_card.damage_to_enemy = 0
                            picked_card.health_to_player = -2
                            print("The Feral Dog attacked you instead of the enemy.\n")
                    elif picked_card.title == "Archer":
                        placeholder_health_to_player = 0
                        if random_number == 0:
                            picked_card.damage_to_enemy = 5
                        elif random_number == 1 or random_number == 2:
                            picked_card.damage_to_enemy = 2
                        else:
                            picked_card.damage_to_enemy = 0
                            print("The Archer missed.\n")
                    elif picked_card.title == "Tamed Dog":
                        picked_card.health_to_player = 0
                        if random_number == 0:
                            picked_card.damage_to_enemy = 0
                            print("The Tamed Dog misunderstood your command and did nothing.\n")
                        else:
                            picked_card.damage_to_enemy = 12
                    elif picked_card.title == "Witch":
                        picked_card.damage_to_enemy = 0
                        if random_number == 0:
                            picked_card.health_to_player = 0
                            print("The Witch's potion didn't work this time.\n")
                        else:
                            picked_card.health_to_player = 8
                    elif picked_card.title == "Warlock":
                        picked_card.health_to_player = 0
                        if random_number == 0:
                            picked_card.damage_to_enemy = 0
                            print("The Warlock's spell missed the enemy.\n")
                        else:
                            picked_card.damage_to_enemy = 8
                    elif picked_card.title == "Loyal Dog":
                        if random_number == 0 or random_number == 1:
                            picked_card.health_to_player = 3
                        else:
                            picked_card.health_to_player = 0

                    # Picking which enemy to target. If the card does no damage, or there's only one enemy, it does not need a target.
                    if len(current_enemies) > 1 and picked_card.damage_to_enemy != 0:
                        print("Pick which enemy to target:")
                        i = 0
                        for enemy in current_enemies:
                            i = i + 1
                            print(f"{i}. {enemy}")
                        player_enemy_input = get_input(len(current_enemies))
                        target_enemy = int(player_enemy_input) - 1
                    else:
                        target_enemy = 0

                    # Calculating effects on enemy health.
                    current_enemy_health[target_enemy] = current_enemy_health[target_enemy] - enemy_health_change(picked_card, buff)
                    if current_enemy_health[target_enemy] <= 0:
                        print(f"You have defeated {current_enemies[target_enemy]}!\n")
                        current_enemies.pop(target_enemy)
                        current_enemy_health.pop(target_enemy)
                        current_enemy_attack.pop(target_enemy)
                        if len(current_enemies) == 0:
                            player_win_check = 1
                            players_turn = 0
                            turn = 0
                            break

                    # Calculating effects on player health.
                    player_health = player_health + player_health_change(picked_card, buff)
                    if player_health > max_player_health:
                        player_health = max_player_health
                    elif player_health <= 0:
                        turn = 0
                        player_death_check = 1
                        break

                    # Cards that add buffs.
                    if picked_card.title in {"Apprentice", "Mage"}:
                        buff = buff * 2
                        print(f"The {picked_card.title} cast a spell. Now, your next card will have {Color.CYAN}{buff} times{Color.OFF} the effect.\n")
                    elif picked_card.title in {"Wizard", "???","Bennett"}:
                        buff = buff * 3
                        if picked_card.title == "Wizard":
                            print(f"The Wizard cast a spell. Now, your next card will have {Color.CYAN}{buff} times{Color.OFF} the effect.\n")
                        else:
                            # Easter egg card.
                            if picked_card.title == "???":
                                picked_card.title = "Bennett"
                                picked_card.description = f"An adventurer from another world. Multiplies the effects of the next card by {Color.CYAN}3{Color.OFF}, deals {Color.RED}10 damage{Color.OFF}, and gives {Color.GREEN}10 health{Color.OFF}. Costs {Color.YELLOW}3 energy{Color.OFF}."

                            print(f"{picked_card.title} used his burst. Now, your next card will have {Color.CYAN}{buff} times{Color.OFF} the effect.\n")
                    else:
                        buff = 1

                    # Discarding cards.
                    hand.remove(picked_card)


                    # Single-use cards are not added to the discard pile.
                    if picked_card.title not in {"Bomb", "Assassin"}:
                        discard.append(picked_card)

                    # If a single-use card was used, hand size may need to be decreased.
                    elif len(hand) + len(draw) + len(discard) < 5:
                        max_hand_size = len(hand) + len(draw) + len(discard)

                # If player_main_input was 2, they chose to end their turn.
                else:
                    players_turn = 0

                # End of the players_turn loop.
            # This is the start of the enemies' turn.
            if player_win_check == 0 and player_death_check == 0:
                i = 0
                for enemy in current_enemies:
                    final_damage = current_enemy_attack[i] + random.randint(0, 1 + int(current_enemy_attack[i] / 5))
                    print(f"{enemy} hit you for {BgColor.RED}{final_damage} damage{Color.OFF}.")
                    player_health = player_health - final_damage
                    i = i + 1
                    if player_health <= 0:
                        turn = 0
                        player_death_check = 1
                        break
                print()
            # End of the turn loop.
        if player_death_check == 1:
            print("Do you want to quit the game or play again?")
            print("1. Quit game.")
            print("2. Play again.")
            player_death_input = get_input(2)
            if player_death_input == "1":
                print("Okay! Bye!")
                exit()
            else:
                print("Returning to start...")
                break
                # Checking if the player is on the 11th level.
        elif level_number == 11:
            print("It is over. The kingdom is safe.")
            print("You weep for the people in the castle you have slaughtered.")
            if cat_check == 0:
                print("You even killed a cat.")
                print(
                    "For that, you are full of regret. You think, if you could do it all over again, maybe you'd make a different choice.\n")
            else:
                print(
                    "Still, you saved the rest of the kingdom, not just from a tyrannical king, but a horrible dragon.\n")
                print("If you had to, you'd do it all over again.\n")
            print("Do you want to quit the game or play again?")
            print("1. Quit game.")
            print("2. Play again.")
            player_death_input = get_input(2)
            if player_death_input == "1":
                print("Okay! Bye!")
                exit()
            else:
                print("Returning to start...")
                break
        elif player_win_check == 1:
            print("You win the level! Now, choose a reward:")
            print(f"1. Increase max health by {Color.GREEN}8{Color.OFF}.")
            print("2. Choose a new card to add to your deck.")
            print("3. Discard a card permanently.")
            player_win_input = get_input(3)
            if player_win_input == "1":
                print(
                    f"Your max health has increased from {Color.GREEN}{max_player_health}{Color.OFF} to {Color.GREEN}{max_player_health + 10}{Color.OFF}")
                max_player_health = max_player_health + 10
            elif player_win_input == "2":
                print("Choose a new card:")
                new_cards = level.cards
                random.shuffle(new_cards)
                new_cards = new_cards[:3]
                for i in range(0, 3):
                    print(f"{i + 1}. {new_cards[i]}: {new_cards[i].description}")
                new_card_input = get_input(3)
                new_card = new_cards[int(new_card_input) - 1]
                print(f"{new_card} has been added to your deck.\n")
                if max_hand_size < 5:
                    max_hand_size = max_hand_size + 1
                    hand.append(new_card)
                else:
                    draw.insert(0, new_card)
            else:
                print("Choose which card to discard:")
                temporary_cards = hand + draw + discard
                for i in range(0, len(temporary_cards)):
                    print(f"{i + 1}. {temporary_cards[i]}: {temporary_cards[i].description}")
                player_discard_input = get_input(len(temporary_cards))
                discarded_card = temporary_cards[int(player_discard_input) - 1]
                if discarded_card in hand:
                    hand.remove(discarded_card)
                elif discarded_card in draw:
                    draw.remove(discarded_card)
                elif discarded_card in discard:
                    discard.remove(discarded_card)
                if len(temporary_cards) < 6:
                    max_hand_size = max_hand_size - 1
                print(f"{discarded_card} has been removed from the deck.\n")
