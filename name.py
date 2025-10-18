words = ('kazak', 'car', 'laptop', 'madam', 'kg')
new_words = []
for n in words:
    if n == n[::-1]:
        new_words.append(n)
print(new_words)