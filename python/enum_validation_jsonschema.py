# https://json-schema.org/understanding-json-schema/reference/generic.html#enumerated-values
from pprint import pprint as pp

from jsonschema import Draft4Validator, validate

LETTERS = ["A", "B", "C", "D", "E"]

# import jsonschema

# print(dir(jsonschema))
# print(dir(jsonschema.Draft4Validator), type(jsonschema.Draft4Validator))

# from jsonschema.Draft4Validator import validate

# validate = Draft4Validator()

# schema = {
#     "type" : "object",
#     "properties" : {
#         "price" : {"type" : "number"},
#         "name" : {"type" : "string"},
#     },
# }

schema = {
  "type": "array",
  "items": [
    { "type": "number" },
    { "type": "string" },
    { "enum": ["Street", "Avenue", "Boulevard"] },
    { "enum": ["NW", "NE", "SW", "SE"] }
  ]
}

schema = {
  "type": "array",
  "items": [
    { "enum": LETTERS },
  ],
  "uniqueItems": True,
  # "additionalItems": {
  #     "type": "string"
  # }
}

# schema = {
#   "type": "array",
#   "contains": {
#     "type": "string",
#     "enum": LETTERS,
#   },
#   "uniqueItems": True,
#   # "additionalItems": {
#   #     "type": "string"
#   # }
# }

# schema = {
#   "type": "array",
#   "contains": {
#     "type": "string",
#     "enum": LETTERS,
#   }
# }

schema = {
    "type": "array",
    "items": {
        "type": "string",
        "enum": LETTERS
    }
}

# data = {"name" : "Eggs", "price" : ""}
# data = [1600, "Pennsylvania", "Avenue", ""]
# data = [24, "Sussex", "Drive"]

test_data = [
  ["A"],
  ["A", "C"],
  ["A", "B", "F"],
  ["A", "C", ""],
  ["NA"],
  [""],
]
print("Schema:")
pp(schema)

# print("FIRST")
for d in test_data:
    try:
        validate(instance=d, schema=schema)
        print("Success: ", d)
    except:
        print("Error: ", d)
# print(validate(instance=data, schema=schema, format_checker=Draft4Validator.FORMAT_CHECKER))
# print("SECOND")
# Draft4Validator(schema).validate(data)
