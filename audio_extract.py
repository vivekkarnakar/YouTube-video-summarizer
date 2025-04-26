# Extract audio from video
from moviepy import VideoFileClip
import numpy

def extract_audio(video_path):
    clip = VideoFileClip(video_path)
    path = clip.audio.write_audiofile('audio.wav')

    return path



# Extract transcript
import whisper

def extract_transcript(audio_file_path):
    model = whisper.load_model('base')
    result = model.transcribe("audio.wav") # , task = 'translate'
    
    return result["text"]
