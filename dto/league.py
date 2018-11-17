class League:
	def __init__(self, _teams, _year):
		if isinstance(_teams, list) and isinstance(_year, str):
			self.teams = _teams
			self.year = year
		else:
			raise Exception("_teams must be of type list and _year must be of type string")

	def get_teams(self):
		return self.teams

	def get_year(self):
		return self.year