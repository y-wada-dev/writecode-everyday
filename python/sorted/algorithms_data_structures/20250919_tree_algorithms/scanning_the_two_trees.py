# 二本木の捜査

tree = [
    None,
    [2, 3],
    [4, 5],
    [6, 7],
    [8, 9],
    [10, 11],
    [12, 13],
    [14, None],
    [None, None],
    [None, None],
    [None, None],
    [None, None],
    [None, None],
    [None, None],
    [None, None]
]

result = []

def order(n: int) -> None:
    """中間走査（in-order）: 左 → 自分 → 右"""
    if n is None:
        return
    left, right = tree[n]
    order(left)
    print(n)
    result.append(n)
    order(right)

order(1)

print("中間走査の結果確認用:")
print(result)