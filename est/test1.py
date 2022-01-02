# 로봇을 이용하여 여러 종류의 완제품을 만드는 공장을 운영하려고 합니다.
#
# 로봇 한 대는 부품 한 종류만 처리할 수 있으며,
#
# 완제품의 종류에 따라 필요한 부품이 다를 수 있습니다. 이때,
#
# 로봇 r대로 최대한 다양한 완제품을 만들려 합니다.
#
# 예를 들어, 각 완제품을 만들 때 다음과 같은 부품이 필요하고, 살 수 있는 로봇은 최대 두 대라고 가정하겠습니다(번호는 0번부터 시작합니다).

# 따라서, 최대한 다양한 완제품을 만들려면 부품 0을 처리하는 로봇과 부품 1을 처리하는 로봇을 구매해야 합니다.
#
# 완제품을 만드는 데 필요한 부품의 정보 needs와 최대로 구매 가능한 로봇 수 r이 매개변수로 주어질 때,
#
# 최대 몇 종류의 완제품을 만들 수 있는지 return 하도록 solution 함수를 완성해 주세요.
#
from itertools import combinations

def solution(needs, r):
    # 부품의 번호 수 
    numberOfPart = len(needs[0])
    # 봅을 수 있는 부품 조합 
    combinationParts = list(combinations(range(numberOfPart), r))
    # 뽑는 부품 별 최대 갯수
    countPartArray = []

    #  뽑는 부품 반복 
    for combinationPart in combinationParts:
        # 뽑지않는 부품 
        missinParts = []
        
        # 뽑지 않는 부품 저장 
        for missingPart in range(numberOfPart):
            if missingPart not in combinationPart:
                missinParts.append(missingPart)
        # 완제품 갯수 
        countProduct = 0
        # 제품 반복
        for product in needs:
            canMakeProdcct = True

            # 제품의 파트 아닌 것 체크
            for part in missinParts:
                if product[part] == 1:
                    canMakeProdcct = False
            # 완제품 갯수 추가
            if canMakeProdcct:
                countProduct += 1
        # 뽑는 부품 별 최대 갯수 추가
        countPartArray.append(countProduct)

    return max(countPartArray)


if __name__ == '__main__':
    print(solution([[1, 0, 0], [1, 1, 0], [1, 1, 0], [1, 0, 1], [1, 1, 0], [0, 1, 1]], 2))
