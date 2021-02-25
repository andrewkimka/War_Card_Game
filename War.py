import random

class Card:
    rank_names=[None,"Ace","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King"]
    suit_names=["Clubs","Diamonds","Hearts","Spades"]
    
    def __init__(self,rank=2,suit=0):
        self.rank=rank
        self.suit=suit
    
    def __str__(self):
        return Card.rank_names[self.rank]+" of "+Card.suit_names[self.suit]
    
    def __lt__(self,other):
        if self.rank != other.rank:
            return self.rank < other.rank
        return self.suit < other.suit
    
    def __eq__(self,other):
        return self.rank == other.rank and self.suit == other.suit
    
    def __le__(self,other):
        return self==other or self<other
    
class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                card = Card(rank,suit)
                self.cards.append(card)
    
    def __str__(self):
        answer = ""
        for card in self.cards:
            answer = answer + str(card) + "\n"
        return answer
    
    def pop_card(self):
        return self.cards.pop()
    
    def add_card(self,card):
        return self.cards.append(card)
    
    def shuffle(self):
        random.shuffle(self.cards)
        
    def moveCard(self,player,number):
        for i in range(number):
            player.add_card(self.pop_card())
    
    def deal_hand(self,player1,player2,Ncards):
        for i in range(1):
            self.moveCard(player1,Ncards)
            self.moveCard(player2,Ncards)
        
class Hand:
    def __init__(self,name="player"):
        self.cards=[]
        self.name=name
    
    def pop_card(self):
        return self.cards.pop()
        
    def add_card(self,card):
        return self.cards.append(card)
        
    def moveCard(self,player,number):
        for i in range(number):
            player.add_card(self.pop_card())
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def __str__(self):
        answer = self.name + " is holding\n"
        for card in self.cards:
            answer = answer + str(card) + "\n"
        return answer

class WarHand(Hand):
    def __init__(self,name="player",wins=0,losses=0):
        super().__init__(name)
        self.w=wins
        self.l=losses
    
    def hasCard(self):
        if cards>0:
            return True
        return False

    def stats(self):
        print(self.name+" has lost "+str(self.w)+" times and lost "+str(self.l)+" times. ")
    
    def win(self):
        self.w=self.w+1
    
    def win(self):
        self.w=self.w+1
    
    def loss(self):
        self.l=self.l+1

class WarDeck(Deck):
    def __init__(self,name="dealer"):
        super().__init__()
        
    def collectCards(self,player):
        for i in range(len(player.cards)):
            self.cards.add_card(player.pop_card())
        self.cards.shuffle()
        
    def War(self,player1,player2):
        self.shuffle()
        self.deal_hand(player1,player2,26)
        for i in range(26):
            player1.shuffle()
            player2.shuffle()
            card1=player1.pop_card()
            card2=player2.pop_card()
            if card1<card2:
                player2.win()
                player1.loss()
            else:
                player1.win()
                player2.loss()
        
        player1.stats()
        player2.stats()
        print()
        
Deck=WarDeck()
Bob=WarHand('Bob')
Alice=WarHand('Alice')
Deck.War(Bob,Alice)
