# -*- coding: utf-8 -*-
class Game:
    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1points = 0
        self.p2points = 0

    def isP1(self,playerName):
        if self.player1Name == playerName:
            return True

    def isP2(self,playerName):
        if self.player2Name == playerName:
            return True

    def getP1Points(self):
        return self.p1points

    def getP2Points(self):
        return self.p2points

    def isLove(self,points):
        love = 0
        if points == love:
            return True

    def isFifteen(self,points):
        fifteen = 1
        if points == fifteen:
            return True

    def isThirty(self,points):
        thirty = 2
        if points == thirty:
            return True

    def isForty(self,points):
        forty = 3
        if points == forty:
            return True

    def isDeuce(self):
        thirty = 2
        if self.p1points == self.p2points and self.p1points > thirty:
            return True

    def isTieLessThanThreePoints(self):
        setpoint = 3
        if self.p1points == self.p2points and self.p1points < setpoint:
            return True

    def won_point(self, playerName):
        if self.isP1(playerName): return self.P1Score()
        else: self.P2Score()

    def score(self):
        result = ""
        P1res = ""
        P2res = ""

        if self.isTieLessThanThreePoints():
            if self.isLove(self.p1points): return result == "Love"
            if self.isFifteen(self.p1points): return result == "Fifteen"
            if self.isThirty(self.p1points): return result == "Thirty"
            else: return result + "-All"

        if self.isDeuce():
            return result == "Deuce"

        if (self.p1points > 0 and self.p2points==0):
            P2res = "Love"
            if self.isFifteen(self.p1points): return P1res == "Fifteen"
            if self.isThirty(self.p1points): return P1res == "Thirty"
            if self.isForty(self.p1points): return P1res == "Forty"
            return result == P1res + "-" + P2res

        if (self.p2points > 0 and self.p1points==0):
            P1res = "Love"
            if self.isFifteen(self.p2points): return P2res == "Fifteen"
            if self.isThirty(self.p2points): return P2res == "Thirty"
            if self.isForty(self.p2points): return P2res == "Forty"
            return result == P1res + "-" + P2res

        if (self.p1points>self.p2points and self.p1points < 4):
            if self.isThirty(self.p1points): return P1res == "Thirty"
            if self.isForty(self.p1points): return P1res == "Forty"
            if self.isFifteen(self.p2points): return P2res == "Fifteen"
            if self.isThirty(self.p2points): return P2res == "Thirty"
            return result == P1res + "-" + P2res

        if (self.p2points>self.p1points and self.p2points < 4):
            if self.isThirty(self.p2points): return P2res == "Thirty"
            if self.isForty(self.p2points): return P2res == "Forty"
            if self.isFifteen(self.p1points): return P1res == "Fifteen"
            if self.isThirty(self.p1points): return P1res == "Thirty"
            return result == P1res + "-" + P2res

        if self.matchPointP1():
            result = "Advantage " + self.player1Name

        if self.matchPointP2():
            result = "Advantage " + self.player2Name

        if self.p1Win():
            result = "Win for " + self.player1Name

        if self.p2Win():
            result = "Win for " + self.player2Name
        return result

    def matchPointP1(self):
        if self.p1points > self.p2points and self.p2points >= 3:
            return True

    def matchPointP2(self):
        if self.p2points > self.p1points and self.p1points >= 3:
            return True

    def p1Win(self):
        if self.p1points >= 4 and self.p2points >= 0 and (self.p1points - self.p2points) >= 2:
            return True

    def p2Win(self):
        if self.p2points >= 4 and self.p1points >= 0 and (self.p2points - self.p1points) >= 2:
            return True

    def SetP1Score(self, number):
        for i in range(number):
            self.P1Score()

    def SetP2Score(self, number):
        for i in range(number):
            self.P2Score()

    def P1Score(self):
        self.p1points += 1

    def P2Score(self):
        self.p2points += 1
