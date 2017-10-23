class Smashing_Pumpkins(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics

	def play_a_song(self):
		for statement in self.lyrics:
			print(statement)

today = Smashing_Pumpkins(["Today is the greatest",
		   				   "day I've ever known",
				   		   "Can't live for tomorrow",
				   		   "Tomorrow's much too long"])

bullet_with_butterfly_wings = Smashing_Pumpkins(["Despite all my rage",
							 					 "I am still just a rat",
							 					 "in a cage!"])

today.play_a_song()

bullet_with_butterfly_wings.play_a_song()