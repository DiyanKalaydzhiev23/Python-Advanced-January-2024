from re import findall


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MoreThanOneAtSymbol(Exception):
    pass


class InvalidNameError(Exception):
    pass


VALID_DOMAINS = ("com", "bg", "org", "net")
MIN_NAME_SYMBOLS_COUNT = 4

pattern_name = r'\w+'  # a1234_ -> [a1234_]; a??123 -> [a, 123]

email = input()

while email != "End":

    if email.count("@") > 1:
        raise MoreThanOneAtSymbol("Email should contain only one @ symbol!")
    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @!")
    if len(email.split("@")[0]) <= MIN_NAME_SYMBOLS_COUNT:
        raise NameTooShortError("Name must be more than 4 characters!")
    if email.split(".")[-1] not in VALID_DOMAINS:
        raise InvalidDomainError(f"Domain must be one of the following: {', '.join('.' + d for d in VALID_DOMAINS)}")
    if findall(pattern_name, email.split("@")[0])[0] != email.split("@")[0]:
        raise InvalidNameError("Name must contain only letters, digits and underscores!")

    print("Email is valid")

    email = input()
