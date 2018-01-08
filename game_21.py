import random as rnd

class Master:
    sumPlayer = 0
    sumEnemy = 0
    enemyThreshold=17
    while sumEnemy < enemyThreshold:
        sumEnemy = sumEnemy + rnd.randint(0,10)

    def ini(self):
        Master.sumPlayer = 0
        Master.sumEnemy=0
        Master.enemyThreshold=17
        while Master.sumEnemy < Master.enemyThreshold:
            Master.sumEnemy = Master.sumEnemy + rnd.randint(0,10)

    def draw(self):
        Master.sumPlayer = Master.sumPlayer + rnd.randint(0,10)
        print "Your total score is",Master.sumPlayer

    def finish(self):
        pBurst = Master.sumPlayer>21
        eBurst = Master.sumEnemy>21

        print "***finish***"
        print "Your total score is",Master.sumPlayer
        print "Enemy's total score is",Master.sumEnemy

        if pBurst:
            if eBurst:
                print "Draw Game"
            else:
                print "Enemy wins"
        else:
            if eBurst:
                print "You win"
            else:
                if Master.sumPlayer>Master.sumEnemy:
                    print "You win"
                elif Master.sumPlayer==Master.sumEnemy:
                    print "Draw Game"
                else:
                    print "Enemy wins"

    def debagSetPScore(self,s):
        Master.sumPlayer=s

    def debagSetEScore(self,s):
        Master.sumEnemy=s

    def debagSetThreshold(self,t):
        Master.enemyThreshold = t
        Master.sumEnemy = 0
        while Master.sumEnemy < Master.enemyThreshold:
            Master.sumEnemy = Master.sumEnemy + rnd.randint(0,10)

