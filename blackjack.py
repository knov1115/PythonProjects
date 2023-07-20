import os
import random


class Game:
	def __init__(self):
		self.player_cards = []
		self.computer_cards = []


	def idle_screen(self):
		self.clear_console()
		game_text = """
		 ____  _            _         _            _    
 		|  _ \| |          | |       | |          | |   
 		| |_) | | __ _  ___| | __    | | __ _  ___| | __
 		|  _ <| |/ _` |/ __| |/ /    | |/ _` |/ __| |/ /
 		| |_) | | (_| | (__|   <   __| | (_| | (__|   < 
 		|____/|_|__,_ |___|_|____| |___,_|___ |_|__|___\
                                                
 						made by: knov
		"""
		print(game_text)
		print("Welcome to BlackJack!")
		game_init = input("Would you like to play a game of Blackjack? (y/n): ")

		if game_init == "y":
			print("Great! Dealer is throwing out the cards...")
			return self.game_start()
		elif game_init == "n":
			return "See you later!"
		else:
			return "Uh-oh! Incorrect input...Try(y/n)"





	def game_start(self):
		self.player_cards.clear()
		self.computer_cards.clear()

		for i in range(0, 2):
			p = random.randint(2, 10)
			self.player_cards.append(p)
		for j in range(0, 2):
			c = random.randint(2, 10)
			self.computer_cards.append(c)
		print("--------------")
		print(f"The computer card's: {self.computer_cards} Total: {self.sum_of_list(self.computer_cards)} \nThe player's card's: {self.player_cards} Total: {self.sum_of_list(self.player_cards)}")
		print("--------------")
		player_choice_draw = input("Hit or Stay?: ")

		if player_choice_draw == "Hit":
			print("Giving you a new card...")
			return self.new_card()
		elif player_choice_draw == "Stay":
			new_card_computer = random.randint(2, 10)
			self.computer_cards.append(new_card_computer)
			print("--------------")
			print(f"The computer card's: {self.computer_cards} Total: {self.sum_of_list(self.computer_cards)} \nThe player's card's: {self.player_cards} Total: {self.sum_of_list(self.player_cards)}")
			print("--------------")

			if self.sum_of_list(self.player_cards) > self.sum_of_list(self.computer_cards):
				print("Congrats! You've Won!")
			elif self.sum_of_list(self.player_cards) < self.sum_of_list(self.computer_cards):
				print("Computer Has Won! Better luck next time :)")
			else:
				print("It's a Draw!")
			return self.stop()
		

		
		

	def ask_for_new_card(self):
		player_choice_draw = input("Hit or Stay?: ")

		if player_choice_draw == "Hit":
			print("Giving you a new card...")
			return self.new_card()
		elif player_choice_draw == "Stay":
			new_card_computer = random.randint(2, 10)
			self.computer_cards.append(new_card_computer)
			print("--------------")
			print(f"The computer card's: {self.computer_cards} Total: {self.sum_of_list(self.computer_cards)} \nThe player's card's: {self.player_cards} Total: {self.sum_of_list(self.player_cards)}")
			print("--------------")
			
			if self.sum_of_list(self.player_cards) > self.sum_of_list(self.computer_cards):
				print("Congrats! You've Won!")
			elif self.sum_of_list(self.player_cards) < self.sum_of_list(self.computer_cards):
				print("Computer Has Won! Better luck next time :)")
			else:
				print("It's a Draw!")
			return self.stop()
		




	def sum_of_list(self, card_list):
		total = 0
		for num in card_list:
			total += num
		return total


	def new_card(self):
		new_card_player = random.randint(2, 10)
		self.player_cards.append(new_card_player)
		new_card_computer = random.randint(2, 10)
		self.computer_cards.append(new_card_computer)
		print("--------------")
		print(f"The computer card's: {self.computer_cards} Total: {self.sum_of_list(self.computer_cards)} \nThe player's card's: {self.player_cards} Total: {self.sum_of_list(self.player_cards)}")
		print("--------------")

		return self.decide_winner()

	def decide_winner(self):
		player_total = self.sum_of_list(self.player_cards)
		computer_total = self.sum_of_list(self.computer_cards)

		if player_total == 21 and computer_total == 21:
			print("It's a draw!")
		elif player_total > 21 and computer_total > 21:
			print("Both players are over 21. It's a draw!")
		elif player_total > 21:
			print("You're busted! Computer has won!")
		elif computer_total > 21:
			print("Computer is busted! You've won!")
		else:
			return self.ask_for_new_card()

		return self.stop()


	def stop(self):
		game_reset = input("Thanks for playing! Would you like another round of BlackJack? (y/n)")

		if game_reset == "y":
			print("-----------------------------------------")
			self.idle_screen()
		else:
			pass


	def __repr__(self):
		pass

	def clear_console(self):
		
		os.system('clear')


#INSTANTIATE
blackjack = Game()
Game.idle_screen(blackjack)
