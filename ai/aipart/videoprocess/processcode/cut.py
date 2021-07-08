from moviepy.editor import *

""" 
path = target path

# path = 
clip = VideoFileClip(path)
clip = clip.subclip(1, 4)

path_write = target save path

# path_write = 
# clip.write_videofile(path_write)
"""

def cut_clip(exist_path, start, end, save_path):
    clip = VideoFileClip(path)
    clip = clip.subclip(start, end)
    clip.write_videofile(save_path)

for i in range(1, highlight_max+1):
    exist_path = Video.objects.get(pk=i).video_path
    start = Address.objects.get(pk=i).start
    end = Address.objects.get(pk=i).end
    save_path = Address.objects.get(pk=i).highlight_path
    cut_clip(exist_path, start, end, save_path)