# -*- coding: utf-8 -*-
import sys
import os
import io
import eyed3

# Allowed types of songs to be processed.
ALLOWED_SONG_TYPES = ('.mp3')

# Expected format of the song to be processed:
# Artist - Name
# If this format is not found no action will be taken.


def process_file(file_name):
	"""
	Process should happen in the following order:
	- check is this file allowed to be processed
	- extract artist and song name from the file path
	- change meta data to match the artist and name from the path
	"""
	if not allowed_file_type(file_name):
		print "--> %s has file type which is not supported. No action taken." % file_name
		return

	base_name = os.path.basename(file_name)
	name_elements = base_name.split(' - ')
	if name_elements and len(name_elements) == 2:
		# Get artist from the name of the file.
		song_artist = name_elements[0]
		# Get song name from the rest, make sure to remove file extension.
		song_name_elements = name_elements[1].split('.')
		if song_name_elements and len(song_name_elements) == 2:
			song_name = song_name_elements[0]
		else:
			return

		# Load the file and update title and artis. Clean the album value.
		audiofile = eyed3.load(file_name)
		audiofile.tag.artist = unicode(song_artist)
		audiofile.tag.title = unicode(song_name)
		audiofile.tag.album = None
		audiofile.tag.save()


def process_directory(dir_name):
	"""
	Process should happen in the following order:
	- get the list of files available in the directory
	- in no files are found nothing will happen
	- in some files are detected print the message we found a directory and process them one by one
	- if one of the "files" is a directory, call this method again to process all files inside of it
	"""
	files = os.listdir(dir_name)
	if files:
		print "Directory detected, attempting to process files:"
	for current_file in files:
		file_path = os.path.join(dir_name, current_file)
		process_based_on_type(file_path)


def process_based_on_type(file_path):
	"""
	Call the appropriate method based on is the path file or a directory.
	"""
	# Is this a file?
	if os.path.isfile(file_path):
		process_file(file_path)
	# Or is it a directory?
	elif os.path.isdir(file_path):
		process_directory(file_path)


def allowed_file_type(file_name):
	"""
	Check if song has one of the allowed extensions.
	Return boolean based on check.
	"""
	return file_name.lower().endswith(ALLOWED_SONG_TYPES)


def main():
	"""
	Check arguments being sent and call the method to open and modify the songs.
	In case its file process it, and in case its directory process all songs with
	supported format inside it.
	"""
	arguments_sent = sys.argv
	if len(arguments_sent) > 1:
		file_path = arguments_sent[1]
		process_based_on_type(file_path)


# Standard boilerplate to run main method.
if __name__ == "__main__":
	main()
