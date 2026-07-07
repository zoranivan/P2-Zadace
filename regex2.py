import re

email_regex = r"^[a-zA-Z]+\.[a-zA-Z]+@fpmoz\.sum\.ba$"
eduid_regex = r"^[a-zA-Z]+\.[a-zA-Z]+\d*@sum\.ba$"

mail = input("Unesi email: ")
korisnicki_eduid = input("Unesi eduid: ")

provjera_mail = re.search(email_regex, mail)
provjera_eduid = re.search(eduid_regex, korisnicki_eduid)

if provjera_mail:
    print("Email je ispravan")
else:
    print("Email nije ispravan")

if provjera_eduid:
    print("EduId je ispravan")
else:
    print("EduId nije ispravan")