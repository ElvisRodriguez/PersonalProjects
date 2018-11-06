def create_bin_list(val_string, reverse=False):
    r = len(val_string)
    result = []
    for i in range(2**r):
        val = str(bin(i))
        val = val.replace('0b', '', 1)
        if len(val) < 2 and r > 1:
            val = '0' + val
        result.append(val)
    if reverse:
        r = 2**r
        first = result[0:r // 2]
        second = result[r // 2:]
        second = second[::-1]
        result = first + second
    return result


def convert_b10(bin_str):
    n = len(bin_str)
    result = 0
    for char in bin_str:
        coeff = int(char)
        result += coeff * 2**(n - 1)
        n -= 1
    result = str(result)
    if len(result) == 1:
        result += ' '
    return result


def create_k_map(val_strA, val_strB):
    k_map = []
    for i in range(2**len(val_strA)):
        k_map.append([0] * 2**len(val_strB))
    return k_map


def print_k_map(k_map):
    for row in k_map:
        print(row)


def karnough_map(x, y):
    k_map = create_k_map(x, y)
    if len(x) > 1:
        x_bins = create_bin_list(x, reverse=True)
    else:
        x_bins = create_bin_list(x)
    if len(y) > 1:
        y_bins = create_bin_list(y, reverse=True)
    else:
        y_bins = create_bin_list(y)
    for i in range(len(k_map)):
        for j in range(len(k_map[i])):
            bin_str = x_bins[i] + y_bins[j]
            b10 = convert_b10(bin_str)
            k_map[i][j] = b10
    print_k_map(k_map)


if __name__ == '__main__':
    print('2-Variable K-Map')
    karnough_map('X', 'Y')
    print('3-Variable K-Map')
    karnough_map('X', 'YZ')
    print('4-Variable K-Map')
    karnough_map('WX', 'YZ')
    print('5-Variable K-Map')
    karnough_map('AB', 'XYZ')
    print('6-Variable K-Map')
    karnough_map('ABC', 'XYZ')
