import builtins

#
# print("the vars(builtins) are:", vars(builtins))

exception_count = 0

# vars(builtins) returns a dictionary
# .items() returns the dictionary's keys and values in a "list of a list"
for name, obj in vars(builtins).items():
    if isinstance(obj, type) and issubclass(obj, BaseException):
        print(name)
        exception_count += 1

print(f"There are {exception_count} built-in exceptions in Python 3.11.5")
