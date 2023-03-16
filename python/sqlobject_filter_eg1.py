from sqlobject import *

__connection__ = "sqlite:/:memory:?debug=1&logger=TEST&loglevel=debug"


class Blog(SQLObject):
    name = StringCol(default="")


q = sqlbuilder.Select(Blog.q.name)
print(q)
# print(dir(q))

# Below lines throws error
# conn = sqlhub.getConnection()

q = q.newClause(Blog.q.name == "1")

# Below lines throws error
# q = q.filter(Blog.q.name == "1")
# print(q)
# print(Blog._connection.sqlrepr(q))
# print(q.__repr__())
# print(q.__sqlrepr__())

print(Blog._connection.sqlrepr(q))
# print(q)
