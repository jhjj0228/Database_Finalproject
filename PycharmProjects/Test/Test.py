import HouseJang




a=HouseJang.Name("혁준")
a.travel("부산")
print("프린트")
b=abs(-3)
print(b)


#for문

family = ['mother', 'father', 'gentleman', 'lady']

for x in family:
    print("{} {}".format(x, len(x)))




#for문
marks = [90, 25, 67, 45, 80]

number = 0
for mark in marks:
    number = number +1
    if mark < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다. " % number)


#for문
marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." % (number+1))