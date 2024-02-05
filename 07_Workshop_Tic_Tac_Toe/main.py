def custom_all(iterable):
    for el in iterable:
        if not el:
            return False

    return True


print(custom_all([True, 0, "ji"]))