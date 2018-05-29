
class User():
    id = 0
    def __init__(self,user_name,balance=0):
        self.user_name = user_name
        self.number = id
        User.id += 1
        self.balance = balance
    def set_balance(self,balance):
        if balance > 0:
            self.balance = balance

    def get_money(self,count):
        if count>0:
            self.balance += count
    def give_money(self,count):
        if count>0 and self.have_enought_money(count):
            self.balance -= count

    def have_enought_money(self,money):
        
        if self.balance - money < 0 :
            return False
        else:
            return True
   

def make_transaction(from_user,to_user,count):
    if not (isinstance(from_user,User) and isinstance(to_user,User)):
        print("Вы пытаетесь перевести деньги не нашему пользователю")
        return ""
    if from_user.have_enought_money(count):
        from_user.give_money(count)
        to_user.get_money(count)
    else:
        print("Недостаточно средств для обработки транзакции")

Vovan_1  = 1
Serega = User("Serega",100500)
Vovan = User("Vovan",500)
make_transaction(Serega,Vovan_1,100600)
input()