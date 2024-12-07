import sys

def array_path(n, m):
    array = list(range(1, n + 1))
    path = []
    current_pos = 0
    
    while True:
        path.append(array[current_pos])
        current_pos = (current_pos + m - 1) % n
        if current_pos == 0:
            break
            
    return ''.join(map(str, path))

if __name__ == '__main__':
    if len(sys.argv) == 3:
        n, m = int(sys.argv[1]), int(sys.argv[2])
        result = array_path(n, m)
        print(result)
    else:
        print('Error: expected 3 arguments')