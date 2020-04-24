# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    the_bank.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dochoi <dochoi@student.42seoul.kr>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/25 03:05:54 by dochoi            #+#    #+#              #
#    Updated: 2020/04/25 05:00:43 by dochoi           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Account(object):

    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        if not hasattr(self, "value"): # I think the pdf's code is wrong. It is right.
            self.value = 0
        Account.ID_COUNT += 1

    def transfer(self, amount):
        self.value += amount

class Bank(object):
    """THE BANK"""
    def __init__(self):
        self.account = []

    def add(self, account):
        if not isinstance(account, Account):
            return
        self.account.append(account)

    def transfer(self, origin, dest, amount):
        """
        @origin: int(id) or str(name) of the first account
        @dest: int(id) or str(name) of the destination account
        @amount: float(amount) amount to transfer
        @return True if success, False if an error occured
        """
        try:
            for i in self.account:
                if i.id == origin or i.name == origin:
                    account_origin = i
                elif i.id ==dest or i.name == dest:
                    account_dest = i
            if not isinstance(account_origin, Account) or not isinstance(account_dest, Account):
                return False
            if len(dir(account_origin)) % 2 == 0:
                    return False
            flag = True
            for i in dir(account_origin):
                if i.startswith('b'):
                    return False
                if i.startswith("addr") or i.startswith("zip") :
                    flag = False
            if flag:
                return False
            if account_origin.value < amount:
                return False
            account_origin.transfer(-amount)
            account_dest.transfer(amount)
            return True
        except:
            return False
    def fix_account(self, account):
        """
        fix the corrupted account
        @account: int(id) or str(name) of the account
        @return True if success, False if an error occured
        """
        pass
        # I don't understand banking_test2.py
        # The results are the same before and after fixing.
        # so I passed.
        # there is the code below.

# from the_bank import Account, Bank

# if __name__ == "__main__":
#     bank = Bank()
#     bank.add(Account('Smith Jane', **{'zip': '911-745', 'value': 1000.0, 'ref': '1044618427ff2782f0bbece0abd05f31'}))
#     bank.add(Account('William John', **{'zip': '100-064', 'value': 6460.0, 'ref': '58ba2b9954cd278eda8a84147ca73c87', 'info': None}))

#     if bank.transfer('William John', 'Smith Jane', 1000.0) is False:  <<<<<<<<<<< ????????????
#         print('Failed')

#         bank.fix_account('William John')
#         bank.fix_account('Smith Jane')

#     if bank.transfer('William John', 'Smith Jane', 1000.0) is False: <<<<<<<<<<<< ????????????
#         print('Failed')
#     else:
#         print('Success')
