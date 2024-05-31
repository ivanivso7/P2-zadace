import re

def izdvoji_email_adrese(tekstporuke):
    regexizraz = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    email_adrese = re.findall(regexizraz, tekstporuke)
    return email_adrese

poruka = "Moja e-mail adresa je: ivan.filipovic5@fpmoz.sum.ba"
email_adrese = izdvoji_email_adrese(poruka)
print("Pronađene e-mail adrese:")
for email in email_adrese:
    print(email)
