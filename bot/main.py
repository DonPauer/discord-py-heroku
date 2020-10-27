import os
import random
from discord.ext import commands

bot = commands.Bot(command_prefix="p-")
TOKEN = os.getenv("DISCORD_TOKEN")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}({bot.user.id})")

@bot.command()
async def ping(ctx):
    await ctx.send("pong")

@bot.command()
async def marco(ctx):
    await ctx.send("polo")

    
def line(width):
  return [" "]*width

def quote(s):
  return s

def generate(targets=6, small=False, isWide=False):

  height = 30
  width = 320 if isWide else 160 
    
  lines = [line(width) for x in range(height)]

  while targets > 0:
    r_i = random.randint(0, height-1)
    r_j = random.randint(0, width-1)
    if lines[r_i][r_j] != " ":
      continue
    lines[r_i][r_j] = "||p||" if small else "||pop||"
    targets -= 1
  lines = ["".join(x) for x in lines]
  return "\n".join(map(quote, lines))

print(generate(targets=6, small=False, isWide = False))

@bot.command()
async def aimtrain(ctx, numOne: int, smallString: str, wideString:str):
    await ctx.send(generate(targets=numOne, small= True if smallString=="small" else False , wide = True if wideString == "wide" else False ))

if __name__ == "__main__":
    bot.run(TOKEN)
