# Creating a class:
class User:
    #Creating an attribute:
    def __init__(self, user_id, user_name):
        self.user_id = user_id
        self.user_name = user_name
        self.followers = 0
        self.following = 0


    # Creating a method:
    def follow(self, user):
        user.followers += 1
        self.following += 1


# Creating an object from my class:
user_1 = User("001", "David")
user_2 = User("002", "Diego")

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

print(user_1.user_id, user_1.user_name)

# Calling an attribute from my object:
# user_1.id = "001"
# user_1.name = "David"
#
# print(f"Name: {user_1.name} --- ID number: {user_1.id}.")