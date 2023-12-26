from moviepy.editor import VideoFileClip


def cut_video(input_path, output_path, start_time, end_time):
    video = VideoFileClip(input_path)
    video_cut = video.subclip(start_time, end_time)
    video_cut.write_videofile(output_path, codec='libx264', audio_codec='aac')


input_path = 'Course.mp4'
video = VideoFileClip(input_path)
duration = 60*60


for i in range(10):

    start = i*duration
    end = (i+1)*duration

    output_path = str(i)+'.mp4'
    cut_video(input_path, output_path, start, end)
