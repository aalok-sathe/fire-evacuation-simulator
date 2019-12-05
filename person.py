class Person: 
	def __intit__(self, r, p, i, j):
		self.rate = r
		self.loc =(i,j)
		self.life = 1
		self.p_closest = p
		self.safe = 0
		self.exit_time = float("inf")

	def move(self,graph):
		pass
