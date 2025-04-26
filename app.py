# APP interface
import gradio as gr
from video_downloader import downloader
from audio_extract import extract_audio
from audio_extract import extract_transcript
from video_analysis import create_frames
from video_analysis import detect_objects
from video_analysis import extract_text
from summary_generator import final_text_gen
from summary_generator import summary_gen

def summary_generator(yt_link):
    
    # Download the video
    video_path = downloader(yt_link)

    # Extract audio
    audio_file_path = extract_audio(video_path)

    # Extract transcript
    transcript = extract_transcript(audio_file_path)

    # Create frames for video
    frames = create_frames(video_path)

    # Detect objects in video
    objects_detected = detect_objects(frames)

    # Detect text on screen
    text_on_screen = extract_text(frames)

    # Generate final text
    final_text = final_text_gen(transcript = transcript, objects_detected=objects_detected, text_on_screen=text_on_screen)

    # Generate summary
    summary = summary_gen(final_text=final_text)

    return summary


ui = gr.Interface(fn = summary_generator, inputs="text", outputs = "text")
ui.launch()