#9. Can you change the values inside a list which is contained in set S? 


s = {8, 7, 12, "Harry", [1,2]}


# Short answer: No, you cannot do that.

# Here’s why:

# A set in Python only allows immutable (unchangeable) elements.
# The list [1,2] is mutable, so Python will throw an error even before you try to change it.