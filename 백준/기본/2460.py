off_arr=[]
on_arr=[]
for _ in range(10):
    off, on = map(int, input().split())
    off_arr.append(off)
    on_arr.append(on)

max=0 
acc=0 #현재 탑승인원(누적값)
for i in range(10):
    acc+=on_arr[i]
    acc-=off_arr[i]
    if(max < acc):
        max=acc
print(max)