import json
import yaml

with open("1.json", "r") as js:
    js_dict = json.load(js)

with open("1.json", 'w') as js:
    js.write(json.dumps(js_dict, indent=2))

with open("2.yaml", 'w') as yml:
    yml.write(yaml.dump(js_dict, explicit_start=True, indent=2))

with open("2.yaml", 'r') as yml:
    yml_dict = yaml.safe_load(yml)

with open("2.json", 'w') as js:
    js.write(json.dumps(yml_dict))