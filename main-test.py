from main import f_sum

def TestSum():
    assert f_sum(3,6) == 9
    print("Sum function works correctly")

if __name__ == '__main__':
    TestSum()