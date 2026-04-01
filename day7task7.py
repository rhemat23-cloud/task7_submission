# Higher-Order Function: accepts a list and a function
def process_users(users, func,use_filter=False):
    """
    Processes a list of users using the provided function.
    
    :param users: list of user data (strings, dicts, etc.)
    :param func: function to apply to each user
    :param use_filter: if True, uses filter; otherwise uses map
    :return: list of processed users
    """

    if not callable(func):
        raise TypeError("func must be a callable function")
    if not isinstance(users, list):
        raise TypeError("users must be a list")

    if use_filter:
        return list(filter(func, users))
    else:
        return list(map(func, users))


# Example 1: Using map to transform user names
users_list = ["naresh", "bavani", "chandru"]
uppercased_users = process_users(users_list, lambda u: u.upper())
print("Uppercased:", uppercased_users)
long_names = process_users(users_list, lambda u: len(u) > 3, use_filter=True)
print("Long names:", long_names)

