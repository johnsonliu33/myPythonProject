class MobilePhone:
    def coler(self):
        print("MobilePhone color is  multicoloured ...")


class HuaWei(MobilePhone):  # 继承MobilePhone
    def coler(self):  # overrides --> color()
        print("lenove color is black ...")

    def sys(self):
        print("HuaWei system is qilin ...")


class Iphone(MobilePhone):  # 继承MobilePhone
    def coler(self):  # overrides --> color()
        print("mac color is white ...")


class XiaoMi(MobilePhone):  # 继承MobilePhone
    pass


mp = MobilePhone()
# mp.coler()

hw = HuaWei()
# hw.coler()
hw.sys()

ph = Iphone()
# ph.coler()

xm = XiaoMi()


# xm.coler()


def demo_color(mp):
    mp.coler()


for item in [mp, hw, ph, xm]:
    demo_color(item)  # 多态 : 根据不同的参数，访问不同的class
"""
HuaWei system is qilin ...
MobilePhone color is  multicoloured ...
lenove color is black ...
mac color is white ...
MobilePhone color is  multicoloured ...
"""
