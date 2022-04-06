# -*- coding: utf-8 -*-
class Game:
    
    minPoints= 0  
    
    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1points = 0
        self.p2points = 0
    
    def isP1(self,playerName):
        if self.playerName = player1Name:
            return true

    def isP2(self,playerName):
        if self.playerName = player2Name:
            return true

    def getP1Points(self):
        return self.p1points

    def getP2Points(self):
        return self.p2points
        
    def isLove(points):
        love = 0
        if points == love:
            return true

    def isFifteen(points):
        fifteen = 1
        if points == fifteen:
            return true

    def isThirty(points):
        thirty = 2
        if points == thirty:
            return true

    def isForty(points):
        forty = 3
        if points == forty:
            return true
        
    def isDeuce(self):
        thirty = 2
        if self.p1points == self.p2points and self.p1points > thirty:
            return true

    def isScore(self):
        setpoint = 3
        if self.p1points == self.p2points and self.p1points < setpoint:
            return true
        
    def won_point(self, playerName):
        if isP1(playerName) return P1Score()
        if isP2(playerName) return P2Score()
    
    def score(self):
        result = ""
        P1res = ""
        P2res = ""
        
        if isScore():
            if isLove(p1points) return result = "Love"
            if isFifteen(p1points) return result = "Fifteen"
            if isThirty(p1points) return result = "Thirty"
            return result += "-All"
        else isDeuce() return result = "Deuce"
        
        if (self.p1points > 0 and self.p2points==0):
            P2res = "Love"
            if isFifteen(p1points) return P1res = "Fifteen"
            if isThirty(p1points) return P1res = "Thirty"
            if isForty(p1points) return P1res = "Forty"
            return result = P1res + "-" + P2res
            
        if (self.p2points > 0 and self.p1points==0):
            P1res = "Love"
            if isFifteen(p2points) return P2res = "Fifteen"
            if isThirty(p2points) return P2res = "Thirty"
            if isForty(p2points) return P2res = "Forty"
            return result = P1res + "-" + P2res
        
        if (self.p1points>self.p2points and self.p1points < 4):
            if isThirty(p1points) return P1res = "Thirty"
            if isForty(p1points) return P1res = "Forty"
            if isFifteen(p2points) return P2res = "Fifteen"
            if isThirty(p2points) return P2res = "Thirty"
            return result = P1res + "-" + P2res
        
        if (self.p2points>self.p1points and self.p2points < 4):
            if isThirty(p2points) return P2res = "Thirty"
            if isForty(p2points) return P2res = "Forty"
            if isFifteen(p1points) return P1res = "Fifteen"
            if isThirty(p1points) return P1res = "Thirty"
            return result = P1res + "-" + P2res
        
        if (self.p1points > self.p2points and self.p2points >= 3) return result = "Advantage " + self.player1Name
        if (self.p2points > self.p1points and self.p1points >= 3) return result = "Advantage " + self.player2Name
        
        if (self.p1points>=4 and self.p2points>=0 and (self.p1points-self.p2points)>=2) return result = "Win for " + self.player1Name
        if (self.p2points>=4 and self.p1points>=0 and (self.p2points-self.p1points)>=2) return result = "Win for " + self.player2Name
        return result
    
    def SetP1Score(self, number):
        for i in range(number):
            self.P1Score()
    
    def SetP2Score(self, number):
        for i in range(number):
            self.P2Score()
    
    def P1Score(self):
        self.p1points +=1
    
    def P2Score(self):
        self.p2points +=1
