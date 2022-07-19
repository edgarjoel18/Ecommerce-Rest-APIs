from models.user import User
import hmac
# users = [
#    User(1, "someusername", "password")
# ]

# username_mapping = {u.username: u for u in users}
# username_mapping = {
#     'firstname': {
#         "id": 1,
#         "username": "firstname",
#         "password": "password"
#     }
# }

# userid_mapping = {user.id: user for user in users}


# userid_mapping = {
#     1: {
#         "id": 1,
#         "username": "firstname",
#         "password": "password"
#     }
# }


def authenticate(username, password):
    # user = username_mapping.get(username, None)
    user = User.find_by_username(username)
    if user and hmac.compare_digest(user.password, password):
        return user


def identify(payload):
    user_id = payload['identity']
    return User.find_by_id(user_id)
    # return userid_mapping.get(user_id)
