#Sort a list of dictionaries based on the "year" value of the dictionaries:
cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]

cars.sort(reverse= True, key= lambda e : e['year'])
print(cars)
