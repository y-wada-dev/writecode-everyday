# ヒープのアルゴリズム

array = [None, 15, 30, 10, 60, 5, 20, 45]
length = len(array)-1

def make_heap():
    for i in range(2, length + 1):
        j = i
        while j > 1:
            k = j // 2
            if array[j] > array[k]:
                temp = array[j]
                array[j] = array[k]
                array[k] = temp
                j = k
            else:
                break
            print(array[1:])  # Noneは除いて表示

make_heap()



    