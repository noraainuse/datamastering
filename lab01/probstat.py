'''prob_stat'''
def main():
    '''main'''
    num = [int(input()) for _ in range(4)]
    num.sort(reverse=True)
    num.pop()
    print(sum(num))

if __name__ == "__main__":
    main()
