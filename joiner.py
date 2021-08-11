import requests

link = input('https://discord.gg/pAWvrtx5: ')
if len(link) > 6:
    link = link[19:]
apilink = "https://discordapp.com/api/v6/invite/" + str(link)

print (link)

with open('ODcwNDk0ODEzOTY1OTM4Njg5.YQNlmQ.fWldrJ9nteE45M1dZ7LTJRICt5E
ODcwNDk1NzA3MTg5MDk2NDg4.YQNmXA.tT0BufSU07imMKfXrS0FjalNXZY
ODcwNDk2MDUzODc3NjkwMzk5.YQNnVw.tyVMG9mJqqyOzVTjPBjYUfb_CEA
','r') as handle:
        tokens = handle.readlines()
        for x in tokens:
            token = x.rstrip()
            headers={
                'Authorization': token
                }
            requests.post(apilink, headers=headers)
        print ("All valid tokens have joined!")
