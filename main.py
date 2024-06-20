from concurrent.futures import ThreadPoolExecutor
from deep_translator import GoogleTranslator
import json

def get_verbs():
	to_ret = ""
	with open("./verbs.json", "r") as f:
		to_ret = f.read()
	return json.loads(to_ret)["verbs"]

i = 0

def translate_verbs(_w):
	global i
	print(i)
	to_ret = GoogleTranslator(source='french', target='english').translate(_w)
	i += 1
	return {"e" : to_ret, "f" : _w}

verbs = get_verbs()

with ThreadPoolExecutor(max_workers=12) as executor:
	results = list(executor.map(translate_verbs, verbs["first_group"]))

with open("./group_a.json", "w") as f:
	f.write(json.dumps({"verbs": results}))
