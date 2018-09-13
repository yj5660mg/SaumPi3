class Player:
    def __init__(self, input_name):
        self.name = input_name

    def name(self):
        # print(self.name + " is playing.")
        return self.name

    def name(self, input_name):
        print(self.name + "The Player is winning")
        self.name = input_name

# def main():
#    bob = Player()
#    bob.play()
#    bob.player_is_winning()

# if_name__== "_main_";
#    main()