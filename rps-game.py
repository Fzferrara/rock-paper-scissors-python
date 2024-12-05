    
p1 = input("Write your name: ")
p2 = input("Write your name: ")

juego = False
turnos = 0
p1_points = 0
p2_points = 0

while turnos <3: 
    player1 = input(f"Hi {p1}, choose btw ROCK, PAPER, SCISSORS: ").strip().upper()
    player2 = input(f"Hi {p2}, choose btw ROCK, PAPER, SCISSORS: ").strip().upper()

    condition1 = player1 == "ROCK" and player2 == "SCISSORS"
    condition2 = player1 == "PAPER" and player2 == "ROCK"
    condition3 = player1 == "SCISSORS" and player2 == "PAPER"
 
    if player1 not in "ROCK, PAPER, SCISSORS: " or player2 not in "ROCK, PAPER, SCISSORS: ":
        print("Invalid imput, please try again")
        continue

    if player1 == player2:
        print("Tied Game")
    elif  condition1 or condition2 or condition3:
        print(f"{p1} WINS!")
        p1_points +=1
    else:   
        print(f"{p2} WINS!")
        p2_points +=1
    
    turnos += 1

if p1_points > p2_points:
    print(f"Game Over! {p1} WINS with {p1_points} over {p2_points}")
elif p1_points < p2_points:
    print(f"Game Over! {p2} WINS with {p2_points} over {p1_points}")   
else:
    print("Game Over! Tied Match")
