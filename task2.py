import argparse
def solve(s : str) -> int:
    start = 0
    count = 0
    max_len = 0
    not_repeat = set()

    while count < len(s):
       if s[count] not in not_repeat:
          not_repeat.add(s[count])
          count += 1
          max_len = max(max_len, count - start)
       else:
          not_repeat.remove(s[start])
          start += 1

    return max_len
          
if __name__ == '__main__':
  parser  = argparse.ArgumentParser()
  parser.add_argument("--str", type = str)
  args = parser.parse_args()
  args.str = input("Enter a string: ")
  print(solve(args.str))