class Item_Structure:
    # 구조체처럼 한번에 변수들을 관히하기 위해 클래스 생성
    def __init__(self, item_number, weight, value):
        self.item_index = item_number
        self.weight = weight
        self.value = value
        # 무게 대비 가치
        self.real_value = value // weight
    # 이후 내림차순 정렬을 할 때의 정렬 기준은 real_value로 설정해야하므로 __lt__함수를 사용한다.
    def __lt__(self, other):
        return self.real_value < other.real_value
         

def solve_fractional_knapsack (capacity,weight, value):
    items=[]
    for i in range(len(weight)):
        items.append(Item_Structure(i,weight[i], value[i]))
    # 내림차순 정렬을 해주어야하므로 reverse=True로 지정한다.
    items.sort(reverse=True)
    # 배낭에 들어가는 아이템과 그 개수를 담기 위한 selected_items 배열 선언
    selected_items=[]
    total_value = 0
    for i in items:
        current_weight = i.weight
        current_value = i.value
        if capacity - current_weight >= 0:
            capacity -= current_weight
            total_value += current_value
            # [아이템 number,fraction 개수] 를 selected_items 리스트에 저장
            selected_items.append([str(i.item_index)+"th items",1])
        else:
            # 아이템을 쪼갠다 = fraction !
            fraction = capacity / current_weight
            total_value += current_value * fraction
            capacity = capacity - (current_weight * fraction)
            selected_items.append([str(i.item_index)+"th items",fraction])
            break #fraction 되었다는 의미 = 이제 배낭 capacity만큼 찼다는 의미이므로 for문 break
    return total_value, selected_items
 
 
if __name__ == "__main__":
    capacity = 16
    weight = [6, 10, 3, 5, 1, 3]
    value = [60, 20, 12, 80, 30, 60]
    
    result = solve_fractional_knapsack(capacity,weight,value)

    print("Maximum value in Knapsack :", result[0])
    print("Associated items with their fraction numbers :")

    for i in range(len(result[1])):
        print(result[1][i])
    
 
# This code is contributed by vibhu4agarwal