class TruthTable:
    def __init__(self, values):
        self.values = values

    def create_table(self):
        max_length = 2 ** len(self.values)
        table = {}
        for i in range(len(self.values)):
            table[self.values[i]] = []
            alternate = max_length
            for j in range(i + 1):
                alternate /= 2
            count = 0
            bool_exp = 1
            for h in range(max_length):
                table[self.values[i]].append(bool_exp)
                count += 1
                if count == alternate:
                    count = 0
                    if bool_exp == 1:
                        bool_exp = 0
                    else:
                        bool_exp = 1
        return table


def format_table(table):
    sorted_keys = sorted(table.keys())
    result = ""
    result += '-' * (len(sorted_keys) * (len(sorted_keys))) + '\n'
    for i in range(len(sorted_keys)):
        if i  == len(sorted_keys) - 1:
            result += ' | ' + str(sorted_keys[i]) + ' |\n'
        else:
            result += ' | ' + str(sorted_keys[i])
    result += '-' * (len(sorted_keys) * (len(sorted_keys))) + '\n'
    for i in range(len(table[sorted_keys[0]])):
        for j in range(len(sorted_keys)):
            if j == len(sorted_keys) - 1:
                result += ' | ' + str(table[sorted_keys[j]][i]) + ' |\n'
            else:
                result += ' | ' + str(table[sorted_keys[j]][i])
        result += '-' * (len(sorted_keys) * (len(sorted_keys))) + '\n'
    return result
