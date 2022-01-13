"""This is a quiz that helps you figure out which Outer Banks Pogue you are."""

__author__ = "730530326"


from random import randint

days_of_the_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
list_of_nbateams = ['Atlanta Hawks', 'Boston Celtics', 'Brooklyn Nets', 'Charlotte Hornets', 'Chicago Bulls', 'Cleveland Cavaliers', 'Dallas Mavericks', 'Denver Nuggets', 'Detroit Pistons', 'Golden State Warriors', 'Houston Rockets', 'Indiana Pacers', 'LA Clippers', 'LA Lakers', 'Memphis Grizzlies', 'Miami Heat', 'Milwaukee Bucks', 'Minnesota Timberwolves', 'New Orleans Pelicans', 'New York Knicks', 'Oklahoma City Thunder', 'Orlando Magic', 'Philadelphia Sixers', 'Phoenix Suns', 'Portland Trail Blazers', 'Sacramento Kings', 'San Antonio Spurs', 'Toronto Raptors', 'Utah Jazz', 'Washington Wizards']
rankings = [72, 75, 87, 35, 76, 47, 68, 79, 39, 77, 52, 77, 82, 93, 48, 82, 84, 53, 47, 53, 30, 46, 85, 76, 61, 41, 47, 58, 78, 45]
BASKETBALL = "\U0001F3C0"
points: int
player: str
your_team: str
your_position: int
attributes: list[str]
ratings: list[int]
index: int
records: list[int]
points_p: float
assists: float
rebounds: float
steals: float
blocks: float


def greet() -> None:
    """This function greets the player, contextualizes the game, and asks for player's name."""
    global player
    player = str(input("What is your name?"))
    print(f"Welcome to the custom NBA Season game {BASKETBALL}! In this game, you will become an NBA player for a season!") 
    print(f"{player}, congratulations! You are one step away from becoming an NBA player! After going undrafted in the NBA 2021 Draft, three teams are offering you a contract. These teams are {list_of_nbateams[randint(0, 29)]} , {list_of_nbateams[randint(0, 29)]} and {list_of_nbateams[randint(0, 29)]}")
    return None


def team_setup() -> None:
    """This procedure presents the opportunity to the player to choose one of three teams offering contracts, set up their position, and then shows them their initial position-specific ratings."""
    global your_team
    counter = 0
    while counter == 0:
        your_team = str(input("Which team would you like to sign with? If you do not want to accept one of these contracts, you can type the word done. (Please type out name exactly as you see it, note capitalization and spacing)"))
        if your_team == 'done':
            print("Each of the three teams sends you well wishes, and you choose a different career. The amount of work you put in to even receive one NBA contract is incredible, and you should be proud of yourself regardless, no matter where life takes you. Your final points amount to 0, but in our hearts you've earned an infinite amount of points. Congratulations, and goodbye!")
            counter += 1
            return None
        else:
            if your_team not in list_of_nbateams:
                print("Uh oh! You may have made a typing error - we can't find that team in the NBA!")
            else:
                counter += 1

    print("Congrats! Which position do you want to play?")
    global your_position
    your_position = int(input("Type in 1 for point guard, 2 for shooting guard, 3 for small forward, 4 for power forward, or 5 for center."))
    print("Oh boy. We've got 7 days until the season starts and these are your current ratings, or how good you are at each aspect of the game:")
    global attributes
    global ratings
    if your_position == 1:
        attributes_p = ['3pt', '2pt', 'finishing', 'passing', 'defense', 'rebounding']
        ratings_p = [25, 20, 25, 35, 15, 10]
        ratings = ratings_p
        attributes = attributes_p
        for i in range(len(attributes_p)):
            print(f"For {attributes_p[i]} your rating is {(ratings_p[i])}")
    if your_position == 2:
        attributes_s = ['3pt', '2pt', 'finishing', 'passing', 'defense', 'rebounding']
        ratings_s = [35, 30, 20, 10, 15, 10]
        attributes = attributes_s
        ratings = ratings_s
        for i in range(len(attributes_s)):
            print(f"For {attributes_s[i]} your rating is {(ratings_s[i])}")
    if your_position == 3:
        attributes_sf = ['3pt', '2pt', 'finishing', 'passing', 'defense', 'rebounding']
        ratings_sf = [20, 20, 20, 20, 20, 20]
        attributes = attributes_sf
        ratings = ratings_sf
        for i in range(len(attributes_sf)):
            print(f"For {attributes_sf[i]} your rating is {(ratings_sf[i])}")
    if your_position == 4:
        attributes_pf = ['3pt', '2pt', 'finishing', 'passing', 'defense', 'rebounding']
        ratings_pf = [10, 15, 25, 5, 35, 25]
        attributes = attributes_pf
        ratings = ratings_pf
        for i in range(len(attributes_pf)):
            print(f"For {attributes_pf[i]} your rating is {str(ratings_pf[i])}")
    if your_position == 5:
        attributes_c = ['3pt', '2pt', 'finishing', 'passing', 'defense', 'rebounding']
        ratings_c = [0, 10, 35, 5, 25, 40]
        attributes = attributes_c
        ratings = ratings_c
        for i in range(len(attributes_c)):
            print(f"For {attributes_c[i]} your rating is {(ratings_c[i])}")


