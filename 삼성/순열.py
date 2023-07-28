def permutation(arr, r):
    # 1.
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))] # 방문

		# 실제 순열 만들기
		# chosen - 순열 원소를 저장하는 배열 
    def generate(chosen, used): 
        # 2.
        if len(chosen) == r:
            print(chosen)
            return
	
        for i in range(len(arr)):
            if not used[i]:
                chosen.append(arr[i])
                used[i] = 1 # 방문
                generate(chosen, used)
                used[i] = 0 # 마지막에 방문한 원소들을 하나씩 미방문으로 체크
                chosen.pop()
    generate([], used)

permutation('ABCD', 2)
permutation([1, 2, 3, 4, 5], 3)