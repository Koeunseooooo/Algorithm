n, k = map(int,input().strip().split())
items = list(map(int,input().split()))

# 멀티탭 수만큼 list 만들기
multiTap = [0]*n

cnt=0
for i in range(len(items)):
    # 현재 item이 이미 멀티탭에 꽂혀있는 경우 continue
    if items[i] in multiTap:
          continue
    else:
      # 자리가 남아있는 경우 멀티탭 꽂음
      if 0 in multiTap:
          multiTap[multiTap.index(0)] = items[i]

      # 자리가 안 남아있는 경우
      else:
        appear=[]
        # 멀티탭에 꽂힌 아이템 중 다시 등장하는 아이템은 나중에 뽑아야하므로 appear 리스트로 check
        for j in range(i+1,len(items)):
            if items[j] in multiTap:
                appear.append(items[j])

        # 멀티탭에 꽂힌 아이템 중 다시 등장하는 아이템이 존재한다면
        if(appear):
          result_list = list(dict.fromkeys(appear))
          for k in range(len(multiTap)):
            # 멀티탭에 꽂힌 아이템 중 다시 등장하지 않는 아이템을 뽑음
            if multiTap[k] not in result_list:
                  multiTap[k]=items[i]
                  cnt+=1
                  break
         
          # 만약 멀티탭에 꽂힌 아이템 중 다시 등장하지 않는 아이템이 아예 없거나, 
          # 다시 등장하는 아이템이 여러개인 경우 
          # 가장 순서가 가까운 아이템을 가장 나중에 뽑아야하므로 맨 뒷순서의 아이템을 뽑음
          else:
            multiTap[multiTap.index(result_list[-1])]=items[i]
            cnt+=1
        # 만약 멀티탭에 꽂힌 아이템 중 다시 등장하는 아이템이 한 개도 없다면, 멀티탭에서 아무거나 뽑음
        else:
          multiTap[0]=items[i]
          cnt+=1
    # print(multiTap,'멀티탭', cnt, '카운트')

print(cnt)

