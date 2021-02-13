int_val = 4
str_val = 'PythonIsBest'
flt_val = 24.56

print(f'The integer hash value is: {hash(int_val)}')
print(f'The string hash value is: {hash(str_val)}')
print(f'The float hash value is: {hash(flt_val)}')

class Password:
    def __init__(self, password, username):
        self.password = password
        self.username = username

    def __eq__(self, other):
        return self.password == other.password and self.username == other.username
        
    def __hash__(self):
        print('The hash is: ')
        return hash((self.password, self.username))

user = Password('password123', 'coolguy23')
print(hash(user))
