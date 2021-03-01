product_list = [
    ('iPhone', 100),
    ('Mac Pro', 1000),
    ('iPad Mini', 150),
    ('Bike', 50)
]


budget = input("請輸入你的購買預算：")
shopping_car = []


if budget.isdigit():
    budget = int(budget)
    while True:
        for index, item in enumerate(product_list):
            #print(product_list.index(item), item)
            print(index, item)

        user_choice = input("請選擇要購買的商品:")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(product_list) and user_choice >= 0:
                product_itme = product_list[user_choice]
                if product_itme[1] <= budget:
                    shopping_car.append(product_itme)
                    budget -= product_itme[1]
                    print("Added %s into shopping car, your current balance is \033[31;1m%s\033[0m" %(product_itme, budget))
                else:
                    print("\033[41;1m你的餘額[%s]...不夠了!!!\033[0m" %(budget))
                    break
            else:
                print("你輸入錯誤商品代號\033[34;1m[%s]\033[0m了，請重新輸入" %(user_choice))
        elif user_choice == 'q':
            print("---------------購買清單---------------")
            for p in shopping_car:
                print(p)
            print("\033[41;1m你的餘額[%s]...\033[0m" % (budget))
            print('Exit')
            exit()
        else:
            print("invalid option")