def trainingandseasonsimulation() -> int:
    """Allows user to choose which aspect of their game to train each day for 7 days before the NBA season starts. Simulates entire season, calculates statistics based on updated ratings, team record based on team rating and the player's effect on their team's rating, and then assigns points to player based on these numbers. Prints faux headlines specific to player and team based on player's performance."""
    print("Okay, we've got 7 days to train for the upcoming NBA season.")

    global ratings
    global attributes
    
    for i in range(7, 0, -1):
        print(str(i) + "days left until NBA season.") 
        training = int(input("What do you want to train today? Type in 0 for 3pt, 1 for 2pt, 2 for finishing, 3 for passing, 4 for defense, or 5 for rebounding. You will add 30 points to whichever attribute you select."))
        ratings[training] = ratings[training] + 30
 
    print("The NBA season is here! These are your new ratings!")
    for i in range(len(attributes)):
        print(f"For {attributes[i]} your rating is {(ratings[i])}")

    global index
    index = list_of_nbateams.index(your_team)
    rankings[index] = int(rankings[list_of_nbateams.index(your_team)] + (sum(ratings) / len(ratings)) / 5)
    global records
    records = []
    global your_position

    for i in range(len(list_of_nbateams)):
        wins = 0
        for j in range(len(rankings)):
            if i != j:
                total = rankings[i] + rankings[j]
                if randint(0, total) <= rankings[i]:
                    wins += 1
            else:
                None
        records.append(int(2.827 * wins))

    global points_p
    global assists
    global rebounds
    global steals
    global blocks

    points_p = (ratings[0] / 10 + ratings[1] / 15 + ratings[2] / 15)
    assists = ratings[3] / 10
    rebounds = ratings[5] / 12
    steals = ratings[4] / 100 + randint(0, 1)
    blocks = ratings[4] / 100 + randint(0, 1)

    print("We are halfway through the season. Let's see what the headlines are saying now: ")
    global points
    if records[index] > 50:
        points = 15
    elif records[index] > 41:
        points = 10
    else:
        points = 5
    
    if points_p > 15 or assists > 4 or rebounds > 6 or steals > 1.5 or blocks > 1.5:
        points += 10
        print(f"From {your_team} Digest: ")
        print(f"{player} trying to make presence known as undrafted rookie in NBA")
    else:
        print("From ESPN: ")
        print(f"Ugly rookie season for undrafted {your_team} {your_position}, {player}")
    if points_p > 20:
        points += 15
        print(f"From the {your_team} Daily: ")
        print(f"{player} is surprising in rookie year as reliable scoring option for the {your_team}")
    if assists > 8:
        points += 15
        print(f"From the {your_team} Report: ")
        print(f"Undrafted rookie {player} is showing streaks of sky-high playmaking potential in first year")
    if rebounds > 8:
        points += 15
        print("From House of Highlights: ")
        print(f"House of Highlights rebounder to watch: undrafted rookie {player}")
    if (steals > 1 and blocks > 1) or steals > 2 or blocks > 2:
        points += 15
        print(f"From The {your_team} Times:")
        print(f"Promising year-round defensive potential from newly signed {player}")
    if points_p >= 4 and assists >= 6 and rebounds >= 6:
        points += 15
        print(f"From the {your_team} Weekly: ")
        print(f"All-around impact from {your_team} {your_position}, {player}")

    return points


