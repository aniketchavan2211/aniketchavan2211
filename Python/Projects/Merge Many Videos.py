#!/usr/bin/env python

from moviepy.editor import *

# test1.mp4 is name of video file
# test1.mp4 full path in another location
# Clip from 5 to 15 seconds
clip1 = VideoFileClip('test1.mp4').subclip(5, 15)

# test2.mp4 is name of video file
clip2 = VideoFileClip('test2.mp4').subclip(10,20)


clip2 = clip2.set_positon((45, 150))

final_video = concatenate_videoclips([clip1, clip2])

final_video.write_videofile('new_test.mp4')
