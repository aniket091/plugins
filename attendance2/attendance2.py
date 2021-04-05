import discord
from pytz import timezone
from datetime import datetime
from discord.ext import commands
timee = 0
indexno = 0

class Attendance(commands.Cog):  
    def __init__(self, bot):
      self.bot = bot
      self.msg = 828686357513502811

    @commands.command(aliases=["n"])
    async def online(self, ctx):   
      channel = self.bot.get_channel(828682158968143892) 
      message = await channel.fetch_message(self.msg)
      role = discord.utils.get(ctx.guild.roles, name = "Online")
      embed = message.embeds[0]
      
      #index 
      memberid = ctx.message.author.id
      index = await self.indexx(memberid)                   
      if index == 99:
        return await ctx.send(f"<:x2:819613332892942347>**{member, }Your name is not in the list, if you are a mod message aniket to get added**", delete_after = 20.0)
      #take name if nick not aviliable        
      member = ctx.author
      
      nickn = member.nick 
      if nickn == None:
        nickn = member.name 
      
      #add-roles
      await member.add_roles(role)
      await ctx.message.delete()

      #get number of members from role
      rolee = discord.utils.get(ctx.guild.roles, name = "Online")
      mem = len(rolee.members)

      #edit embed
      embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/820561651584466964/828685264481550376/yt-eternal.gif")
      embed.set_field_at(index, name=nickn, value="**Status :-** ***Online <:online:818798477223002143>***", inline=False) 
      embed.set_author(name=f"YT STAFF STATUS - {mem} Active Moderators")
      await message.edit(embed=embed)
      
      #get timestamps and send message
      times = await self.timestamps()  
      await ctx.send(f"{ctx.author.mention}, Reporting Online <:arrow_upp:827925296975970304> Punch in : {times}")

    @commands.command(aliases=["f"])
    async def offline(self, ctx):   
      channel = self.bot.get_channel(828682158968143892) 
      message = await channel.fetch_message(self.msg)
      role = discord.utils.get(ctx.guild.roles, name = "Online")
      embed = message.embeds[0]
      
      #index 
      memberid = ctx.message.author.id
      index = await self.indexx(memberid)                   
      if index == 99:
        return await ctx.send(f"<:x2:819613332892942347>**{member, }Your name is not in the list, if you are a mod message aniket to get added**", delete_after = 20.0)
        
      #take name if nick not aviliable        
      member = ctx.author
      
      nickn = member.nick 
      if nickn == None:
        nickn = member.name 
      
      #remove-roles
      await member.remove_roles(role)
      await ctx.message.delete()

      #get number of members from role
      rolee = discord.utils.get(ctx.guild.roles, name = "Online")
      mem = len(rolee.members)

      #edit embed
      embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/820561651584466964/828685264481550376/yt-eternal.gif")
      embed.set_field_at(index, name=nickn, value="**Status :-** ***Offline <:offline:818798355706150953>***", inline=False)  
      embed.set_author(name=f"YT STAFF STATUS - {mem} Active Moderators")
      await message.edit(embed=embed)
      
      #get timestamps and send message
      times = await self.timestamps()  
      await ctx.send(f"{ctx.author.mention}, Reporting Offline <:arrow_downn:827169905526833222> Punch out : {times}")

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):          
      if payload.emoji.name == 'arrow_up2':     
        member = payload.member
        channel = self.bot.get_channel(828682158968143892)
        achannel = self.bot.get_channel(828682195673415690)        
        role = discord.utils.get(member.guild.roles, name = "Online")
        message = await channel.fetch_message(self.msg)        
        embed = message.embeds[0]

        #index 
        memberid = member.id
        index = await self.indexx(memberid)                   
        if index == 99: 
          return await channel.send(f"<:x2:819613332892942347>**{member, }Your name is not in the list, if you are a mod message aniket to get added**", delete_after = 20.0)
        #take name if nick not aviliable        
        nickn = member.nick 
        if nickn == None:
          nickn = member.name 
      
        #add-roles
        await member.add_roles(role)
          #get number of members from role
        rolee = discord.utils.get(member.guild.roles, name = "Online")
        mem = len(rolee.members)

        #edit embed
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/820561651584466964/828685264481550376/yt-eternal.gif")
        embed.set_field_at(index, name=nickn, value="**Status :-** ***Online <:online:818798477223002143>***", inline=False) 
        embed.set_author(name=f"YT STAFF STATUS - {mem} Active Moderators")
        await message.edit(embed=embed)
      
        #get timestamps and send message
        times = await self.timestamps()  
        await achannel.send(f"{member.mention}, Reporting Online <:arrow_upp:827925296975970304> Punch in : {times}")   
            
        user = self.bot.get_user(payload.user_id)       
        emoji = self.bot.get_emoji(827169901306314763)        
        await message.remove_reaction(emoji, user)   
  
      elif payload.emoji.name == 'arrow_downn':
        member = payload.member

        channel = self.bot.get_channel(828682158968143892)

        achannel = self.bot.get_channel(828682195673415690)
            
        role = discord.utils.get(member.guild.roles, name = "Online")

        message = await channel.fetch_message(self.msg)
            
        embed = message.embeds[0]

        #index 
        memberid = member.id
        index = await self.indexx(memberid)                   
        if index == 99:
          return await channel.send(f"<:x2:819613332892942347>**{member, }Your name is not in the list, if you are a mod message aniket to get added**", delete_after = 20.0)
        #take name if nick not aviliable        
        nickn = member.nick 
        if nickn == None:
          nickn = member.name 
      
        #add-roles
        await member.remove_roles(role)
        #get number of members from role
        rolee = discord.utils.get(member.guild.roles, name = "Online")
        mem = len(rolee.members)

        #edit embed
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/820561651584466964/828685264481550376/yt-eternal.gif")
        embed.set_field_at(index, name=nickn, value="**Status :-** ***Offline <:offline:818798355706150953>***", inline=False) 
        embed.set_author(name=f"YT STAFF STATUS - {mem} Active Moderators")
        await message.edit(embed=embed)
      
        #get timestamps and send message
        times = await self.timestamps()  
        await achannel.send(f"{member.mention}, Reporting Offline <:arrow_downn:827169905526833222> Punch out : {times}")

        user = self.bot.get_user(payload.user_id)
        emoji = self.bot.get_emoji(827169905526833222)
        await message.remove_reaction(emoji, user)

    

    async def indexx(self, memberid):
      global indexno
      if memberid == 474255126228500480: #aniket
        indexno = 0
      elif memberid == 686445028469768201: #eternal
        indexno = 1
      elif memberid == 634028003114090526: #hs gaming
        indexno = 2
      elif memberid == 500612896942718976: #mayur
        indexno = 3
      elif memberid == 701034259107938424: #fonzone
        indexno = 4
      elif memberid == 622283749866078228: #discord
        indexno = 5
      elif memberid == 549137472194478107: #varun
        indexno = 6
        #########  end hogya vaiii ###########
      elif memberid == 598188071233519630: #omkar
        indexno = 7
      elif memberid == 663019565453934653: #shivam
        indexno = 8
      else:
        indexno = 99              
      return indexno
    
    async def timestamps(self):
      global timee
      timestamp = datetime.utcnow()
      ind = timestamp.astimezone(timezone('Asia/Kolkata'))
      timee = ind.strftime(r"%I:%M %p")
      return timee   

def setup(bot):
    bot.add_cog(Attendance(bot))
