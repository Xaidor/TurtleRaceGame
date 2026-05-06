# 🐢 Turtle Racers 
---

#  Goal
### Using `turtle`, create:
- A race between **3 racers**, each a different color  
- A **user choice** of which racer will win  
- A result that tells the user if their racer **won or lost**  
- **Special power‑ups** that can completely change the outcome  

---

#  How the Game Works

```text
Step 1 → Draw the race layout (start + finish line)

Step 2 → Create and position the racers

Step 3 → Randomize each racer's forward movement

Step 4 → After 3 moves, each racer hits a Mystery Box:
             🔥 FIREBALL → Spins + slows the other racers
             ⚡ BOOST    → Gives extra distance to that racer

Step 5 → First racer to cross the finish line wins.
         The game tells the user if their chosen racer won or lost.

```
---
## Things Still To Do

### 🟪 MysteryBox Function
    - MysterBox Function
        The mysterbox would need to be called in the StartRace function. I will disappear
        after a racer reaches it at a set loctation or random loction. The locations of 
        each mysterbox must be inline of racers path. 
        For testing purposes, the powerup is given after each racers 3rd move.
    - MysteryBox Image 
        Determine the size, color, and style. Will it move or be startionary?
    - Ask user to select a racer they think will win :white_check_mark:
    - Tally loses and wins of users selected racer :white_check_mark:
    - Clean up code (In Progress) 
            - Add detailed notes
            - Section each funchtion off boldly, so its easy to find
            ` Make the code more readable
            ` Remeove unnecessary variables
            - Improve variable names for clarity
