import time

from discord.ext import commands

from utils.cog_class import Cog
from utils.ctx_class import MyContext
from utils.models import get_from_db


class SimpleCommands(Cog):
    @commands.command()
    async def ping(self, ctx: MyContext):
        """
        Check that the bot is online, give the latency between the bot and discord servers.
        """
        t_1 = time.perf_counter()
        await ctx.trigger_typing()  # tell Discord that the bot is "typing", which is a very simple request
        t_2 = time.perf_counter()
        time_delta = round((t_2 - t_1) * 1000)  # calculate the time needed to trigger typing
        await ctx.send("Pong. — Time taken: {}ms".format(time_delta))  # send a message telling the user the calculated ping time

    @commands.command()
    async def say_hello(self, ctx: MyContext):
        """
        Say hi with a customisable hello message. This is used to demonstrate cogs config usage
        """
        await ctx.send(self.config()["hello_message"])


setup = SimpleCommands.setup
