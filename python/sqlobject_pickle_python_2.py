from __future__ import print_function
import zlib, pickle, json

data = { "a": 1, "b": 2, "c": 3 }

json_data = json.dumps(data)
compressed_data = zlib.compress(json_data)
pickled_data = pickle.dumps(compressed_data)
hexed_data = pickled_data.encode('hex')
print(hexed_data)
print(zlib.decompress(pickle.loads(hexed_data.decode('hex'))))

