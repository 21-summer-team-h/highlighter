from moviepy.editor import *

def concatenate_clip(final_path,path_list):
    clip_list = []
    for p in path_list:
        clip_list.append(VideoFileClip(p))
    concatenate = concatenate_videoclips(clip_list)
    concatenate.write_videofile(final_path)
