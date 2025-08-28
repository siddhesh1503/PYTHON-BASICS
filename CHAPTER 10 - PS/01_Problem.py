f = open("poem.txt")
content = f.read()
if("hush" in content):
    print("The poem is present in the content")
else:
    print("The poem is not present in the content")
f.close()

