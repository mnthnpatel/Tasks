import mysql.connector as connector


class DataBase:
    def __init__(self):
        self.con = connector.connect(host="localhost",
                                     port="3306",
                                     user="root",
                                     password="",
                                     database="test")

        # Create A Table...
        query = 'Create Table If Not Exists user(userId int primary key, userName varchar(200), phone varchar(12))'
        cur = self.con.cursor()
        cur.execute(query)
        print("Created")


    # Inserting Data...
    def insert_User(self,UserId,UserName,Phone):
        query = "insert into user(userId,userName,phone) values({},'{}','{}')".format(UserId,UserName,Phone)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("User Saved To DB")


    # Fetching All Data...
    def fetch_all(self):
        query = "select * from user"
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("UserId : ",row[0])
            print("UserName : ",row[1])
            print("Phone : ",row[2])
            print()

            
    # Delete User...
    def delete_user(self,userId):
        query = "delete from user where userId = {}".format(userId)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print(f"{userId} Deleted Successfully...")


    # Update Data...
    def update_user(self,newName,newPhone,userId):
        query = "UPDATE `user` SET `userName` = '{}',`phone` = '{}' WHERE `user`.`userId` = {}".format(newName,newPhone,userId)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Updated Successfully...")



# Main Coding...

b = DataBase()

# b.insert_User(444,"SMG","4000055555")
# b.insert_User(666,"Jin","1000055555")
# b.insert_User(777,"Sniper","2000055555")
# b.insert_User(888,"Nade","3000055555")

# b.delete_user(444)

# b.fetch_all()

b.update_user('Nade','3000055555',888)