import sys 

def read_numbers(filename):
    with open(filename, 'r') as file:
        return [int(line.strip()) for line in file]

def min_moves(nums):
    nums.sort()
    n = len(nums)
    
    median = nums[n // 2] 
    moves = sum(abs(num - median) for num in nums)
    return moves

if __name__ == '__main__':
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        nums = read_numbers(filename)
        moves = min_moves(nums)
    
        print(moves)
    else:
        print('Error: expected 2 arguments')