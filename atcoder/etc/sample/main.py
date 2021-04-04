line_list = ['line 1\n', 'line 2  \n']

# ジェネレータ式
stripped_iter = (line.strip() for line in line_list)
print(list(stripped_iter))
# リスト内包表記
stripped_list = [line.strip() for line in line_list]
