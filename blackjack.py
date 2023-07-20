import random
#testing
class Game:
	def __init__(self):
		self.player_cards = []
		self.computer_cards = []


	def idle_screen(self):
		print("Welcome to BlackJack -- Made By knov.")
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

		print(f"The computer card's: {self.computer_cards} Total: {self.sum_of_list(self.computer_cards)} \nThe player's card's: {self.player_cards} Total: {self.sum_of_list(self.player_cards)}")
		print("--------------")
		player_choice_draw = input("Hit or Stay?: ")

		if player_choice_draw == "Hit":
			print("Giving you a new card...")
			return self.new_card()
		elif player_choice_draw == "Stay":
			pass
			#We need to decide wether the player has more points than the computer and decide the winner and loser!

		
		

	def ask_for_new_card(self):
		player_choice_draw = input("Hit or Stay?: ")

		if player_choice_draw == "Hit":
			print("Giving you a new card...")
			return self.new_card()
		elif player_choice_draw == "Stay":
			pass
			#We need to decide wether the player has more points than the computer and decide the winner and loser!
		




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
		print(f"The computer card's: {self.computer_cards} Total: {self.sum_of_list(self.computer_cards)} \nThe player's card's: {self.player_cards} Total: {self.sum_of_list(self.player_cards)}")

		if self.sum_of_list(self.computer_cards) > 21:
			print("Computer is busted!\nYou've Won!")
			return self.stop()
		else:
			return self.ask_for_new_card()
		if self.sum_of_list(self.player_cards) > 21:
			print("You're busted!\nComputer has Won!")
			return self.stop()
		else:
			return self.ask_for_new_card()





	def stop(self):
		game_reset = input("Thanks for playing! Would you like another round of BlackJack? (y/n)")

		if game_reset == "y":
			print("-----------------------------------------")
			self.idle_screen()
		else:
			pass


	def __repr__(self):
		pass


#INSTANTIATE
blackjack = Game()
Game.idle_screen(blackjack)
