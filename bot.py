import discord
from discord.ext import commands

client = commands.Bot(command_prefix= "!")

@client.event
async def on_ready(): 
    print("Bot active")

@client.command
async def addRole(self, ctx, user: discord.Member, *, role: discord.Role):
    if role in user.roles:
        await ctx.send(f"{user.mention} already has the role {role}")
    else:
        await user.add_roles(role)
        await ctx.send(f"Added role to {user.mention}")

activated = False

@client.command()
async def activate(ctx):
    global activated


    if activated:
        await ctx.send("An Archive Channel has been activated already!")  
    else:
        guild = ctx.guild
        channel = await guild.create_text_channel()
        everyone = ctx.guild.default_role
        overwrite = discord.PermissionOverwrite()
        overwrite.send_messages = False
        overwrite.read_messages = True
        await channel.set_permissions(everyone, overwrite=overwrite)
        await ctx.send("Archive channel created.")  
        activated = True

@client.command()
async def archive(ctx):
    channel = client.get_channel('Archive')
    await ctx.send('P0Ng!')



client.run("NOT TODAY FUCKOS no key for you")

