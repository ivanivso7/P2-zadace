import re

def provjeri_email(email):
    regex_email = r"^[a-zA-Z]+\.[a-zA-Z]+@fpmoz\.sum\.ba$"
    if re.match(regex_email, email):
        return True
    else:
        return False

def provjeri_eduid(eduid):
    regex_eduid = r"^[a-zA-Z][a-zA-Z0-9]*@sum\.ba$"
    if re.match(regex_eduid, eduid):
        return True
    else:
        return False

def main():
    email = input("Unesite e-mail adresu: ")
    if provjeri_email(email):
        print("E-mail adresa je ispravna.")
    else:
        print("E-mail adresa nije ispravna.")

    eduid = input("Unesite eduID: ")
    if provjeri_eduid(eduid):
        print("EduID je ispravan.")
    else:
        print("EduID nije ispravan.")

main()
