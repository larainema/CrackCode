#1.1
def check_string(s):
  string_list = list(s)
  if len(string_list) == len(set(string_list)):
    return True
  else:
    return False

string1 = 'abcdefg'
string2 = 'aaabb'
print check_string(string1)
print check_string(string2)

#1.2
def reverse_string(s):
  string_list = list(s)
  return string_list[::-1]

print ''.join(reverse_string(string1))
