# Goal
# Using turtle, create a race between 3 racers, each a different color.
# Ask the user to pick a racer and tell the user if their racer won or lost.
# Incorporate special moves (power-ups) that affect the race outcome.
# Step 1: Draw the race layout (start line and finish line).
# Step 2: Create and position the racers.
# Step 3: Randomize each racer's forward movement.
# Step 4: Add a twist: each racer gets a mystery box after 3 moves.
#         The mystery box gives either:
#           - a speed boost, OR
#           - a fireball attack that spins and slows the other racers.
# Step 5: Identify the winner and display the result on the screen.

# Things to still do:
#           - MysterBox Function
# The mysterbox would need to be called in the StartRace function. I will disappear
# after a racer reaches it at a set loctation or random loction. The locations of 
# each mysterbox must be inline of racers path. 
# For testing purposes, the powerup is given after each racers 3rd move.
#           - MysteryBox Image 
# Determine the size, color, and style. Will it move or be startionary?

# Import libraries 
import time
import random 
import turtle as t

#Create race layout
def Layout():
    t.pen(fillcolor="black", 
          pencolor="red", 
          pensize=10)
    t.penup()
    t.goto(200, 100)
    t.setheading(-90)
    t.pendown()
    t.forward(300)

# Create, style and positions 3 turtle racers 
def Racers():
    t_racers = []
    racer_colors = ["gold", "pink", "gray"]

    for race in range(0,len(racer_colors)):
        r = t.Turtle()
        r.shape("turtle")
        r.color(racer_colors[race])
        # Slows speed to see animation later
        r.speed(3)

        # Spaces racers vertically with gaps in between
        r.penup()
        r.goto(-200, race * 40)

        t_racers.append(r)

    return t_racers

# randomize the distance each racer moves towards the finish line
def StartRace(t_racer):
    #Declare race tracking variables 
    finish_line = 200
    racer_moves = [[],[],[]]
    totals = [0,0,0]
    travel = int()
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
                return win
            
    return totals

# Power-Ups for mystery box: Fireball or Boost
def PowerUp(racer_index, totals, t_racer):
    powerups = ["fireball", "boost"]
    activate = powerups[random.randint(0,1)]

    # Fireball will hit everyone except the racer that was given the fireball
    if activate == "fireball":
        # let the user know who got the fireball
        TempMessages(t_racer[racer_index], "FIREBALL", 1.5)

        # Loops through racers to find victims
        for target in range(0, len(totals)):
            if target != racer_index:
                # Spin-out animation 
                for _ in range(10):  # nested loop
                    t_racer[target].right(36)

                # Speed reduction for those hit damage
                totals[target] -= 15

    # Racer gets to move a bit further if given a boost
    elif activate == "boost":
        # Let the user know which racer got a boost
        TempMessages(t_racer[racer_index], "BOOST", 1.5)
        totals[racer_index] += 20
    
    return totals

# Displays what power-up the racer got from the mystery box 
def TempMessages(t_obj, message, duration=1.5):
    # Create a separate turtle so racer graphics aren't erased
    msg = t.Turtle()
    msg.hideturtle()
    msg.penup()

    # Gets location of racer to position message above racer
    x, y = t_obj.position()
    msg.goto(x, y + 20)

    # Display message
    msg.write(message, align="center", font=("Arial", 12, "bold"))
    time.sleep(duration)
    msg.clear()
    
def main():
    # Decalre Variables
    set_racers = list()
    winner = str() 

    # Draw race layout
    Layout()

    # Call Racers to create racers and store in a varible  
    set_racers = Racers()

    # Call StartRace and get the winner 
    winner = StartRace(set_racers)

    # Winner message with outline effect 
    # Set message loctation
    t.penup()
    t.goto(0,200)
    t.hideturtle()

    # Outline (balck) 
    t.color("Black")
    t.write(winner, 
            align="center", 
            font=("Comic Sans MS", 32, "bold"))

    # Fill (CadetBlue1)
    t.color("CadetBlue1")
    t.write(winner, 
            align="center", 
            font=("Comic Sans MS", 28, "bold"))
    

main()




