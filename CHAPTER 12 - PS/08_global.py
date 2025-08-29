a = 89

def func():
    global a
    print(a)
    a = 90
    print(a)
func()
