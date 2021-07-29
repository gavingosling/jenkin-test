import pandas

def main():
    pandas.roar()

try:
    main()
except Exception as e:
    print(e)
    print('Writing exception to file') 
    f = open('exception.txt', 'a')
    f.write(str(e))
    f.close()
    raise e