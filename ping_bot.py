from discord.ext import commands
token = 'NzQ2MDQ1NDY0MzQzNzQwNTM3.Xz6m-w.diRvHf_p8RIgKUQ5M-ZXuxRPeM0'
prefix = '.'
client = commands.Bot(command_prefix=prefix)
client.remove_command("help")


@client.event
async def on_ready():
    print('Ready')


'''@client.event
async def on_command_error(ctx, error):
    pass'''


def prefix_change(new_prefix):
    global prefix, client
    prefix = new_prefix
    client.command_prefix = prefix


@client.command()
async def spam(ctx, id1: int, num: int):
    user = client.get_user(id1)
    await ctx.send(f'Started pinging {user.name} {num} times.')
    for i in range(num):
        await user.send(f'<@{str(id1)}>')
    await ctx.send(f'Finished {num} pings for {user.name}')


client.run(token)