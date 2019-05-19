try:
    assert (1 == 0)
except:
    print("断言失败")
else:
    print("断言成功")
finally:
    print("不论失败还是成功都执行")
