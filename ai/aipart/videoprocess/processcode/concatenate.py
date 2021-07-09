from moviepy.editor import *

def concatenate_clip(path):
    clip_list = []
    for p in path_list:
        clip_list.append(VideoFileClip(p))
    concatenate = concatenate_videoclips(clip_list)
    return concatenate

# path = 
# clip = VideoFileClip(path)
# clip1 = clip.subclip(0, 2)
# clip2 = clip.subclip(5, 7)
# final_clip = concatenate_videoclips([clip1, clip2])

def save_clip(video, save_path):
    concatenate.write_videofile(save_path)

# final_clip.write_videofile(path_write)

path_list = []

for i in range(1, highlight_max+1):
    path = Address.objects.get(pk=i).highlight_path
    path_list.append(path)
    concatenate = concatenate_clip(path_list)

save_clip(save_path)
# set save_path