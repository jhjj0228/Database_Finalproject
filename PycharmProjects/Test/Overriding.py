# -*-coding: cp949 -*-
import HouseJang





class HouseHyun(HouseJang.Name):

    lastname="현"



    def travel(self, where, day):
        print(("{} {} {} 가네").format(self.fullname, where, day))


if __name__ == "__main__":
    fullname=HouseHyun("인수")
    fullname.travel("미국", "20일")