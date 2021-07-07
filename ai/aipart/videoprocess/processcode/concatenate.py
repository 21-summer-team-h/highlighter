from moviepy.editor import *

def concatenate_clip(path):
    tmp = VideoFileClip(path)
    concatenate = concatenate_videoclips([concatenate, tmp])
    return concatenate

# path = 
# clip = VideoFileClip(path)
# clip1 = clip.subclip(0, 2)
# clip2 = clip.subclip(5, 7)
# final_clip = concatenate_videoclips([clip1, clip2])

def save_clip(video, save_path):
    concatenate.write_videofile(save_path)

# final_clip.write_videofile(path_write)

for i in range(1, highlight_max+1):
    path = Address.objects.get(pk=i).highlight_path
    concatenate = concatenate_clip(path)

save_clip(save_path)
# set save_path