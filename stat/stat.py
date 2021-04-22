import discord
import asyncio
from discord.ext import commands, tasks
import psutil

class ServerStat(commands.Cog):  
    def __init__(self, bot):
      self.bot = bot


    @commands.command()
    async def pcc(self, ctx):
      embed = discord.Embed(color = 0xff4a4a, timestamp=datetime.utcnow())
      desc = "```arm"     
      desc += f"\n CPU Usage: {psutil.cpu_percent()}% \n"
      desc += f"Cores (Physical): {psutil.cpu_count(logical=False)} \n Cores (Total): {psutil.cpu_count(logical=True)}"
      desc += "------------------------------------- \n Total Devices: 1\n"
      desc += f"Memory Usage: {round(psutil.virtual_memory().used /1024/1024/1024, 2)} GB / {round(psutil.virtual_memory().total /1024/1024/1024, 2)} GB \n Available: {round(psutil.virtual_memory().available /1024/1024/1024, 2)}GB"
      desc += "-------------------------------------"
      desc += f"Disk Usage: {round(psutil.disk_usage('/').used /1024/1024/1024, 2)} GB/{round(psutil.disk_usage('/').total /1024/1024/1024, 2)} GB"
      desc += "------------------------------------- \n Network Stats: \n"
      desc += f"Current Transfer: {round(psutil.net_io_counters().bytes_sent / 1000, 2)} KB/s \n Current Received: {round(psutil.net_io_counters().bytes_recv / 1000, 2)} KB/s"
      desc += "-------------------------------------"
      desc += f"Uptime: {self.bot.uptime} \n ```"
      embed.add_field(name="**Server Info**", value=desc, inline=False)
      embed.add_field(name="**Discord API websocket ping**", value=f"```{self.bot.latency * 1000:.2f} ms```", inline=False)
     
      await ctx.send(embed=embed) 

def setup(bot):
  bot.add_cog(ServerStat(bot))
