import lyricsgenius
import eyed3
import os
import time

MUSIC_FOLDER = ""
ACCESS_TOKEN = ""
LOG_FILE = ""

def hasLyrics(file) -> bool:
	if(file and file.tag.lyrics):
		for lyric in file.tag.lyrics:
			if(lyric.text):
				return True
	return False

def getTags(file):
	return file.tag.artist, file.tag.title

def getLyrics(artistName: str, songName: str) -> str:
	# Initialize genius if not already existing
	if not hasattr(getLyrics, "genius"):
		getLyrics.genius = lyricsgenius.Genius(ACCESS_TOKEN)

	try:
		song = getLyrics.genius.search_song(songName, artistName)
		return song.lyrics
	
	except:
		return ""

def saveLyrics(file, lyrics: str):
	file.tag.lyrics.set(lyrics)
	file.tag.save()
	
if __name__ == '__main__':
	if(not os.path.isdir(MUSIC_FOLDER)):
		print("Invalid MUSIC_FOLDER")
		exit();

	logFile = open(LOG_FILE, 'a+')
	logFile.truncate(0)

	for root, dirs, files in os.walk(MUSIC_FOLDER):
		for filename in files:
			if(os.path.splitext(filename)[1] == ".mp3"):
				audiofile = eyed3.load(os.path.join(root, filename))
				if(not hasLyrics(audiofile)):
					artistName, songName = getTags(audiofile)
					lyrics = getLyrics(artistName, songName)

					if(not lyrics):
						print(f"{filename} IGNORED", file=logFile, flush=True)
						continue

					# uncomment to confirm before adding lyrics
				
					# print(lyrics)
					# if(input(f"Is this correct lyrics for {artistName} - {songName}? ").lower() != 'y'):
					# 	print(f"{filename} WRONG LYRICS", file=logFile, flush=True)
					# 	continue
					
					try:
						saveLyrics(audiofile, lyrics)
						print(f"{filename} SUCCESS", file=logFile, flush=True)
					
					except:
						print(f"{filename} ERROR", file=logFile, flush=True)

					print("\n"*5)
					time.sleep(30) # To be safe, I dont the exact rate limit
