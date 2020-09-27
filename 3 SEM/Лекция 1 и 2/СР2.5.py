"""
  Логинова Софья ИВТ2.3
  Самостоятельная работа №2 

  Задание №5
  (A∨B)∧¬C
    
  Задание №5
  https://repl.it/@sonyadk/SAMwork25

  Задание №7
  https://repl.it/@sonyadk/SAMwork27

  Задание №21
  https://repl.it/@sonyadk/SAMwork221

  Задание №3 и Задание №15
  https://repl.it/@sonyadk/SAMwork33

"""

a = [1, 1, 1, 1, 0, 0, 0, 0]
b = [1, 1, 0, 0, 1, 1, 0, 0]
c = [1, 0, 1, 0, 1, 0, 1, 0]
f = []
delimiter = "—"
header = "|  A  ||  B  ||  C  ||  F  |"
print(delimiter * len(header))
print('|       F = (A∨B)∧¬C       |')
for i in range(8):
    f.append(int((bool(a[i]) or bool(b[i])) and (not bool(c[i]))))
print(delimiter * len(header))
print(header)
print(delimiter * len(header))
for i in range(8):
    res = "|  " + str(a[i]) + "  ||  " + str(b[i]) + "  ||  " + str(
        c[i]) + "  ||  " + str(f[i]) + "  |"
    print(res)
    print(delimiter * len(header))
