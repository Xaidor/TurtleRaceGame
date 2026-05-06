# ---------------------------------------------

# Import libraries 
import time 
import random 
import turtle as t

#Create race layout
# --------------------------------------------
# TODO: change background to sand color and finish line needs to be blue
# --------------------------------------------
def Layout():
    t.pen(fillcolor="black", 
          pencolor="red", 
          pensize=10)
    t.hideturtle()
    t.penup()
    t.goto(200, 190)
    t.setheading(-90)
    t.pendown()
    t.forward(300)
    
# ---------------------------------------------------------------------
# Create, style and positions 3 turtle racers 
# ---------------------------------------------------------------------
def Racers():
    t_racers = []
    racer_colors = ["gold", "pink", "gray"]

    for race in range(0,len(racer_colors)):
        r = t.Turtle()
        r.shape("turtle")
        r.color(racer_colors[race])
        # Slows speed to see animation later
        r.speed(4)

        # Spaces racers vertically with gaps in between
        r.penup()
        r.goto(-200, race * 40)

        t_racers.append(r)

    return t_racers

# ---------------------------------------------------------------------
# randomize the distance each racer moves towards the finish line
# ---------------------------------------------------------------------
def StartRace(t_racer):
    #Declare race tracking variables 
    finish_line = 400
    racer_moves = [[],[],[]]
    totals = [0,0,0]
    travel = random.randint()
    win = str()
    flag = True

    # Main loop allwos us to keep looping until winner is achieved 
    while flag == True:
        # Loops through each racer and move them forward
        for move in range(0, len(t_racer)):
            travel = random.randint(20,60)
            # Moves racer foward 
            t_racer[move].forward(travel)

            # Keeps record of each racers movement for power-up 
            racer_moves[move].append(travel)

            # Accumulates each racers movement 
            totals[move] += travel

            
            # Uses the length of each list inside racer_moves to set when PowerUp is called
            # Once each racer reaches 3 moves the power up is activated
            if len(racer_moves[move]) == 3:
                # totals will be adjucted depending on the powerup a racer recieves
                totals = PowerUp(move, totals, t_racer)

        # Check if any racer has crossed the finish line
        for winner in range(0,len(totals)):
            # Identify who wins by their total
            if totals[winner] >= finish_line:
                win = "Racer "+ str(winner +1) + " Wins"
                flag = False
                break
                
            
    return totals, win

# ---------------------------------------------------------------------
# Power-Ups for mystery box: Fireball or Boost
# Spin animation 
# Adjustment of totals[]
# PowerUp will be used inside StartRace for racer_index
# ---------------------------------------------------------------------
def PowerUp(racer_index, totals, t_racer):
    powerups = ["fireball", "boost"]
    activate = powerups[random.randint(0,1)]

    # Fireball will hit everyone except the racer that was given the fireball
    if activate == "fireball":
        # let the user know who got the fireball
        # Message dissapears after a set time
        TempMessages(t_racer[racer_index], "FIREBALL", 1.5)

        # Loops through racers to find victims
        for target in range(0, len(totals)):
            if target != racer_index:
                # Spin-out animation 
                for _ in range(10):  # nested loop
                    t_racer[target].right(36)

                # Speed reduction for those hit damage. 
                # Adjust totals[]
                t_racer[target].backward(20)
                totals[target] -= 20

    # Racer gets to move a bit further if given a boost
    elif activate == "boost":
        # Let the user know which racer got a boost
        # Message dissapears after a set time
        TempMessages(t_racer[racer_index], "BOOST", 1.5)
        totals[racer_index] += 20
    
    return totals

# ---------------------------------------------------------------------
# Displays a temporary message
# Used for racers powerup recieved (BOOST or FIREBALL)
# ---------------------------------------------------------------------
def TempMessages(t_obj, message, duration=1.5):
    # Create a separate turtle so racer graphics aren't erased
    msg = t.Turtle()
    msg.hideturtle()
    msg.penup()

    # Gets location of racer to position message above racer
    x, y = t_obj.position()
    msg.goto(x, y + 20)

    # Display message
    if message == "FIREBALL":
        msg.color("red")

    else:
        msg.color("green")

    msg.write(message, align="center", 
              font=("Arial", 8, "bold"))
    time.sleep(duration)
    msg.clear()

    
