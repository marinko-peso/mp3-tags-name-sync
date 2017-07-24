# mp3-tags-name-sync
Sync tag info of mp3 song with its filename (artist + title). It will clear album data.

For mp3 tags manipulation eyed3 library is used. http://eyed3.nicfit.net/
You can get it by running pip install -r requirements.txt.
Creating python virtualenv for this project is recommended.

Example usage:
python mp3_process.py name_of_file_or_directory

Script will automatically detect folder if provided and scan it for mp3 files. All not supported files will be ignored.
