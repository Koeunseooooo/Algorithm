function solution(stones, k) {
  // 이분탐색을 사용한다.
  let left = 1;
  let right = 200000000;

  while (left <= right) {
    const mid = ((left + right) / 2) >> 0;

    let count = 0;
    for (let i = 0; i < stones.length; i++) {
      if (stones[i] - mid <= 0) count++;
      else count = 0;

      if (count === k) break;
    }

    if (count === k) right = mid - 1;
    else left = mid + 1;
  }

  return left;
}

// from itertools import product,permutations,combinations
// def solution(dice):
//     n=len(dice)
//     nums=[0]*(10**n)
//     nums[0]=1

//     for i in range(n):
//         for j in range(6):
//             nums[dice[i][j]]=1

//     part_dice=[]
//     for r in range(2,n+1):
//         for comb in list(combinations(list(range(n)),r)):
//             part_dice.append(comb)

//     candidate_dice=[]
//     for part in part_dice:
//         temp_dice=[]
//         for p in part:
//             temp_dice.append(dice[p])
//         candidate_dice.append(temp_dice)
//     for cur_dice in candidate_dice:
//         for _product in list(product(*cur_dice)):
//             for _permu in list(permutations(_product)):
//                 if _permu[0]==0:
//                     continue
//                 result=int(''.join(map(str,_permu)))
//                 nums[result]=1

//     answer=nums.index(0)
//     return answer
