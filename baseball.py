class Player:

    def __init__(self, name):
      self.name = name
      self.inning = [None]*9
    
    def bat(self, i):
        strikes = 0
        balls = 0
        run = None
        c = 1
        while strikes < 3 and balls < 4 and run is None:
            play = input("Name: " + self.name + "\n Pitch " + str(c) + ": ")
            if play == 'x':
                strikes += 1
            elif play == 'b':
                balls += 1
            elif play == 'h':
                run = input("What base did they get to? ")
            else:
                print("Invalid input")
            c += 1

        self.inning[i] = (strikes, balls, run)
        #print ("Inning " + str(i + 1) + ": " + str(Player.inning[i]))
        print(self.inning)

    def compare(self, i):
        inn1 = self.inning[i]
        inn2 = self.inning[i-1]
        if inn1[0] < inn2[0]:
            print("Yay " + self.name + " got less strikes than last inning!")
        if inn2[2] is None:
            if inn1[2] is not (None or 0):
                print("Yay " + self.name + " got on base this inning!")
        elif inn1[2] is not None and (inn1[2] > inn2[2]):
            print("Yay " + self.name + " got further on the bases than last inning!")


def main():
    Joe = Player("Joe")
    Bob = Player("Bob")
    print("Inning 1")
    Joe.bat(0)
    Bob.bat(0)
    print("Inning 2")
    Joe.bat(1)
    Joe.compare(1)
    Bob.bat(1)
    Bob.compare(1)
    


main()

