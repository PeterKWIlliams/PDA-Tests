import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.cardGame = CardGame()
        self.card = Card("Hearts",3)
        self.card2 = Card("Diamonds",5)
        self.card3 = Card("Spades",1)
        self.cards =[self.card,self.card2,self.card3]


    def test_check_for_ace_False(self):
        
        
        self.assertEqual(False,self.cardGame.check_for_ace(self.card))

    
    def test_check_for_ace_True(self):
        
        
        self.assertEqual(True,self.cardGame.check_for_ace(self.card3))


    def test_highest_card(self):
        self.assertEqual(self.card2,self.cardGame.highest_card(self.card,self.card2))

    def test_cards_total(self):
        
        self.assertEqual("You have a total of 9",self.cardGame.cards_total(self.cards))
    