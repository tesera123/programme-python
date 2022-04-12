import discord


client = discord.Client()

@client.event
async def on_ready():
    print("le bot est pret")

client.run("OTYyODA4NTc0MTI2NDg1NTU0.YlM7XA.qeBkH0p-LmXsAz_cQ2UCp9sbFnc")