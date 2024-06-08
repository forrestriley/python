import random


# function "roll" returns a random value between 1 and 6
def roll():
  min_value = 1
  max_value = 6
  roll = random.randint(min_value, max_value)

  return roll

# value = roll()
# print(value)

# while True asks for input again if non valid value is entere5
while True:
  players = input("Enter the number of players (2-4): ")
  if players.isdigit():
    players = int(players)
    if 2 <= players <= 4:
      break
    else:
      print("Must be between 2 and 4 players")
  else:
    print("Invalid Entry, Try Again")

print(players)

max_score = 50
player_scores = [0 for _ in range(players)]

# print(player_scores)

while max(player_scores) < max_score:

  for player_index in range(players):
    print("\nPlayer", player_index + 1, "It is your turn.")
    print("you have: ", player_scores[player_index], "points\n")
    current_score = 0

    while True:

      should_roll = input("Would you like to roll? (Y)")
      if should_roll.upper() != "Y":
          break
      
      value = roll()
      if value == 1:
        print("You rolled a 1, turn over")
        current_score = 0
        break
      else:
        current_score += value
        print("You rolled a:", value)
      
      print("Your Score is:", current_score)


  player_scores[player_index] += current_score
  print("Your total score is:", player_scores[player_index])

max_score = max(player_scores)
winning_index = player_scores.index(max_score)
print("Player numer", winning_index + 1, "has won! They had:", max_score, "points")





