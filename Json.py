import json
with open('data.json') as json_file:
	data = json.load(json_file)

	
	print("Type:", type(data))

	print("\nPeople1:", data['People1'])
