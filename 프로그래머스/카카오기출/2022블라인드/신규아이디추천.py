def solution(new_id):
    answer = ""
    new_id = new_id.lower()
    arr = ""
    for n in new_id:
        if n.isalnum() or n in "_-.":
            # if n.isalpha() or n.isdigit() or n=='_' or n=='-' or n=='.':
            arr += n
    while ".." in arr:
        arr = arr.replace("..", ".")
    new_id = "".join(arr)
    new_id = new_id.strip(".")
    if len(new_id) < 1:
        new_id = "a"
    if len(new_id) >= 16:
        new_id = new_id[:15]
        # print(new_id,1)
        if new_id[-1] == ".":
            new_id = new_id[:14]
    if len(new_id) <= 2:
        final = new_id[-1]
        while len(new_id) < 3:
            new_id += final

    return new_id
