def total_score(number_list):  # The purpose of this function is to add up the total scores of the cards in hand
    add_up = 0  # used for adding other numbers to
    for i in number_list:  # goes through each item in the list
        add_up = add_up + i
        if add_up >= 10:  # checks if above ten, this is Saum Pi after all
            add_up = add_up - 10
    return_number = add_up
    return return_number  # Going to get remainder for ten division

# will compare the total score of each player against each other
def compare_score(playerListNumbers):
    counter = -1  # starts at negative one because when going through the loop it will automatically add the first one
    #first = playerListNumbers[0]  # was thinking of testing whom won with code another way
    highest = 0  # used to keep track what the highest score is
    player_whom_won = 0  # this number is for telling whom in the list has the highest code
    for i in playerListNumbers:  # going through each number in the list
        counter = counter + 1  # keeping track of which player we are comparing
        if highest < i:  # comparing the two players numbers
            highest = i  # making new highest if larger
            player_whom_won = counter  # will let us know whom won

    if player_whom_won == 0:  # That's You!
        print("You Won!")
    elif player_whom_won == 1:
        print("Second Player Won!")
    elif player_whom_won == 2:
        print("Third Player Won!")
    elif player_whom_won == 3:
        print("Forth Player Won!")
    else:
        pass