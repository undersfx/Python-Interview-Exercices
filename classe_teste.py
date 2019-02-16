class Circle:
	_pi = 3.14 # Variavel reservada da classe

	def __init__(self, radius=5):
		self.r = radius

	def get_perimter(self):
		# return 2 * math.pi * self.r
		return 2 * self._pi * self.r
