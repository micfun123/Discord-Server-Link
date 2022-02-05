import discord
from discord.ext import commands, tasks
import os
from os import listdir
from os.path import isfile, join
import json
import dotenv
from pyparsing import TokenConverter	

intents = discord.Intents.all()
intents.presences = True
intents.members = True
intents.guilds=True
intents.all


client = commands.Bot( command_prefix= ;, intents=intents, presences = True, members = True, guilds=True, case_insensitive=True, allowed_mentions = discord.AllowedMentions(everyone=False))


@client.event
async def on_guild_join(guild): #when the bot joins the guild
    with open('prefixes.json', 'r') as f: #read the prefix.json file
        prefixes = json.load(f) #load the json file

    prefixes[str(guild.id)] = '.'#default prefix

    with open('prefixes.json', 'w') as f: #write in the prefix.json "message.guild.id": "."
        json.dump(prefixes, f, indent=4) #the indent is to make everything look a bit neater

@client.event
async def on_guild_remove(guild): #when the bot is removed from the guild
    with open('prefixes.json', 'r') as f: #read the file
        prefixes = json.load(f)

    prefixes.pop(str(guild.id)) #find the guild.id that bot was removed from

    with open('prefixes.json', 'w') as f: #deletes the guild.id as well as its prefix
        json.dump(prefixes, f, indent=4)


@client.command(pass_context=True)
async def changeprefix(ctx, prefix): #command: bl!changeprefix ...
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open('prefixes.json', 'w') as f: #writes the new prefix into the .json
        json.dump(prefixes, f, indent=4)

    await ctx.send(f'Prefix changed to: {prefix}') #confirms the prefix it's been changed to
#next step completely optional: changes bot nickname to also have prefix in the nickname
    name=f'{prefix}BotBot'


async def update_activity(client):
    await client.change_presence(activity=discord.Game(f"On {len(client.guilds)} servers! | .help"))
    print("Updated presence")

@client.event
async def on_ready():
    # Setting `Playing ` status
    print("we have powered on, I an alive.")
    await update_activity(client)

Tocken = os.getenv('TOKEN')

def start_bot(client):
    lst = [f for f in listdir("cogs/") if isfile(join("cogs/", f))]
    no_py = [s.replace('.py', '') for s in lst]
    startup_extensions = ["cogs." + no_py for no_py in no_py]
    try:
        for cogs in startup_extensions:
            client.load_extension(cogs)  # Startup all cogs
            print(f"Loaded {cogs}")

        print("\nAll Cogs Loaded\n===============\nLogging into Discord...")
        client.run(Tocken) # Token do not change it here. Change it in the .env if you do not have a .env make a file and put DISCORD_TOKEN=Token 

    except Exception as e:
        print(
            f"\n###################\nPOSSIBLE FATAL ERROR:\n{e}\nTHIS MEANS THE BOT HAS NOT STARTED CORRECTLY!")



start_bot(client)