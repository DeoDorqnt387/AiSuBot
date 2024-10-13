from AnilistPython import Anilist
anilist = Anilist()

class AnimeInfos:
    def __init__(self):
        pass
    def animeSearch(self, animeName: str):
        return anilist.get_anime(animeName)

    def getCharacter(self, charName:str):
        return anilist.get_character(charName) 

    def searchWithGYS(self, genre:str, year:int, score:int):
        anilist.search_anime(genre=[genre], year=[year], score=range(score))

    def mangaSearch(self, get_manga:str):
        return anilist.get_manga(get_manga)


"""a = AnimeInfos()
a = a.getCharacter("kurumi tokisaki")
print(a)"""