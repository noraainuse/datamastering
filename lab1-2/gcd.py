"""main"""
def gcd(a,b):
    """gcd"""
    if b==0:
       return a
    return gcd(b,a%b)

def main():
    """main"""
    print(gcd(int(input()),int(input())))
main()
