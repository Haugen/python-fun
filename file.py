with open('test-file.txt', mode='w') as f:
    f.write('A new line')

with open('test-file.txt', mode='a') as f:
    f.write('\nWriting a new line!')

