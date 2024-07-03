class Television:
	def __init__(self, model, screen_size, volume, channel):
		self.model = model
		self.screen_size = screen_size
		self.__volume = volume
		self.__channel = channel
		print("A new television has been built!")
    
	@property
	def volume(self):
		return self.__volume

	@volume.setter
	def volume(self, new_volume):
		if new_volume > 80:
			print("Volume is too loud!")
		else:
			self.__volume = new_volume
			print("Volume set to:", new_volume)
    
	@property
	def channel(self):
		return self.__channel

	@channel.setter
	def channel(self, new_channel):
		if 1 <= new_channel <= 50:
			self.__channel = new_channel
			print("Channel changed to:", new_channel)
		else:
			print("Invalid channel number.")

# Create the Sony and Samsung objects
sony = Television("Bravia", 60, 30, 1)
samsung = Television("KU6020", 65, 30, 1)

# Print model and screen size to confirm creation
print("\nIt is a Sony", sony.model, "with", sony.screen_size, "inch screen.")
print("It is a Samsung", samsung.model, "with", samsung.screen_size, "inch screen.")

# Change the volume on the Sony
print("\nChanging the volume on the Sony...")
vol = int(input("Please provide a volume setting between 1 and 100: "))
sony.volume = vol

# Change the volume on the Samsung
print("\nChanging the volume on the Samsung...")
vol = int(input("Please provide a volume setting between 1 and 100: "))
samsung.volume = vol

# Change the channel on the Sony
print("\nChanging the channel on the Sony...")
chan = int(input("Please provide a channel number between 1 and 50: "))
sony.channel = chan

# Change the channel on the Samsung
print("\nChanging the channel on the Samsung...")
chan = int(input("Please provide a channel number between 1 and 50: "))
samsung.channel = chan