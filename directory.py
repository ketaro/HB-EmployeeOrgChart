#!/usr/bin/python
from people import Employee, Manager

# Sample Data
data = [
	{ 'id': 1,  'type': 'M', 'gn': 'Steve',		'sn': 'Jobs',			't': 'CEO' },
	{ 'id': 2,  'type': 'M', 'gn': 'Peter',		'sn': 'Oppenheimer',	't': 'CFO',						'm': 1 },
	{ 'id': 3,  'type': 'E', 'gn': 'Betsy',		'sn': 'Rafael',			't': 'Control',					'm': 2 },
	{ 'id': 4,  'type': 'M', 'gn': 'Timothy',	'sn': 'Cook',			't': 'COO',						'm': 1 },
	{ 'id': 5,  'type': 'E', 'gn': 'Michelle',	'sn': 'Brown',			't': 'Global Outsourcing', 		'm': 4 },
	{ 'id': 6,  'type': 'E', 'gn': 'Susan', 	'sn': 'Gallagaher',		't': 'AppleCare',				'm': 4 },
	{ 'id': 7,  'type': 'E', 'gn': 'John', 		'sn': 'Couch',			't': 'Education',				'm': 4 },
	{ 'id': 8,  'type': 'E', 'gn': 'Jonathan',	'sn': 'Ive',			't': 'Design',					'm': 1 },
	{ 'id': 9,  'type': 'M', 'gn': 'Philip', 	'sn': 'Schiller',		't': 'Product Marketing',		'm': 1 },
	{ 'id': 10, 'type': 'E', 'gn': 'Eddy',		'sn': 'Cue',			't': 'Internet Services',		'm': 9 },
	{ 'id': 11, 'type': 'E', 'gn': 'Greg',		'sn': 'Joswiak',		't': 'iPhone & iPod Marketing',	'm': 9 },
]

# Employee Dictionary
employees = {}

# Load Sample Data into Classes and store in our "employees" Dictionary
for p in data:
	# Pick which class we're using
	if p['type'] == 'M':
		e = Manager()
	else:
		e = Employee()

	# Basic Data
	e.id		= p['id']
	e.givenname = p['gn']
	e.surname	= p['sn']
	e.title		= p['t']

	# If the person has a manager, record it
	if 'm' in p:
		e.manager = employees[p['m']]
		employees[p['m']].reports.append(e)

	# Add to Employee Directory
	employees[e.id] = e


# Recursive Function to Print the Org Chart (tree)
#   person - Starting Person, required
#   limit  - How many levels deep to display, default is unlimited
#   level  - What level we're currently displaying (for formatting purposes), default is 0
def printOrgChart(person, limit=-1, level=0):
	print ("\t" * level) + person.lastfirst()

	if type(person) == Manager and (limit < 0 or limit > level):
		for report in person.reports:
			printOrgChart(report, limit, level + 1)


# Print the Org Chart
printOrgChart(employees[1])
