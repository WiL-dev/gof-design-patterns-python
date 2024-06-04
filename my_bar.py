"""Bar logic related to entrance"""
import random

def is_blacklisted(name: str) -> bool:
    """Returns True if the name is in the blacklist"""
    if name.lower() == "bob":
        return True

    return False

def is_adult(age: int) -> bool:
    """Returns True if is and adult"""
    return age > 18

def is_id_valid(has_id) -> bool:
    """Returns True if has a valid ID"""
    return has_id and random.randint(1,2) == 2

def enter_club(name: str, age: int, has_id: bool) -> None:
    """Based on the name, age and if has or not id allows the person to enter the club"""
    if is_blacklisted(name):
        print(f"GTFO {name}")
    elif not is_adult(age):
        print("This is not a place for babies")
    elif not is_id_valid(has_id):
        print("No ID, no entrance")
    else:
        print(f'Welcome {name}!')
