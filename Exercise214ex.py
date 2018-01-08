import random as rnd

cardList = []
for i in range(0,10+1):
    cardList.append(i)

deck = []
for i in range(0,10+1):
    randomIndex = rnd.randrange(0,len(cardList))
    currentCard = cardList.pop(randomIndex)
    deck.append(currentCard)









