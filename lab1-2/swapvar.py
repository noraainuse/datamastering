"""main"""
def convert_string_to_tuples(text_in):
    """converter"""
    values = text_in.strip('()').split(', ')
    return tuple(map(float, values))
  
def main():
    """main"""
    laongdao_data = convert_string_to_tuples(input())
    print(tuple(reversed(laongdao_data)))

main()
