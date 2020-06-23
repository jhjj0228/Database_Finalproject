# -*-coding: cp949 -*-

class Name:

    lastname="장"

    def __init__(self,name):
        self.fullname=self.lastname+name
        print("{}시작".format(self.fullname))

    def travel(self, where):
        print ("{} {} 여행을 가다". format(self.fullname, where) )

    def __del__(self):
        print("{} 종료".format(self.fullname))


if __name__=="__main__":

    # pey=Name("혁준")
    # pey.travel("서울")

    a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
    print(list(a.keys()))
    print(list(a.items()))
    for k in a.keys():
        print(k)
