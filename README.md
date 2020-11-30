# Fantasy Sports League

## Introduction
For this project, you can choose your own sport and create a fantasy league for it.

## Objectives
The functionality required from this project is:

- Allow the user to choose an unlimited number of teams
- Allow the user to choose players for those teams
- Allow the user to choose an unlimited number of games
- Report the team scores after those games have been played (the implementation of this can be as simple or complex as you'd like)


You may find that some of the work for one feature overlaps with some of the work for another feature. In that case, consider creating a helper function that can be used for both cases.

### Extra challenges
If you would like to take your project a step further, consider these:

- Team Drafting
    - Have users draft from a limited pool of players
    - Don't allow duplicate player names
- Scoring
    - Track Win/Draw/Loss scores for each team
    - Create random scores for specific players, not just teams
    - After all games are played, report the winning team (and perhaps the MVP as well)
    - Figure out a way to break ties
- Play styles
    - Have all teams play each other, Round Robin Style
    - Create a tournament bracket, where losing teams are removed until there is only one team standing
- Other
    - Create a nice way to print out your data (i.e. "pretty print")

## Example
**NOTE** This is just a sample. You may choose a different format.

```
Welcome to the Fantasy Quidditch League!

How many teams are playing this season?: 2

Enter the name of team #1: Gryffindor
Enter the name of team #2: Slytherin

How many players are there per team?: 2

Enter the name of player #1 for team Gryffindor: Harry
Enter the name of player #2 for team Gryffindor: Hermione

Enter the name of player #1 for team Slytherin: Crabbe
Enter the name of player #2 for team Slytherin: Goyle

How many games are in the season?: 3

Rankings after Game 1: 
Gryffindor score: 0
Slytherin score: 1

Rankings after Game 2: 
Gryffindor score: 1
Slytherin score: 1

Rankings after Game 3: 
Gryffindor score: 1
Slytherin score: 2

Slytherin is the winner!
```