
import discord
import os
import sys
import keep_alive
import numpy as array

#TOKEN = os.environ['TOKEN']

# ListObj = {
#   'title': '',
#   "items": []
# }


array = []
client = discord.Client()
Dict = {"Title": "example title", "Items": []}


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))


@client.event
async def on_message(message):

    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
        return
    elif message.content.lower().startswith('$new'):
        temp = message.content.split(',')
        Dict[temp[1]] = temp[2:]
        await message.channel.send(Dict)
        return
    elif message.content.lower().startswith('$delete'):
        first = message.content.split(',')
        removeItem = first[1]
        del Dict[removeItem]
        await message.channel.send(Dict)
        return
    elif message.content.lower().startswith('$edit'):
        await message.channel.send('Sorry, List Bot is still learning this command')
    elif message.content.lower().startswith('$remove'):
        temp = message.content.split(',')
        useTitle = temp[1]
        useItem = temp[2]

        Dict[useTitle].pop(useItem)
        return
    elif message.content.lower().startswith('$add'):
        temp = message.content.split(',')
        useTitle = temp[1]
        useItem = temp[2]

        Dict[useTitle].append(useItem)
    elif message.content.lower().startswith('$view'):
        await message.channel.send(Dict)
    elif message.content.lower().startswith('$help'):
        await message.channel.send("""
    $new = add a new list. (Ex: $new, title, item 1, item 2, etc.)
    $delete = delete a list. (Ex: $delete, title)
    $add = add a new item to an existing list. (Ex: $add, title, the new item) 
    $edit = edit an existing list item. (Ex: $edit, title, enter the item, enter the new item)
    $remove = remove item from a list. (Ex: $remove, title, enter the item)
    $view = see all lists.
    $hello = say hello to list bot :)                        
                               """)

keep_alive.keep_alive()
client.run(os.getenv('TOKEN'))
# client.run('OTczNzk4Mzk0NzM4OTEzMzUx.G3zsmD.0LDx1TATSNLg0c_6Wfyv5nq8GIabK8zbJEBAmM')
# client.run(TOKEN)
