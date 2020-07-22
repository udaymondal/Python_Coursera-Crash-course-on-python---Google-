# changing email address from old domain to new domain

def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email

print(replace_domain("um@gmail.co.us", "out.com", "yahoo.co.uk"))

print(replace_domain("um@ovimail.com.com", "ovimail.com", "yahoo.co.uk"))

# taking email and domain as input from user - 

email = input()
old_domain = input()
new_domain = input()
print(replace_domain(email, old_domain, new_domain))
