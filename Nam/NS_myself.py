
import introfamily
import sys
args = sys.argv

input1 = args[1]
input2 = args[2]
input3 = args[3]

nam = introfamily.IntroFam(input1, input2, input3)
print(nam.name_out())
print(nam.age_out())
print(nam.cat_out())
