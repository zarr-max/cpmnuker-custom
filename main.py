from cpmnuker import CPMNuker

nuker = CPMNuker()

username = input("Username: ")
password = input("Password: ")

login_result = nuker.login(username, password)
print("Login:", login_result)

if "token" in login_result:
    print("Set ID ke 123456789")
    print(nuker.change_id("123456789"))

    print("Set money ke 9999999")
    print(nuker.set_money(9999999))
