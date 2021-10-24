import json
import copy

def file_formation(file_1, file_2):
    with open(file_1) as json_file:
        a_dict = json.load(json_file)

    with open(file_2) as json_file:
        b_dict = json.load(json_file)

    data_dict = copy.deepcopy(a_dict)


def set_value(d):
    if not isinstance(d, dict):
        return d
    if d.get("value"):
        return d
    r = [x.get("value") for x in b_dict["values"] if x.get("id") == d.get("id")]
    if r and r[0]:
        d["value"] = r[0]
    return d

def apply_recursive(func, obj):
    if isinstance(obj, list):
        return [apply_recursive(func, elem) for elem in obj]
    elif isinstance(obj, dict):
        return {k: apply_recursive(func, func(v)) for k, v in obj.items()}
    else:
        return func(obj)


apply_recursive(set_value, data_dict["tests"])


with open('report.json', 'w') as file:
    json.dump(data_dict, file, indent = 3)

file_formation(input(), input())