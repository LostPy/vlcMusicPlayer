"""A music player model object."""

import vlc
from .queue import Queue
from .music import Music

vlc_player = vlc.Instance()


class MusicPlayer:
	"""A object to reprensent a music player."""

	def __init__(self, queue=[]):
		if isinstance(queue, Queue):
			self.queue = queue
		elif isinstance(queue, list) or isinstance(queue, tuple):
			self.queue = Queue(queue)
		else:
			raise ValueError(f"'queue' must be a instance of list, tuple or Queue, not a instance of {type(queue)}")
		self.player = vlc_player.media_player_new()
		if self.is_empty:
			self.current_media = None
			self.current_music = None
		else:
			try:
				self._set_new_media_to_player(self.queue.pop())
			except ValueError as e:
				raise ValueError("Items of queue" + str(e)[str(e).find(" "):])
		self.current_volume = 100
	
	def __len__(self):
		return len(self.queue)

	@property
	def is_empty(self):
		return self.queue.is_empty
	
	@property
	def is_playing(self):
		return self.player.is_playing() == 1

	def _set_current_media(self, music):
		if isinstance(music, Music):
			self.current_media = vlc_player.media_new(music.path)
			self.current_music = music
		elif isinstance(music, str):
			self.current_music = Music(music)
			self.current_media = vlc_player.media_new(self.current_music.path)
		else:
			raise ValueError(f"'music' must be a instance of Music or str, not {type(music)}.")
	
	def _set_new_media_to_player(self, music):
		self._set_current_media(music)
		self.player.set_media(self.current_media)
	
	def play(self):
		self.player.audio_set_volume(self.current_volume)
		self.player.play()
	
	def pause(self):
		self.player.pause()
	
	def play_pause(self):
		if self.is_playing:
			self.pause()
		else:
			self.play()
	
	def set_volume(self, volume: int):
		self.current_volume = volume
		self.player.audio_set_volume(self.current_volume)

	def skip(self):
		if len(self) == 0:
			self.stop()
		else:
			self.player.stop()
			self._set_new_media_to_player(self.queue.pop())
			self.play()
		
	def stop(self):
		self.player.stop()
		old_volume = self.current_volume
		self.__init__()
		self.set_volume(old_volume)

	def get_position(self):
		return self.player.get_position()

	def set_position(self, postion: float):
		self.player.set_position(postion)
	
	def add_music(self, music_path: str):
		self.queue.add_item(music_path)
	
	def set_playlist(self, queue):
		self.player.stop()
		old_volume = self.current_volume
		self.__init__(queue)
		self.set_volume(old_volume)
