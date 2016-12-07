from LotteryClass import Lottery as L
def main():
    randNumbers = []
    randNumbers = L.createNumbers()
    L.createFile(randNumbers)
    winningNumbers = L.pickWinningNumbers()
    L.checkTickets(winningNumbers)
main()