def final(pointsnumber: int) -> int:
    """This is the function for requirement number 4. This function presents the player an in-game scenario. They are always down two, and they are in a timeout, and they have the opportunity to choose to either take the shot or have someone else on their team take the shot. If they choose to take the shot, then they get to play a little game where they have one chance to guess a random number 1-3. If they guess the number correctly, then they hit the shot, and they add 5 points to their total point value, but if they miss, they lose 5, and if they defer, they lose 2."""
    score = randint(80, 120)
    time = randint(0, 7)
    global index
    global records
    print(f"You are playing the {list_of_nbateams[randint(0, 29)]} right now and the score is {score} to {score-2}. You are down, but you have the chance to either tie or win with {time} seconds on the clock. Your team is currently in the timeout, and they are drawing up a play that will end up in you shooting the final shot. Do you take on the challenge or do you defer to one of the more seasoned, veteran NBA players on your team? If you make this shot, then your final points will increase by five. If you miss, your points will decrease by five. If you defer, your points will decrease by 2.")
    last_minute_decision = str(input("Type in shot to take the shot or defer to pass it off to someone else."))
    if last_minute_decision == 'shot':
        print("You get back on the court - the ball is in your hands. You dribble past your defender, and you take your shot.")
        randnumber = int(input("Please type in a number 1 thru 3. If you guess the random number, then your shot goes in and your points will increase by 5."))
        if randnumber == randint(1, 3):
            print("THE CROWD GOES WILD! YOU HIT THE GAME WINNING SHOT!")
            pointsnumber += 5
        else:
            print("Tough look. you miss the shot, and you go home disappointed, having fueled your most excessive haters on the internet.")
            pointsnumber -= 5
    else:
        print("You pass it off to your teammate who misses the game winning shot. You go home wondering if you could have won the game if you decided to take the shot.")
        pointsnumber -= 2
    
    global points_p
    global assists
    global rebounds
    global steals
    global blocks

    print("SEASON OVER:")
    if records[index] > 50:
        print(f"Congratulations! The {your_team} ended up with {(records[index])} wins and {(int(82 - (records[index])))} losses!")
    elif records[index] >= 34:
        print(f"Decent job. The {your_team} ended up with {(records[index])} wins and {(int(82 - (records[index])))} losses!")
    elif records[index] < 34:
        print(f"Not great. The {your_team} ended up with {(records[index])} wins and {(int(82 - (records[index])))} losses!")
    print(f"Your stats for the 2022 NBA Season were: {(points_p)} points per game, {(assists)} assists per game, {(rebounds)} rebounds per game, {(steals)} steals per game, and {(blocks)} blocks per game.")

    print("YOU ENDED UP WITH " + str(pointsnumber) + "POINTS")
    if pointsnumber < 40 and pointsnumber > 15:
        print("From Bleacher Report: ")
        print(f"Decent first season for {player}. Where do the {your_team} go from here?")
    elif pointsnumber >= 40 and pointsnumber < 55:
        print(f"From the {your_team} Press: ")
        print(f"{player} shushes their doubters in year one for all around great {your_team} season")
    elif pointsnumber >= 55:
        print("Everyone is buzzing, with headlines like: ")
        print(f"{your_team}'s {player}: Next GOAT?")
        print(f"{player} shocks just about the entire planet with their incredible first season.")
        print(f"Witnessing greatness: {player} and the incredible NBA 2022 season")
    else:
        print("From the Washington Post: ")
        print(f"{player} and the season to forget: what went wrong with the newest {your_team} signing")

    return pointsnumber


def main() -> None:
    """Main function. Here, we have nested while loops for game loop. The function begins with greeting the player, then moves on to team and position setup and training, then moves on to season simulation, gamewinner situation, and then end of season stats, points, and headlines, and you have the ability to restart from any branch of the adventure when you finish."""
    global points
    global your_team
    global player
    i = 0
    while i >= 0:
        while i == 0:
            greet()
            i += 1
        while i == 1:
            team_setup()
            if your_team == 'done':
                return None
            print("Your job this season is to convince all of the doubters of your ability to be a great NBA player.")
            headlines = int(input("Do you want to see the headlines about your recent NBA signing? Type 0 for yes or 1 for no"))
            print('')
            if headlines == 0:
                print(f"From the {your_team} Regular: ")
                print(f"{your_team}'s recent signing of {player} disappointment to many long-time fans - How will the undrafted rookie fare in the 2022 season?")
                print("From Bleacher Report: ")
                print(f"{your_team} takes chance on rough-around-the-edges, undrafted prospect {player} to the dismay of long time fans of the franchise.")

            if headlines == 1:
                print(" ")  
            i += 1
        while i == 2:
            trainingandseasonsimulation()
            i += 1
        while i == 3:
            points = final(points)
            i += 1
        
        print(f"With a final point total of {points} points, you can choose to play again or quit the game.")
        i = int(input("If you would like to play again, type 0 to begin from the beginning, 1 to set up your team and position, 2 to simulate the season, and 3 to hit shot. If you want to end the game, enter -1. If you enter 2, then your current ratings will remain. If you want these to be reset, then go to an earlier stage."))
        
    return None


if __name__ == "__main__":
    main()