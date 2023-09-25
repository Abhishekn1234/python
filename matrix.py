first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
matrix = []
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
    encode string="".join([matrix[j][i] for i in range(m) for j in range(n)])
    part=r'(?<=[a-zA-Z0-9])[^a-zA-Z0-9]+(?=[A-Za-z0-9])'
    print(re.sub(part,' ',encode string))