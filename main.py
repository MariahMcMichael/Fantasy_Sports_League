# Get inputs.
print("Welcome to the Fantasy League Finals!\n")
Number_of_Teams = input("How many teams are playing in the finals?: ")
Teams_at_play = int(Number_of_Teams)
print()

team_names = []
for i in range(Teams_at_play):
  team_name = input("Enter the name of team #" + str(i + 1) + ": ")
  team_names.append(team_name)
print()

number_of_players = input("How many players are there per team?: ")
print()

team_players = {}
for i in range(Teams_at_play):
  team_players[i] = []
  for x in range(int(number_of_players)):
    player_name = input("Enter the name of player " + str(x + 1) + " for team " + team_names[i] + ": ")
    team_players[i].append(player_name)
  print()

Number_of_games = int(input("How many games are going to be played during this finals?: "))
print()

# The following code should print random rankings after each game - Mariah Walker
import random

# Create a new list to store team scores.
team_score = []
# This for loop counts how many teams there are, and adds a starting score of zero for each team to the score list.
for i in range(Teams_at_play):
  team_score.append(0)

# Random function for getting the winner for a single game.
def get_winner_of_game(num_of_teams):
    winner_index = random.randint(0, num_of_teams - 1)
    return winner_index

# Function for generating a new game and current rankings.
def generate_rankings(game_num):
    # Get winner.
    winner_index = get_winner_of_game(Teams_at_play)
    team_score[winner_index] += 1

    # Print current rankings.
    print("Rankings after Game " + str(game_num) + ":")
    for i in range(Teams_at_play):
      print(str(team_names[i]) + " score: " + str(team_score[i]))

# Generate rankings after each game.
for i in range(int(Number_of_games)):
  generate_rankings(i + 1)
  print()

# Determine winner.
winner_index = 0
for i in range(Teams_at_play):
  if (team_score[i] > team_score[winner_index]):
    winner_index = i
print(str(team_names[winner_index]) + " is the winner!")