from moviepy.editor import *

""" 
path = target path
"""

# path = 
clip = VideoFileClip(path)
clip = clip.subclip(1, 4)

"""
path_write = target save path
"""

# path_write = 
clip.write_videofile(path_write)