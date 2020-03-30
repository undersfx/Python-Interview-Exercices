import subprocess

p1 = subprocess.run(['cat', 'word_count_alice.py'], capture_output=True) # "output=file" to redirect the output
print(f'Example 1:')
print(f'Output: {p1.stdout.decode()}')
print(f'Return code: {p1.returncode}')
print(f'Erro: {p1.stderr.decode()}')

p1 = subprocess.run(['cat', 'foo'], capture_output=True) # check=True to throw exception on non-zero exit code
print(f'\nExample 2:')
print(f'Output: {p1.stdout.decode()}')
print(f'Return code: {p1.returncode}')
print(f'Erro: {p1.stderr.decode()}')

with open('word_count_alice.py', 'rb') as file:
    p1 = subprocess.run(['grep', '-ni', 'alice'], capture_output=True, input=file.read())
    print(f'\nExample 3:')
    print(f'Output: {p1.stdout.decode()}')
    print(f'Return code: {p1.returncode}')
    print(f'Erro: {p1.stderr.decode()}')

p1 = subprocess.run('cat word_count_alice.py | grep -ni alice | wc -l', capture_output=True, shell=True)
print(f'\nExample 4:')
print(f'Output: {p1.stdout.decode()}')
print(f'Return code: {p1.returncode}')
print(f'Erro: {p1.stderr.decode()}')

p1 = subprocess.Popen(['python', 'word_count_alice.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
print(f'\nExample 5:')
print(f'Output: {p1.stdout}')
print(f'Return code: {p1.returncode}')
print(f'Erro: {p1.stderr}')
print(f'Popen readline: {p1.stdout.readline().decode()}')
