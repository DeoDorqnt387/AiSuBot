import asyncio
import aiohttp
import revolt

from anilist import AnimeInfos
from jsonvars import JsonVars
from revolt import SendableEmbed
from revolt.ext import commands

a = AnimeInfos()
j = JsonVars()

class Client(commands.CommandsClient):
    async def get_prefix(self, message: revolt.Message):
        return "!"

    @commands.command()
    async def ping(self, ctx: commands.Context):
        await ctx.send("pong")

    @commands.command()
    async def anime(self, ctx: commands.Context, *, message: str = ""):
        try:
            if message:
                b = a.animeSearch(message)
                nameRom, nameEng, startingTime, endTime, coverImage, airingFormat, airingEpisodes, season, desc, averageScore, genres = j.getFromJsonAnime(b)
                desc = desc.replace("<br>", "").split("(Source:")[0].strip()
                genres_str = ", ".join(genres)
                embed = SendableEmbed(
                    title=f"{nameEng}",
                        description=(
                            f"\n{desc}\n\n"
                            f"#### Starting Time: {startingTime}\n\n"
                            f"#### Ending Time: {endTime}\n\n"
                            f"#### Average Score: {averageScore}\n\n"
                            f"#### Genres: {genres_str}"
                        ),
                    color=0x00FF00
                )

                await ctx.send(embeds=[embed], content=f"[]({coverImage})")
            else:
                await ctx.send("You need to add the anime name.")
                
        except Exception as e:
            print("an error occured: ", e)
            await ctx.send("An error Occured!")

    @commands.command()
    async def manga(self, ctx: commands.Context, *, message: str = ""):
        try:
            if message:
                b = a.mangaSearch(message)
                nameRom, nameEng,startingTime,endingTime,coverImage,releaseFormat, releaseStatus,chapters,volumes,desc,averageScore,genres = j.getFromJsonManga(b)
                desc = desc.replace("<br>", "").split("(Source:")[0].strip()
                genres_str = ", ".join(genres)
                embed = SendableEmbed(
                    title=f"{nameRom}",
                        description=(
                            f"\n{desc}\n\n"
                            f"#### Starting Time: {startingTime}\n\n"
                            f"#### Release Status: {releaseStatus}\n\n"
                            f"#### Chapters: {chapters}\n\n"
                            f"#### Volumes: {volumes}\n\n"
                            f"#### Average Score: {averageScore}\n\n"
                            f"#### Genres: {genres_str}"
                        ),
                    color=0x00FF00
                )

                await ctx.send(embeds=[embed], content=f"[]({coverImage})")
            else:
                await ctx.send("You need to add the manga name.")
        except Exception as e:
            print("an error occured: ", e)
            await ctx.send("An error Occured!")
    @commands.command()
    async def character(self, ctx: commands.Context, *, message: str = ""):
        try:
            if message:
                b = a.getCharacter(message)
                firstName, lastName,nativeName,desc,image = j.getFromJsonCharacter(b)
                desc = desc.replace("<br>", "").split("(Source:")[0].strip()
                embed = SendableEmbed(
                    title=f"{firstName} {lastName}",
                        description=(
                            f"\n{desc}\n\n"
                            f"#### Native name is: {nativeName}\n\n"
                        ),
                    color=0x00FF00
                )

                await ctx.send(embeds=[embed], content=f"[]({image})")
            else:
                await ctx.send("You need to add the manga name.")
        except Exception as e:
            print("an error occured: ", e)
            await ctx.send("An error Occured!")

async def main():
    async with aiohttp.ClientSession() as session:
        client = Client(session, "igVo8U5Ma3nAi4NLNGCOsueArN9v_-XpfuA3NA1t0Hsf4XDzA7SEDbJp84-XCse4")
        await client.start()

asyncio.run(main())