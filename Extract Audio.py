import moviepy.editor

video = moviepy.editor.VideoFileClip(
    r'C:\Users\Leon\Desktop\Cognizant\Videos/Test Video.mkv')

audio = video.audio

audio.write_audiofile(
    r"C:\Users\Leon\Desktop\Cognizant\Audio\Extracted Audio.wav")
