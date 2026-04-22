a = {"key": "value",
    "harry":"code",
    "marks":"100",
    "list":[1,2,9]
}

print(a.items())

print(a.keys())

print(a.update({"friend":"Sona"}))
print(a.items())

print(a.get("marks"))

a.pop("marks")
print(a)

a.popitem();
print(a)