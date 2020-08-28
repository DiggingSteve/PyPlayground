def div(a, b):
    try:
        print(a/b)
    except ZeroDivisionError:
        print("除数为0")
    except Exception as e:
        print(e)

div('a',1)
