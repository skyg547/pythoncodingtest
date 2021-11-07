# # 음식점에서 하루 동안의 판매 수익을 계산
# # 아래 3개의 표는 각각 음시점에서 사용하는 재료 , 판매하는 메뉴 , 하루 판매 실젝에 대한 정보을 나타내는 예시
#
# # 음식점에서는 메뉴를 만들기위해 재료를 구매해온다
#
# # 재료 r의 구매비용은 10원 a, 의 구매 비용응 23원 ,재료 t의 구매 비용은 124 원, 재료 k 의 구매 비용은 9 원
#
# # 메뉴 pizza, Hambuger, bread, iceCream, shaveDice ,jucce, 필요한 재료 arraak , 판매가 145
#
# # 총 재료비는 98 이다
#
# # 수익은 47 이다
#
# # 똑같은 재료를 사용
# # 재료비는 같으나 발생할수 있는 수익이 다르다
# #  수익이 아닌 손실 날수 있는 메뉴도 있다 .
#
# # 하루동안의 총수익을 return 하도록 함수를 완성해주세요
#
# 1 ≤ ings의 길이 ≤ 26
# ings의 각 원소는 "ING_NAME ING_PRICE" 형식입니다.
# ING_NAME은 재료의 이름을 나타내며, 알파벳 소문자 하나로 표시됩니다.
# ING_PRICE는 재료의 가격을 나타내는 정수입니다.
# 1 ≤ ING_PRICE ≤ 1000
# ING_NAME과 ING_PRICE는 1개의 공백으로 구분되어 있습니다.
# ings에서 ING_NAME은 중복되어 나타나지 않습니다.
# 1 ≤ menu의 길이 ≤ 100
# menu의 각 원소는 "MENU_NAME ING_LIST MENU_PRICE" 형식입니다.
# MENU_NAME은 식당에서 판매하고 있는 메뉴의 이름을 나타내며, 알파벳 대문자로 구성된 문자열입니다.
# 3 ≤ MENU_NAME의 길이 ≤ 10
# ING_LIST는 메뉴를 만드는데 필요한 재료들을 나타내는, 알파벳 소문자로 구성된 문자열입니다.
# 1 ≤ ING_LIST의 길이 ≤ 20
# ings에 담겨있는 재료들만 ING_LIST에 나타납니다.
# MENU_PRICE는 메뉴의 가격을 나타내는 정수입니다.
# 1 ≤ MENU_PRICE ≤ 20000
# MENU_NAME, ING_LIST, MENU_PRICE는 1개의 공백으로 구분되어 있습니다.
# menu에서 MENU_NAME은 중복되어 나타나지 않습니다.
# 1 ≤ sell의 길이 ≤ menu의 길이 ≤ 100
# sell의 각 원소는 "MENU_NAME SELL_COUNT" 형식입니다.
# MENU_NAME은 판매된 메뉴의 이름을 나타내며, 알파벳 대문자로 구성된 문자열입니다.
# 3 ≤ MENU_NAME의 길이 ≤ 10
# menu의 MENU_NAME으로 나타난 것들만 sell의 MENU_NAME에 나타납니다.
# SELL_COUNT는 메뉴가 판매된 수량입니다.
# 1 ≤ SELL_COUNT ≤ 100
# MENU_NAME과 SELL_COUNT는 1개의 공백으로 구분되어 있습니다.
# sell에서 MENU_NAME은 중복되어 나타나지 않습니다.

def solution(ings, menu, sell):
    answer = 0
    ingredientDict = dict()
    saleDict = dict()

    for ingredient in ings:
        ingredientDict[ingredient.split()[0]] = ingredient.split()[1]

    for sale in menu:
        cost = 0

        for saleIngredient in sale.split()[1]:
            cost += int(ingredientDict[saleIngredient])

        saleDict[sale.split()[0]] = int(sale.split()[2]) - cost

    for saleCount in sell:
        answer += (saleDict[saleCount.split()[0]]) * int(saleCount.split()[1])

    return answer


if __name__ == '__main__':
    solution(["r 10", "a 23", "t 124", "k 9"],
             ["PIZZA arraak 145", "HAMBURGER tkar 180", "BREAD kkk 30", "ICECREAM rar 50", "SHAVEDICE rar 45",
              "JUICE rra 55", "WATER a 20"],
             ["BREAD 5", "ICECREAM 100", "PIZZA 7", "JUICE 10", "WATER 1"])
