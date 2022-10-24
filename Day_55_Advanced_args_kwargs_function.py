class User:
    def __int__(self, name):
        self.name = name
        self.is_opened = False

def is_authenticated_decorater(*args):
    def wrapper(*args):
        if args[0].is_opened == True:
            function()
    return wrapper

def create_blog(user):
    print(f"This is {user.name}'s new blog.")

new_user = User("Saiful")
create_blog(new_user)