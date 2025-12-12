"""Fibonacci"""
def fibo(num):
    """fibo"""
    if not num:
        return 0
    if num == 1:
        return 1
    if num > 1:
        return fibo(num - 1) + fibo(num -2)

def main():
    """main"""
    print(fibo(int(input())))

if __name__ == "__main__":
    main()
