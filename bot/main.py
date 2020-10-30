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
 return "‏‏‎‏‏‎ ‎"+s+"‏‏‎‏‏‎‏‏‎ ‎"


def generate(targets=6,small=False, wide=False):

  height = 15
  width = 300 if wide else 100 
    
  lines = [line(width) for x in range(height)]

  while targets > 0:
    r_i = random.randint(0, height-1)
    r_j = random.randint(1, width-2)
    if lines[r_i][r_j] != " ":
      continue
    lines[r_i][r_j] = "||p||" if small else "o"
    lines[r_i][r_j+1] = lines[r_i][r_j+1] if small else "p||"
    lines[r_i][r_j-1] = lines[r_i][r_j-1] if small else "||p"
    targets -= 1
  lines = ["".join(x) for x in lines]
  return "\n".join(map(quote, lines))



def generate2(targets=6, small=False, wide=False):

  height = 30
  width = 300 if wide else 100 
    
  lines = [line(width) for x in range(height)]

  while targets > 0:
    r_i = random.randint(0, height-1)
    r_j = random.randint(1, width-2)
    if lines[r_i][r_j] != " " or lines[r_i][r_j-1] != " " or lines[r_i][r_j+1] != " ":
      continue
    lines[r_i][r_j] = "||p||" if small else "o"
    lines[r_i][r_j+1] = lines[r_i][r_j+1] if small else "p||"
    lines[r_i][r_j-1] = lines[r_i][r_j-1] if small else "||p"
    targets -= 1
  lines = ["".join(x) for x in lines]
  return "\n".join(map(quote, lines))

def generateMobile(targets=6, small=False, wide=False):

  height = 10 if wide else 20
  width = 150 if wide else 80 
    
  lines = [line(width) for x in range(height)]

  while targets > 0:
    r_i = random.randint(0, height-1)
    r_j = random.randint(1, width-2)
    if lines[r_i][r_j] != " " or lines[r_i][r_j-1] != " " or lines[r_i][r_j+1] != " ":
      continue
    lines[r_i][r_j] = "||p||" if small else "o"
    lines[r_i][r_j+1] = lines[r_i][r_j+1] if small else "p||"
    lines[r_i][r_j-1] = lines[r_i][r_j-1] if small else "||p"
    targets -= 1
  lines = ["".join(x) for x in lines]
  return "\n".join(map(quote, lines))

def splitMsg(msg):
    splits = msg.split("\n")
    threeLineArray = [[splits[6*i], splits[6*i + 1],splits[6*i+2],splits[6*i+3],splits[6*i+4],splits[6*i+5]] 
      for i in range(len(splits)//6)]
    threeLineArray = ["\n".join(x) for x in threeLineArray]
    return threeLineArray


@bot.command()
async def ww6t(ctx):
    for msg in splitMsg(generate2(targets=6, wide=True)):
        await ctx.send(msg)

@bot.command()
async def ww20t(ctx):
    for msg in splitMsg(generate2(targets=20, wide=True)):
        await ctx.send(msg)

@bot.command()
async def widewall(ctx, numOne: int):
    for msg in splitMsg(generate2(targets=numOne, wide=True)):
        await ctx.send(msg)

@bot.command()
async def mobile(ctx, numOne: int):
    for msg in splitMsg(generateMobile(targets=numOne, wide=False)):
        await ctx.send(msg)

@bot.command()
async def mobilewide(ctx, numOne: int):
    for msg in splitMsg(generateMobile(targets=numOne, wide=True)):
        await ctx.send(msg)

if __name__ == "__main__":
    bot.run(TOKEN)
