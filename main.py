numbers = [4, 6, 11, 9, 3, 7, 8]
chet_list = []
nechet_list = []


for i in numbers:
    if i % 2 == 0:
        chet_list.append(i)
    else:
        nechet_list.append(i)

print(f'Жуп сандар: {chet_list}')
print(f"Так сандар: {nechet_list}")
