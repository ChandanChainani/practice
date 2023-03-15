#! /usr/bin/env python

from sqlobject import *
from types import GeneratorType

__connection__ = "sqlite:/:memory:?debug=1&debugOutput=1"

class Person(SQLObject):
    class sqlmeta:
        table = 'city_person'
    name = StringCol()
    pets = MultipleJoin('Animal', joinColumn='owner_id')

# class Animal(SQLObject):
#     class sqlmeta:
#         table = 'city_animal'
#     name = StringCol()
#     owner = ForeignKey('Person')
#
# Person.createTable()
# Animal.createTable()
#
# person = Person(name='Test')
# cat = Animal(name='Kitty', owner=person)
#
# print(person.pets)
# print(cat.owner)

# def AND(*ops):
#     if not ops:
#         return None
#     op1 = ops[0]
#     print(op1)
#     ops = ops[1:]
#     print(ops)
#     if ops:
#         return sqlbuilder.SQLOp("AND", op1, AND(*ops))
#     else:
#         return op1
#
# print(AND(1 == 1, 2 == 3))

class Case(sqlbuilder.SQLExpression):

    class When(sqlbuilder.SQLExpression):
        def __init__(self, cond=sqlbuilder.NoDefault, val=sqlbuilder.NoDefault):
            self.cond = cond
            self.val = val

        def __sqlrepr__(self, db):
            return "WHEN %s THEN %s" % (
                converters.sqlrepr(self.cond, db),
                sqlbuilder._str_or_sqlrepr(self.val, db)
            )

    def __init__(self, cases=[(sqlbuilder.NoDefault, sqlbuilder.NoDefault)], default=sqlbuilder.NoDefault):
        self.cases = cases
        if not isinstance(self.cases, (list, tuple, GeneratorType)):
            self.cases = [self.cases]
        self.default = default

    def __sqlrepr__(self, db):
        expr = "CASE %s" % " ".join(
            [
                converters.sqlrepr(
                    self.When(case[0], case[1]), db
                )
                for case in self.cases
            ]
        )
        if not self.default is sqlbuilder.NoDefault:
            expr += " ELSE " + sqlbuilder._str_or_sqlrepr(self.default, db)
        expr += " END"
        return expr

# print(converters.sqlrepr(Case([(1, 2), (3, 4)]), db="mysql"))
for case in [
    Case(),
    Case(default=0),
    Case([(1, 2)]),
    Case([(3, 4)], default=0),
    Case([(5, 6)], default=None),
    Case([(7, 8), (9, 0)]),
    sqlbuilder.ColumnAS(Case([(0 == 0, 2)]), "mycase"),
    sqlbuilder.Select(sqlbuilder.ColumnAS(Case([(0 == 0, 3)]), "mycase"), staticTables=["TableA"]),
    sqlbuilder.Select(1, staticTables=["TableA"]).orderBy(Case([(0 == 0, 3)])),
    Person.select(1).orderBy(Case([(0 == 0, 3)])),
]:
    try:
        print(case)
    except Exception as ex:
        print(ex)



class Between(sqlbuilder.SQLExpression):
    def __init__(self, col=sqlbuilder.NoDefault, val1=sqlbuilder.NoDefault, val2=sqlbuilder.NoDefault):
        self.col = col
        self.val1 = val1
        self.val2 = val2

    def __sqlrepr__(self, db):
        return "%s Between %s AND %s" % (
            converters.sqlrepr(self.col, db),
            sqlbuilder._str_or_sqlrepr(self.val1, db),
            sqlbuilder._str_or_sqlrepr(self.val2, db)
        )
print()

for between in [
    Between(),
    Between(1),
    Between(1, 2),
    Between(3, 4, 5),
    Between("a", "b", "c"),
    Between("a", 6, "b"),
    Between(7, "b", 8),
    Between(9, 0, "c"),
    sqlbuilder.ColumnAS(Between("a", 6, 7), "mycase"),
    sqlbuilder.Select(sqlbuilder.ColumnAS(Between("c", 8, 9), "mycase"), staticTables=["TableA"]),
    sqlbuilder.Select(1, staticTables=["TableA"]).orderBy(Between("c", 1, 0)),
    Person.select(Between(Person.q.name, 1, 0)),
]:
    try:
        print(between)
    except Exception as ex:
        print(ex)


