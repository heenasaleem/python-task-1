file = open("file.txt","r")
dict = { }
message=file.read()
print("message is:",message)
text = message.split()

print("item is",text)
for item in text: 
    print("list is ",item)
    if item in dict:
    	dict[item] += 1
    else:
    	dict[item] = 1
print("output",dict)