# ---------------------------------------------------------------------
# Ask user which racer they think will when
# ---------------------------------------------------------------------
def UserChoice():
    select_turtle = str()
   
    select_turtle = input("Which racer do you think will make it to the water first? (gold/pink/gray): ")

    return select_turtle

# ---------------------------------------------------------------------
# Determines if the users chosen racer won
# Returns win/loss count and a messgae
# ---------------------------------------------------------------------

def WinLose(select_turtle, totals):
    wins = int()
    loses = int()
    msg = str()
    highest = int()
    index = int()
    high_index = int()

    highest = totals[0]

    # Create index for the racers colors
    if select_turtle == "gold":
        index = 0

    elif select_turtle == "pink":
        index = 1

    elif select_turtle == "gray":
        index = 2
    
    # get the index of the highest score 
    for i in range(0, len(totals)):    
        if totals[i] > highest:
            highest = totals[i]
            high_index = i
    
    # Determine which racer actually won
    if high_index == index:
        msg = "Your racer WON!"
        wins +=1
    else:
        msg = "Your racer didn't win"
        loses += 1
    # clears text on screen for user if they wish to play again
    t.clear()

    return wins, loses, msg


# ---------------------------------------------------------------------
# MAIN GAME LOOP
# ---------------------------------------------------------------------    
def main():
    # Decalre Variables
    racers = list()
    totals = list()
    winner_msg = str()
    choice = str()
    wins = int()
    losses = int()
    msg = str()
    
    # Initialize variables
    total_wins = 0
    total_losses = 0
    play = "yes"

    # Turtles for messages 
    main_msg = t.Turtle()
    scoreboard = t.Turtle()

    # Setup message turtles
    main_msg.hideturtle()
    main_msg.penup()

    scoreboard.hideturtle()
    scoreboard.penup()

    # ---------------------------------------------
    # Run Game 
    # ---------------------------------------------
    while play == "yes":
        
        # Clear screen
        t.clear()
        # Draw race layout
        Layout()

        # Call Racers to create racers and store in a varible  
        racers = Racers()
        
        # Get users choices
        choice = UserChoice(racers)

        # Call StartRace and get the winner 
        totals, winner_msg = StartRace(racers)

        
        #---------------------------------------------------
        # ALL MESSAGES ON SCREEN
        #---------------------------------------------------
        
        # Winner message with outline effect 
        # Set message loctation
        main_msg.penup()
        multi_msg[0].goto(0,200)
        multi_msg[0].hideturtle()

        # Outline (balck) 
        multi_msg[0].color("Black")
        multi_msg[0].write(winner_msg, 
                align="center", 
                font=("Comic Sans MS", 31, "bold"))

        # Fill (CadetBlue1)
        multi_msg[0].color("CadetBlue1")
        multi_msg[0].write(winner_msg, 
                align="center", 
                font=("Comic Sans MS", 30, "bold"))
        
        # Print users wins and losses
        wins, losses, msg = WinLose(choice, totals)
        total_wins += wins
        total_losses += losses
    
        
        scoreboard.penup()
        multi_msg[1].goto(0,0)
        multi_msg[1].hideturtle

        # Let usr know if there racer won
        multi_msg[1].color("Red")
        multi_msg[1].write(msg,
                           align="center",
                           font=("Comic sans MS", 16, "normal"))

        # Tell the user how many wins or loses
        multi_msg[2].penup()
        multi_msg[2].goto(0,-100)
        multi_msg[2].hideturtle()

        multi_msg[2].color("Black")
        multi_msg[2].write("Wins: ",
                           align="center",
                           font=("Arial", 8, "normal" ))
        multi_msg[2].penup()
        multi_msg[2].goto(20,-100)
        multi_msg[2].hideturtle()
        multi_msg[2].color("Black")
        multi_msg[2].write(total_wins,
                           align="center",
                           font=("Arial", 8, "normal" ))
        
        
        multi_msg[2].penup()
        multi_msg[2].goto(0,-120)
        multi_msg[2].hideturtle()

        multi_msg[2].color("Black")
        multi_msg[2].write("Loses: ",
                           align= "center",
                           font=("Arial", 8, "normal" ))
        
        scoreboard.penup()
        multi_msg[2].goto(20,-120)
        multi_msg[2].hideturtle()
        multi_msg[2].color("Black")
        multi_msg[2].write(total_losses,
                           align="center",
                           font=("Arial", 8, "normal" ))

        # Keep playing?
        play = input("Would you like to play again? (yes/no): ")
        

main()




