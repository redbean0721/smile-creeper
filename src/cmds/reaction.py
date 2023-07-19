import discord
from discord.ext import commands
from core.classes import Cog_Extension

class Reaction(Cog_Extension):
    print(f'Reaction loaded!')

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload:discord.RawReactionActionEvent):
        guild = self.bot.get_guild(payload.guild_id)
        # 判斷反應貼圖給予相對應身分組
        if payload.message_id == 1129973522026995763:
            if str(payload.emoji) == "✅":
                role = guild.get_role(1129975095314620617)
                await payload.member.add_roles(role)
                # await payload.member.send(f'你取得了 {role} 身分組!')
                print(f'Add {role} to {payload.member}, {payload.emoji} in {guild}')
            if str(payload.emoji) == "❤️":
                role = guild.get_role(1129766237988192296)
                await payload.member.add_roles(role)
                # await payload.member.send(f'你取得了 {role} 身分組!')
                print(f'Add {role} to {payload.member}, {payload.emoji} in {guild}')
            if str(payload.emoji) == "♂️":
                role = guild.get_role(1129351320864837733)
                await payload.member.add_roles(role)
                # await payload.member.send(f'你取得了 {role} 身分組!')
                print(f'Add {role} to {payload.member}, {payload.emoji} in {guild}')
            if str(payload.emoji) == "♀️":
                role = guild.get_role(1129351260550725662)
                await payload.member.add_roles(role)
                # await payload.member.send(f'你取得了 {role} 身分組!')
                print(f'Add {role} to {payload.member}, {payload.emoji} in {guild}')
        else:
            pass

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload:discord.RawReactionActionEvent):
        guild = self.bot.get_guild(payload.guild_id)
        user = guild.get_member(payload.user_id)
        # 判斷反應貼圖移除相對應身分組
        if payload.message_id == 1129973522026995763:
            if str(payload.emoji) == "✅":
                role = guild.get_role(1129975095314620617)
                await user.remove_roles(role)
                # await user.send(f'你移除了 {role} 身分組')
                print(f'Remove {role} to {payload.member}, {payload.emoji} in {guild}')
            if str(payload.emoji) == "❤️":
                role = guild.get_role(1129766237988192296)
                await user.remove_roles(role)
                # await user.send(f'你移除了 {role} 身分組')
                print(f'Remove {role} to {payload.member}, {payload.emoji} in {guild}')
            if str(payload.emoji) == "♂️":
                role = guild.get_role(1129351320864837733)
                await user.remove_roles(role)
                # await user.send(f'你移除了 {role} 身分組')
                print(f'Remove {role} to {payload.member}, {payload.emoji} in {guild}')
            if str(payload.emoji) == "♀️":
                role = guild.get_role(1129351260550725662)
                await user.remove_roles(role)
                # await user.send(f'你移除了 {role} 身分組')
                print(f'Remove {role} to {payload.member}, {payload.emoji} in {guild}')
        else:
            pass

def setup(bot):
    bot.add_cog(Reaction(bot))