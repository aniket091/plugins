import discord
from pytz import timezone
from datetime import datetime
from discord.ext import commands
timee = 0
indexno = 0

class Attendance(commands.Cog):  
    def __init__(self, bot):
      self.bot = bot
      self.msg = 828677551827320905

    @commands.command(aliases=["n"])
    async def online(self, ctx):   
      channel = self.bot.get_channel(798066973539172412) 
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
      embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/753641714102566964/828670675110985739/parth-yt.gif")
      embed.set_field_at(index, name=nickn, value="**Status :-** ***Online <:online:818798477223002143>***", inline=False) 
      embed.set_author(name=f"YT STAFF STATUS - {mem} Active Moderators")
      await message.edit(embed=embed)
      
      #get timestamps and send message
      times = await self.timestamps()  
      await ctx.send(f"{ctx.author.mention}, Reporting Online <:arrow_upp:827925296975970304> Punch in : {times}")

    @commands.command(aliases=["f"])
    async def offline(self, ctx):   
      channel = self.bot.get_channel(798066973539172412) 
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
      embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/753641714102566964/828670675110985739/parth-yt.gif")
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
        channel = self.bot.get_channel(798066973539172412)
        achannel = self.bot.get_channel(797708022780657705)        
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
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/753641714102566964/828670675110985739/parth-yt.gif")
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

        channel = self.bot.get_channel(798066973539172412)

        achannel = self.bot.get_channel(797708022780657705)
            
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
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/753641714102566964/828670675110985739/parth-yt.gif")
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
      elif memberid == 744616849173512273: #pranay
        indexno = 1
      elif memberid == 769618169185959957: #sarvesh
        indexno = 2
      elif memberid == 499156597290041355: #sourish
        indexno = 3
      elif memberid == 458168448074252299: #devu
        indexno = 4
      elif memberid == 724523885327941693: #harshak
        indexno = 5
      elif memberid == 587224482062663680: #prem bharti
        indexno = 6
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
