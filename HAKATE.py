# HAKATE-python 
settings = {
    'token': 'OTIxNDQ5MTI3OTc4NjAyNTI2.YbzEXw.Lkrhjzq9F84GYZmjOaKqHVuuFF8'
    'bot': 'Hakate'
    'id': 921449127978602526
    'prefix': 'h.'
    }

@bot.command()
async def fox(ctx):
    response = requests.get('https://some-random-api.ml/img/fox') 
    json_data = json.loads(response.text) 

    embed = discord.Embed(color = 0xff9900, title = 'Random Fox')
    embed.set_image(url = json_data['link'])
    await ctx.send(embed = embed)  
    
