import random
class Lottery:
    def createFile(randNumbers):
        f = open('LotteryNumbers.txt','w')
        for list in randNumbers:
            f.write(str(list)+ "\n")
        print("Finished Writing Numbers")
        f.close
    def createNumbers():
        randNumbers = []
        for x in range(0,300000):
            randNumbers.append([])
            if x == 100000:
                print("33% Done")
            if x == 200000:
                print("66% Done")
            for i in range(3):
                randNumbers[x].append(random.randint(1,40))
        print("Finished Creating Numbers")
        return randNumbers
    def pickWinningNumbers():
        winningNumbers = []
        for x in range(3):
            winningNumbers.append(random.randint(1,40))
        print('The winning number that was randomly selected is ' + str(winningNumbers))
        return winningNumbers
    def checkTickets(winningNumbers):
        lines = (line.rstrip('\n') for line in open('LotteryNumbers.txt', 'r'))
        count = 0
        flag = False
        for line in lines:
            if str(winningNumbers) == str(line):
                print('Theres a winner! Found on line ' + str(count))
                flag = True
            count = count + 1
        if flag == False:
            print('No winning tickets were found.' + str(winningNumbers))
