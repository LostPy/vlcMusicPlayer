"""A music modele object."""

import os
import vlc

vlc_music = vlc.Instance()


class Music:
	"""Class to reprensent a music."""

	def __init__(self, music_path: str, title: str = "Unknow", artist: str = "Unknow"):
		if os.path.exists(music_path):
			self.path = music_path
		else:
			raise FileNotFoundError(f"File {music_path} was not found.")
		self.title = title
		self.artist = artist
		self.player = None

	def __repr__(self):
		return f"<Title: {self.title}, Artist: {self.artist}, Path: {self.path}>"

	def __str__(self):
		return self.__repr__()

	def play(self):
		self.player = vlc_music.media_player_new()
		media = vlc_music.media_new(self.path)
		self.player.set_media(media)
		self.player.play()

	def pause(self):
		if self.player is not None:
			self.player.pause()

	def stop(self):
		if self.player is not None:
			self.player.stop()
			self.player = None

	def resume(self):
		if self.player is not None and not self.is_playing:
			self.player.play()

	@property
	def is_playing(self):
		return self.player is not None and self.player.is_playing() == 1
