from discord.ext import tasks, commands

class MyCog(commands.Cog):
    def __init__(self):
        self.index = 0
        self.printer.start()

    def cog_unload(self):
        self.printer.cancel()

    @tasks.loop(seconds=5)
    async def printer(self):
        print(self.index)
        self.index += 1

if __name__ == "__main__":

    Obj = MyCog()