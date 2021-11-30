class User:
    def __init__(self, fname, lname, role):
        roles = ('Admin', 'Sales', 'Manager')
        if role in roles:
            self.__userRole = role
            self.__firstName = fname
            self.__lastName = lname
        else:
            print('Please set valid user role')

    @property
    def firstName(self):
        return self.__firstName

    @property
    def lastName(self):
        return self.__lastName

    @property
    def userRole(self):
        return self.__userRole

#    @userRole.setter
#    def set_role(self, role):
#        roles = ('Admin', 'Sales', 'Manager')
#        if role not in roles:
#            print('Please set valid user role')

    def display_userinfo(self):
        print(f'{self.__firstName} {self.__lastName} is {self.__userRole}')


def main():
    user1 = User('Kate', 'Tomsone', 'Admin')
    user1.display_userinfo()
    user2 = User('Mary', 'Smith', 'Manager')
    user2.display_userinfo()
    user3 = User('Ivan', 'Ivanov', 'Sales')
    user3.display_userinfo()
    user4 = User('Ivan', 'Ivanov', 'HR')


if __name__ == "__main__":
    main()
