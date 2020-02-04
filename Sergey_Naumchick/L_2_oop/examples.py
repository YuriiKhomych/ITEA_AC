def mu_func(api):
    if api in [1, 2, 3, 4]:
        my_dict = {
            1: "Facebook",
            2: "Google",
            3: "Insta"
        }[api]

        return my_dict
    else:
        return "index is out if range!"


print(mu_func(1))
print(mu_func(0))
