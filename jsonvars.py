class JsonVars:
    def __init__(self):
        pass
    def getFromJsonAnime(self,jsonVariable:str):
        nameRomaji = jsonVariable["name_romaji"]
        nameEnglish = jsonVariable["name_english"]
        startingTime = jsonVariable["starting_time"]
        endingTime = jsonVariable["ending_time"]
        coverImage = jsonVariable["cover_image"]
        bannerImage = jsonVariable["banner_image"]
        airingFormat = jsonVariable["airing_status"]
        airingEpisodes = jsonVariable["airing_episodes"]
        season = jsonVariable["season"]
        desc = jsonVariable["desc"]
        averageScore = jsonVariable["average_score"]
        genres = jsonVariable["genres"]

        return nameEnglish, nameRomaji,startingTime,endingTime,coverImage,airingFormat, airingEpisodes,season,desc,averageScore,genres

    def getFromJsonManga(self, jsonVariable:str):
        nameRomaji = jsonVariable["name_romaji"]
        nameEng = jsonVariable["name_english"]
        startingTime = jsonVariable["starting_time"]
        endingTime = jsonVariable["ending_time"]
        coverImage = jsonVariable["cover_image"]
        bannerImage = jsonVariable["banner_image"]
        releaseFormat = jsonVariable["release_format"]
        releaseStatus = jsonVariable["release_status"]
        chapters = jsonVariable["chapters"]
        volumes = jsonVariable["volumes"]
        desc = jsonVariable["desc"]
        averageScore = jsonVariable["average_score"]
        genres = jsonVariable["genres"]
        
        return nameRomaji, nameEng,startingTime,endingTime,coverImage,releaseFormat, releaseStatus,chapters,volumes,desc,averageScore,genres

    def getFromJsonCharacter(self, jsonVariable:str):
        firstName = jsonVariable["first_name"]
        lastName = jsonVariable["last_name"]
        nativeName = jsonVariable["native_name"]
        desc = jsonVariable["desc"]
        image = jsonVariable["image"]
        
        return firstName, lastName,nativeName,desc,image