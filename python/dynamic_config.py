from os import getenv

class Config(object):
    def __getattr__(self, name):
        value = getenv(name)
        if value == None:
            raise AttributeError("'Config' object has no attribute '%s'" % (name))
        return value

c = Config()

print("Name: %s" % c.Name)
# print("Name: %s" % c.Name)
print()


class Base(object):
    def __init__(self):
        if not isinstance(self.attrs, list):
            raise TypeError("'attrs' attribute incorrect type")
        if len(self.attrs) == 0:
            raise ValueError("'attrs' list is empty")

        for attr in self.attrs:
            if not isinstance(attr, dict):
                raise ValueError("'attrs' value should be dict")

            if attr.get('Name') == None:
                raise AttributeError("Dict does not have 'Name' key")

            if getenv(attr['Name']) == None and attr.get('Default') == None:
                raise AttributeError("'%s' not found in environment variables" % (attr['Name']))

    def __getattr__(self, name):
        return getenv(name)

class Config(Base):
    attrs = [
        {
            "Name": "Name" # Will throw error if env not found
        },
        {
            "Name": "NEW_Name", # Will use Default if env not found
            "Default": "A"
        },
    ]

c = Config()
print("Name: %s" % c.Name)
