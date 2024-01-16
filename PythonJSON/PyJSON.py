#JSON is a syntax for storing and exchanging data.

#JSON is text, written with JavaScript object notation.
#Python has a built-in package called json, which can be used to work with JSON data.

import json # this is for import json

# parse JSON for converting from json to python
# use json.loads()


#already import json  so,

x='{"name":"john","age":30}'

#parse x;
y=json.loads(x)
print(y["age"])


#Python has a built-in package called json, which can be used to work with JSON data.
import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)




