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
            bool_exp = True
            for h in range(max_length):
                table[self.values[i]].append(bool_exp)
                count += 1
                if count == alternate:
                    count = 0
                    if bool_exp:
                        bool_exp = False
                    else:
                        bool_exp = True
        return table

    def logic_table(self):
        table = self.create_table()
        if len(table.keys()) < 2:
            return table
        and_title = ""
        or_title = ""
        sort_keys = sorted(table.keys())
        for i in range(len(sort_keys)):
            if i == len(sort_keys) - 1:
                and_title += sort_keys[i]
                or_title += sort_keys[i]
            else:
                and_title += sort_keys[i] + " AND "
                or_title += sort_keys[i] + " OR "
        table[and_title] = []
        table[or_title] = []
        for i in range(len(table[sort_keys[0]])):
            vals = []
            for key in sort_keys:
                vals.append(table[key][i])
            table[and_title].append(self._and_gate(vals))
            table[or_title].append(self._or_gate(vals))
        return table

    def sort_columns(self):
        table = self.logic_table()
        data = []
        logic = []
        for key in table.keys():
            if len(key) > 1:
                logic.append(key)
            else:
                data.append(key)
        return sorted(data) + sorted(logic)

    def _and_gate(self, values):
        for arg in values:
            if arg == False:
                return False
        return True

    def _or_gate(self, values):
        for arg in values:
            if arg == True:
                return True
        return False


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
