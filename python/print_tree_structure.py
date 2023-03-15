employees = [
  {
    "ID": 1,
    "Name": "M1",
    "ManagerID": None
  },
  {
    "ID": 2,
    "Name": "E1",
    "ManagerID": 1,
  },
  {
    "ID": 3,
    "Name": "E2",
    "ManagerID": 2,
  },
  {
    "ID": 4,
    "Name": "E3",
    "ManagerID": 2,
  },
  {
    "ID": 5,
    "Name": "E4",
    "ManagerID": 3,
  },
  {
    "ID": 6,
    "Name": "E5",
    "ManagerID": 1,
  },
  {
    "ID": 7,
    "Name": "E6",
    "ManagerID": 2,
  },
  {
    "ID": 8,
    "Name": "E7",
    "ManagerID": 1,
  },
  {
    "ID": 9,
    "Name": "E8",
    "ManagerID": 2,
  },
  {
    "ID": 10,
    "Name": "E9",
    "ManagerID": 3,
  },
]

tree = {}
info = {}

for emp in employees:
    info[emp["ID"]] = emp["Name"]

    if emp["ManagerID"]:
        if tree.get(emp["ManagerID"]) == None:
            tree[emp["ManagerID"]] = []
        tree[emp["ManagerID"]].append(emp["ID"])

# print(info)
# print(tree)

def recursive(idx, elems, m, n, d):
    if isinstance(elems, dict):
        for k, v in elems.items():
            if not d.get(k):
                print(n[k])
                if len(v) > 0:
                    recursive(idx + 1, v, m, n, d)

    if isinstance(elems, list):
        for el in elems:
            print("{}{}".format("".ljust((4 * idx) - 4) + "|___", n[el]))
            if m.get(el, None) != None:
                d[el] = 1
                recursive(idx + 1, m.get(el), m, n, d)

recursive(0, tree, tree, info, {})
