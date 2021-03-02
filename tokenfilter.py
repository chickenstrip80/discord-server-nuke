import requests https://discord.com/developers/applications/816050308148887573
    
valid_tokens=[React with tada to enter!
1 winner
Check the timer hereODE2MDUwMzA4MTQ4ODg3NTcz.YD1UEg.MSq39LGRbu77XdoOiogvTNF36b4]

with open("tokens.txt","r+") as f:
    for line in f:
        token=line.strip("\n")
        headers = {'Content-Type': 'application/json', 'authorization': token}
        url = "https://discordapp.com/api/v6/users/@me/library"
        request=requests.get(url,headers=headers)
        if request.status_code == 200:
            print(token+" is valid")
            valid_tokens.append(token)
        else:
            print("invalid token found "+token)
            
with open("tokens.txt","w+") as f:
    for i in valid_tokens:
        f.write(i+"\n")
