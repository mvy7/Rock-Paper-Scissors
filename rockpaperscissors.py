import time
import random

streak = 0

while True: 
  print("Welcome to Rock, Paper, Scissors!\n\nType \"1\" for 1 Player.\nType \"2\" for 2 Player.\nType \"3\" for \"How To Play\".\nType \"EXIT\" to exit the game.\n")
  game_mode = input("Select Game Mode: ").upper()
  
  while (game_mode == "1"):
    print("Player vs. Computer")
    moves = ["R", "P", "S"]
    player = input("\nEnter Rock (R), Paper (P), or Scissors (S): ").upper()
    computer = random.choice(moves)
    
    if (player == "R") and (computer == "P"):
      print("""\n
You chose: ROCK.
Computer chose: PAPER.
The Computer WON!\n""")
      streak = 0
    elif (player == "R") and (computer == "S"):
      streak += 1
      print("""\n
You chose: ROCK.
Computer chose: SCISSORS.
You WON!""")
      print(f"You are on a {streak} game winning streak!\n")
    elif (player == "R") and (computer == "R"):
      print("You both chose ROCK. It's a draw!")
      streak = 0
    elif (player == "P") and (computer == "R"):
      streak += 1
      print("""\n
You chose: PAPER.
Computer chose: ROCK.
You WON!""")
      print(f"You are on a {streak} game winning streak!\n")
    elif (player == "P") and (computer == "S"):
      print("""\n
You chose: PAPER.
Computer chose: SCISSORS.
The Computer WON!\n""")
      streak = 0
    elif (player == "P") and (computer == "P"):
      print("You both chose PAPER. It's a draw!")
      streak = 0
    elif (player == "S") and (computer == "R"):
      print("""\n
You chose: SCISSORS.
Computer chose: ROCK.
The Computer WON!\n""")
      streak = 0
    elif (player == "S") and (computer == "P"):
      streak += 1
      print("""\n
You chose: SCISSORS.
Computer chose: PAPER.
You WON!""")
      print(f"You are on a {streak} game winning streak!\n")
    elif (player == "S") and (computer == "S"):
      print("You both chose SCISSORS. It's a draw!")
      streak = 0
    else:
      print("Not a valid entry. Try Again.")
  
    retry = input("Play Again? [Yes/No]: ").upper()
  
    if (retry == "NO"):
      print()
      break
  
  
  while (game_mode == "2"):
    
    from getpass import getpass as input
    print("\nPlayer vs. Player:")
    player1 = input("\nPLAYER 1: Enter Rock (R), Paper (P), or Scissors (S): ").upper()
    player2 = input("PLAYER 2: Enter Rock (R), Paper (P), or Scissors (S): ").upper()
    
    if (player1 == "R") and (player2 == "P"):
      print("Player 2 has WON!")
    elif (player1 == "R") and (player2 == "S"):
      print("Player 1 has WON!")
    elif (player1 == "R") and (player2 == "R"):
      print("Both players chose ROCK. It's a draw!")
    elif (player1 == "P") and (player2 == "R"):
      print("Player 1 has WON!")
    elif (player1 == "P") and (player2 == "S"):
      print("Player 2 has WON!")
    elif (player1 == "P") and (player2 == "P"):
      print("Both players chose PAPER. It's a draw!")
    elif (player1 == "S") and (player2 == "R"):
      print("Player 2 has WON!")
    elif (player1 == "S") and (player2 == "P"):
      print("Player 1 has WON!")
    elif (player1 == "S") and (player2 == "S"):
      print("Both players chose SCISSORS. It's a draw!")
    else:
      print("Not a valid entry. Try Again.")

    retry = input("\nPlay Again? [Yes/No]: ").upper()
    
    if (retry == "NO"):
      print()
      break

  while (game_mode == "3"):
    print("""\n
Type "1" for 1 Player mode, where you'll play against the computer.
Type "2" for 2 Player mode, where two players can play against each other.
(Note: Your inputs in 2 Player mode will be hidden to prevent spoliers).

For either game mode, you'll be prompted to enter your choice (Rock, Paper, or Scissors) by typing "R," "P," or "S."

The rules are as follows:
- Rock beats Scissors.
- Paper beats Rock.
- Scissors beat Paper.

Enjoy playing Rock, Paper, Scissors with your friends or against the computer!\n
    """)
    time.sleep(3)
    break

  if (game_mode == "EXIT"):
    print("Exiting the game...")
    time.sleep(2)
    print("Game Exited.")
    break
    
    
  if (game_mode != "1") and (game_mode != "2") and (game_mode != "3") and (game_mode != "EXIT"):
    print("Not a valid input.\n")
    

  