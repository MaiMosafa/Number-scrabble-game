array=['1','2','3','4','5','6','7','8','9']
print(array)
sumation1=0
sumation2=0
counter=0
counter2=0
while (counter!=3) :
        counter2=0
        player1= (input("player 1 : choose number from this list:"))
        for i in range (0,len(array)):
                if player1 != array[i]:
                        counter2=counter2+1
        if counter2 == len(array):
                        print("invalid, please insert a valid input")
                        counter2 = 0
        else:
                
                sumation1+=int(player1)
                if sumation1 == 15 and counter == 2:
                        print("player 1 is winner")
                        break
                else:
                        array.remove(player1)
                        print(array)
                        while (1):
                                counter2=0
                                player2=(input("player 2 : choose number from this list:"))
                                for i in range (0,len(array)):
                                        if player2 != array[i]:
                                                counter2=counter2+1
                                if counter2 == len(array):
                                        print("invalid, please insert a valid input")
                                else:
                                        sumation2+=int(player2)
                                        if sumation2 == 15 and counter == 2:
                                                print("player 2 is winner")
                                                counter=3
                                                break
                                        else:
                                                if counter==2:
                                                        print("draw")
                                                        counter=3
                                                        break
                                                else:
                                                        array.remove(player2)
                                                        print(array)
                                                        counter=counter+1
                                                        break
