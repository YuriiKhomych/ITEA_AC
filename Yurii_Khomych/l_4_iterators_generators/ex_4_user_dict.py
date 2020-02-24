from collections import UserDict


class TwoWayDict(UserDict):
    def __delitem__(self, key):
        value = self[key]
        super().__delitem__(key)
        self.pop(value, None)


d = TwoWayDict()
d[3] = 7
del d[3]
print(d)
