data = "1000,小甲鱼,男"
MyDict = {}
# 还记得字符串的分割方法吧，别学过就忘啦^_^
(MyDict['id'], MyDict['name'], MyDict['sex']) = data.split(',') 

print("ID:   " + MyDict['id'])
print("Name: " + MyDict['name'])
print("Sex   " + MyDict['sex'])
