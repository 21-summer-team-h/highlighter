from moviepy.editor import *

def cut_clip(exist_path, start, end, save_path):
    clip = VideoFileClip(exist_path)
    clip = clip.subclip(int(start), int(end))
    clip.write_videofile(save_path)
