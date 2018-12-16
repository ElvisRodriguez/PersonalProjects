#group: sum 1 to 100 skip by 1

import importlib

def parse_string(string):
  parsed_string = string.split()
  return parsed_string

def command_map(parsed_string):
  commands = dict()
  commands['function'] = parsed_string[0]
  commands['start'] = int(parsed_string[1])
  commands['finish'] = int(parsed_string[3])
  if 'skip' in parsed_string:
    commands['skip'] = int(parsed_string[-1])
  return commands

def create_function(commands, operation_map):
  lines = []
  operation = operation_map[commands['function']]
  lines.append('def {}():'.format(commands['function']))
  begin = 1 if operation == '*' else 0
  lines.append('\tresult = {}'.format(begin))
  s = commands['start']
  f = commands['finish']
  skip = commands['skip'] if 'skip' in commands else 0
  if skip == 0:
    lines.append('\tfor i in range({}, {}):'.format(s,f))
  else:
    lines.append('\tfor i in range({}, {}, {}):'.format(s,f,skip))
  lines.append('\t\tresult {}= i'.format(operation))
  lines.append('\treturn result')
  return '\n'.join(lines)

def write_program(name, program):
  with open(name, 'w') as file:
    file.write(program)

def create_module(name):
  name = name.replace('.py', '')
  module = importlib.import_module(name)
  return module

if __name__ == '__main__':
  operation_map = {
    'sum' : '+',
    'subtract' : '-',
    'multiply' : '*',
    'divide' : '//',
    'modulo' : '%'
  }
  parsed = parse_string('modulo 100 to 50 skip by -1')
  commands = command_map(parsed)
  func = create_function(commands, operation_map)
  write_program('output.py', func)
  module = create_module('output.py')
  print('Your Program:')
  print(func)
