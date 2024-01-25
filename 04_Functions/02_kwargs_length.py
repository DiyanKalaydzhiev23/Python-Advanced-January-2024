def kwargs_length(**kwargs) -> int:
    # {'name': 'Peter', 'age': 25}
    return len(kwargs)


dictionary = {'name': 'Peter', 'age': 25}

print(kwargs_length(**dictionary))  # ** => kwargs_length(name="Peter", age=25)
print(kwargs_length(name="Peter", age=25))