#Binary Representation of numbers

#O(lg n)
def to_binary(num, base=2):
  if num == 0:
    return str(0)
  if num == 1:
    return str(1)
  output = ''
  while num > 0:
    output = str(num % base) + output
    num //= base
  return output

#O(n lg n) where n = 2^len(bin_str) - 2^(len(bin_str) - 1)
def to_num(binary_num):
  if len(binary_num) > 1:
    while binary_num[0] == '0':
      binary_num = binary_num.replace('0', '', 1)
  if binary_num == '0':
    return 0
  n = len(binary_num)
  start = 2 ** (n - 1)
  end = (2 ** n)
  while start < end:
    if to_binary(start) == binary_num:
      return start
    start += 1

#O(n) where n is len(bin_string)
def bin_to_num(bin_string):
  result = 0
  exponent = len(bin_string) - 1
  for char in bin_string:
    coeff = int(char)
    result += coeff * 2 ** exponent
    exponent -= 1
  return result

for i in range(33):
  binary_string = to_binary(i)
  print(to_num(binary_string))
