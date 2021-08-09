def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Alexis", "lastname": "Montaño"}

    super_list=[
        {"firstname": "Alexis", "lastname": "Montaño"},
        {"firstname": "Yaril", "lastname": "Moreno"},
        {"firstname": "Mireya", "lastname": "Valenzuela"},
        {"firstname": "Saúl", "lastname": "Montaño"},
        {"firstname": "Loki", "lastname": "Montaño"},
    ]
    super_dict = {
    "natural_nums": [1, 2, 3, 4, 5],
    "integer_nums": [-1, -2, 0, 1, 2],
    "floating_nums": [1.1, 4.5, 6.43]
}

    for item in super_list:
        print(item["firstname"] , "-" , item["lastname"])

if __name__ == "__main__":
    run()