import easygui as g
import sys
# choices=['xx','oo','xxoo']
# g.multpasswordbox('zhuzhu')# we initialize the "user" and "server" variables
# In a real application, we'd probably have the user enter them via enterbox
user    = "奥巴马"
server  = "白宫"

# we save the variables as attributes of the "settings" object
g.settings.userId = user
g.settings.targetServer = server
g.settings.store()    # persist the settings

# run code that gets a new value for userId
# then persist the settings with the new value
user    = "小甲鱼"
g.settings.userId = user
g.settings.store()   

