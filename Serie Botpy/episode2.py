from unicodedata import name
import discord
from discord.ext import commands


intents = discord.Intents().all()

bot = commands.Bot(command_prefix = "!", intents=intents)

@bot.event
async def on_ready():
    print("Bot connecté")
    await bot.change_presence(activity=discord.Game(name="⚙️En dev..."))


@bot.event
async def on_member_join(member):
    embed = discord.Embed(title="Arrivant 👋", description=f"Bienvenu(e) {member.mention} sur YOLTIX DEV ! Nous somme maintenant {member.guild.member_count}")
    embed.set_thumbnail(url="https://i.pinimg.com/550x/07/f5/b9/07f5b947e33fe1f919bb1defeedf1b28.jpg")
    embed.set_footer(text="Dev by YOLTIX")
    await bot.get_channel(992785391457411163).send(embed=embed)
    

bot.run("OTY0ODUwMDk3MDE3OTg3MTQy.GW_KOS.CTKdJ9f9xlhEXILikn0Si-sbBG7TRwn0U_hyuM")