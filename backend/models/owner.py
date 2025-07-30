import bcrypt

class Owner:
    @staticmethod
    def sign_up(db, username, password):
        if Owner.check_account_exists(db) == False:
            bytes = password.encode('utf-8')
            salt = bcrypt.gensalt()
            hashed = bcrypt.hashpw(bytes, salt)
            db.execute('INSERT INTO owner(username, hashed_password) VALUES (?, ?)', (username, hashed))
            return True
        else:
            return False

    @staticmethod
    def log_in(db, username, password):
        if Owner.check_account_exists(db, username):
            account = db.fetchone("owner")
            bytes = password.encode('utf-8')
            if username == account[1] and bcrypt.checkpw(bytes, account[2]):
                return True
            else:
                return False
        else:
            return False
    
    @staticmethod
    def check_account_exists(db, username = None):
        account = db.fetchall("owner")
        if account == []:
            return False
        else:
            if username == account[0][1]:
                return True

# bcrypt explaination
# # password = '123'
# # bytes = password.encode('utf-8')
# # salt = bcrypt.gensalt()
# # hashed = bcrypt.hashpw(bytes, salt)
# # print(hashed)
# # # check 
# # password2 = '1234'
# # bytes2 = password2.encode('utf-8')
# # check = bcrypt.checkpw(bytes2, hashed)
# # print(check)