class Smashing_Pumpkins(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics

	def play_a_song(self):
		for statement in self.lyrics:
			print(statement)


today_lyrics = ["Today is the greatest",
		   	    "day I've ever known",
				"Can't live for tomorrow",
				"Tomorrow's much too long"]

bullet_with_butterfly_wings_lyrics = ["Despite all my rage",
							 	      "I am still just a rat",
							 		  "in a cage!"]

today = Smashing_Pumpkins(today_lyrics)

bullet_with_butterfly_wings = Smashing_Pumpkins(bullet_with_butterfly_wings_lyrics)


today.play_a_song()

bullet_with_butterfly_wings.play_a_song()