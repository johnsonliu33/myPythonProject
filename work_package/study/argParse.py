import argparse

def get_args():
    usage="https://yq.aliyun.com/articles/626646?utm_content=m_1000013890"
    parser = argparse.ArgumentParser(description="this is a calculator")
    parser.add_argument("num1",type=int,help="display num1")
    parser.add_argument("num2",type=int,help="display num2")
    args=parser.parse_args()
    if args[1] is not None & args[2] is not None:
        print(args[1])
        print(args[2])
        return True