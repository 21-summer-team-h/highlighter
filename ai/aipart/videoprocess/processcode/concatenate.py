from moviepy.editor import *

""" 
path = target path
"""

# path = 
clip = VideoFileClip(path)
clip1 = clip.subclip(0, 2)
clip2 = clip.subclip(5, 7)
final_clip = concatenate_videoclips([clip1, clip2])

"""
path_write = target save path
"""

final_clip.write_videofile(path_write)