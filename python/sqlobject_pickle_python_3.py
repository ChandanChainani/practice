import pickle

data = { "a": 1, "b": 2, "c": 3 }

pickled_data = pickle.dumps(data)
print(pickled_data)

hexed_data = pickled_data.hex()
print(hexed_data)

print(pickle.loads(bytes.fromhex(hexed_data)))
