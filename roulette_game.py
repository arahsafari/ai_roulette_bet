import random

def main_gamble():
    result = random.randint(0,36)
    return result

def roulette_colour(number):
    red = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
    blk = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
    if number == 0:
        return "green"
    elif number in red:
        return "red"
    elif number in blk:
        return "black"
    else:
        print ("it broke")
        return 0

# def Mart(pasang,color, target, funds):
#     stratg = "Martingale"
#     start = funds
#     win = 0
#     loss = 0
#     rounds = 0
#     bet = pasang
#     while ((funds < target) and (funds > 0)):
#         if color != Gamble():
#             print(funds)
#             print(bet)
#             funds -= bet
#             bet *= 2
#             loss += 1
#             rounds += 1
#             print ("kalah , naikin pasangan ($" + str(bet) + ")")
#         else:
#             print(funds)
#             print(bet)
#             funds += bet
#             win += 1
#             rounds += 1
#             bet=pasang
#             print ("menang , turunin pasangan ($" + str(bet) + ")")
#     if funds >= target:
#         print ("menang , total duit = " + str(funds))
#         print ("total ronde =  " + str(rounds))
#         # d.write(stratg + "," + str(start) + "," + str(target) + "," + str(color) + "," + str(win) + "," + str(loss) + "," + str(rounds) + "," + str(funds) + "\n")
#     else:
#         print ("bangrut! uang sekarang = " + str(funds))
#         # d.write(stratg + "," + str(start) + "," + str(target) + "," + str(color) + "," + str(win) + "," + str(loss) + "," + str(rounds) + "," + str(funds) + "\n")
    
# def normal_bet():
    

init_fund = 100
bet = "red"

betting_money = 1
number_array = []
for i in range(0,5):
    number_array.append(main_gamble())


def normal_bet(number_array , init_fund , betting_money):
    for number in number_array:
        betting_place = roulette_colour(number)
        print(betting_place)
        if betting_place == bet:
            print("win")
            init_fund = init_fund + betting_money
        else:
            init_fund = init_fund - betting_money
            print("lose")
    

print(init_fund)

