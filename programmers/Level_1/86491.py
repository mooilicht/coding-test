def solution(sizes):
    row = []
    column = []
    for size in sizes:
        if size[0] < size[1]:
            size[0], size[1] = size[1], size[0]
        row.append(size[0])
        column.append(size[1])
    return max(row) * max(column)
