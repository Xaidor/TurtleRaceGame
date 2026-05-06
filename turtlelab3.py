# ---------------------------------------------

# Import libraries 
import time 
import random 
import turtle as t

# Create race layout

def Layout():
    t.hideturtle()
    t.penup()
    t.speed(0)

    # Background
    t.bgcolor("wheat1")

    # -----------------------------
    # OCEAN FILL (right side)
    # -----------------------------
    t.goto(200, 400)
    t.color("blue4")
    t.begin_fill()

    t.setheading(0)
    t.forward(250)   # width of ocean
    t.right(90)
    t.forward(800)   # height of ocean
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(800)

    t.end_fill()


    # -----------------------------
    # WAVY PATTERN FOR FINISH LINE
    # -----------------------------
    t.goto(200,400)
    t.setheading(-90)
    t.pensize(8)
    t.pencolor("blue4")
    t.pendown()

    for wave in range(30):
        t.right(20)
        t.forward(30)
        t.left(40)
        t.forward(30)
        t.right(20)

    t.penup()

    # Lighter Wave
    t.goto(206,400)
    t.setheading(-90)
    t.pensize(8)
    t.pencolor("DodgerBlue3")
    t.pendown()

    for wave in range(30):
        t.right(20)
        t.forward(30)
        t.left(40)
        t.forward(30)
        t.right(20)

   
    
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
        r.goto(-200, race * 80)

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
                win = "Racer "+ str(winner +1) + " made it to the water first!"
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
    powerups = ["Rock", "boost"]
    activate = powerups[random.randint(0,1)]

    # Rock Will Hit Everyone Except The Racer That Was Given The Rock
    if activate == "Rock":
        # let the user know who got the rock
        # Message dissapears after a set time
        TempMessages(t_racer[racer_index], "THROW ROCK", 1.5)

        # Loops through racers to find victims
        for target in range(0, len(totals)):
            if target != racer_index:

                # Rock Animation towards targets
                RockAnimation(t_racer[racer_index], t_racer[target])

                # Spin-out animation 
                for _ in range(10): 
                    t_racer[target].right(36)

                # Speed reduction for hit damage
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
    if message == "THROW ROCK":
        msg.color("red")

    else:
        msg.color("green")

    msg.write(message, align="center", 
              font=("Arial", 8, "bold"))
    time.sleep(duration)
    msg.clear()


# ---------------------------------------------------------------------
# Animation For Rock PowerUp Attack
# ---------------------------------------------------------------------
def RockAnimation(attacker, victim):
    rock = t.Turtle()
    rock.hideturtle()
    rock.penup()
    rock.speed(0)
    rock.clear()

    # Declare Variables 
    flag = bool()
    x_distance = int()
    y_distance = int()

    # Initializing Variables 
    flag = True
    attack_travel = 5   # Steps Towards Victim
    x_distance = 0
    y_distance = 0

    # Attacker and Victim positions
    ax,ay = attacker.position()
    vx,vy = victim.position()

    while flag == True:
        # Clear rock before each move and go to new location
        rock.clear()
        rock.goto(ax, ay)

        # Draw Rock Object
        rock.color("gray50")
        rock.pendown()
        rock.begin_fill()
        rock.circle(2.3)
        rock.end_fill()
        rock.penup()
        
        # Moves the position horizontally
        if ax > vx:
            ax -= attack_travel
        elif ax < vx:
            ax += attack_travel

        # Move the position vertically
        if ay > vy:
            ay -= attack_travel
        elif ay < vy:
            ay += attack_travel

        # No Negative Numbers for Horizontal
        x_distance = ax - vx
        if x_distance < 0:
            x_distance = vx - ax

        # No negative numbers for vertical
        y_distance = ay - vy
        if y_distance < 0:
            y_distance = vy - ay

        # Stop Loop
        if x_distance < attack_travel and y_distance < attack_travel:
            flag = False
        
    
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
    result = str()
    
    # Initialize Variables
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

    # ---------------------------------------------------
    # Run Game 
    # ---------------------------------------------------
    while play == "yes":
        
        # ---------------------------------------------------
        # Screen Clearing 
        # ---------------------------------------------------
        t.clear()

        # Clear old racers 
        for r in racers:
            r.clear()
            r.hideturtle()

        # Clear All Messages 
        main_msg.clear()
        scoreboard.clear()

        # Draw Race Layout
        Layout()

        # Create Racers 
        racers = Racers()
        
        # Get Users choices
        choice = UserChoice()

        # Run race 
        totals, winner_msg = StartRace(racers)


        # ---------------------------------------------------
        # DETERMINE WINS/LOSSES 
        # ---------------------------------------------------
        wins, losses, result = WinLose(choice, totals)
        total_wins += wins
        total_losses += losses

        
        #---------------------------------------------------
        # MAIN MESSAGE 
        # Declares The Winner
        # Determines The Users Result
        #---------------------------------------------------
        main_msg.clear()
        # Set message loctation
        main_msg.goto(0,198)
       
        # Winner of the race message
        # Outline (balck) 
        main_msg.color("black")
        main_msg.write(winner_msg,
                       align="center",
                       font=("Comic Sans MS", 30, "bold"))

        # Fill (CadetBlue1)
        main_msg.goto(0,200)
        main_msg.color("CadetBlue1")
        main_msg.write(winner_msg,
                       align="center",
                       font=("Comic Sans MS", 30, "bold"))
        
        # Users Result message 
        main_msg.goto(0, 0)
        main_msg.color("red")
        main_msg.write(result,
                       align="center",
                       font=("Comic Sans MS", 16, "normal"))


        # ---------------------------------------------------
        # SCOREBOARD (Wins + Losses)
        # ---------------------------------------------------
        scoreboard.clear()

        scoreboard.goto(0, -100)
        scoreboard.color("black")
        scoreboard.write("Wins: " + str(total_wins),
                         align="center",
                         font=("Arial", 10, "normal"))

        scoreboard.goto(0, -130)
        scoreboard.write("Losses: " + str(total_losses),
                         align="center",
                         font=("Arial", 10, "normal"))

        # Keep playing?
        play = input("Would you like to play again? (yes/no): ")
        

main()