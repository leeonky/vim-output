class OutputForm(object):
	def __init__(self, ouputer, row_provider):
		self.ouputer = ouputer
		self.row_provider = row_provider

	def synchronize(self):
		self.ouputer.append(self.row_provider.pop_rows())
