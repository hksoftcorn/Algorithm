N = 10
arr = [i for i in range(1, 11)]
sel = [0] * N


def powerset(idx):
    if idx == N:
        # print(sel)
        # print(arr)
        cnt = 0
        for i in range(10):
            if sel[i]:
                cnt += arr[i]
        if cnt == 10:
            for i in range(10):
                if sel[i]:
                    print(arr[i], end=" ")
            print()

    else:
        sel[idx] = 1
        powerset(idx + 1)
        sel[idx] = 0
        powerset(idx + 1)


powerset(0)
