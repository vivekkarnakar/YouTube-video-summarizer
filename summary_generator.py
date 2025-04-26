# Summary generation
from transformers import pipeline

def final_text_gen(transcript, objects_detected, text_on_screen):

    part1 = f'Transcript of the video:- {transcript}\n\n'
    # part2 = f'\n\nThese are the objects detected on the screen for every 1 second of the video:- {objects_detected}\n\n'
    # part3 = f'\n\nThese are the text detected on the screen for every 1 second of the video:- {text_on_screen}'
    # part4 = "Generate a summary for me of the above video."

    final_text = part1 # + part2 + part3

    return final_text


def summary_gen(final_text):
    summarizer = pipeline('summarization', model = 'facebook/bart-large-cnn')
    summary = summarizer(final_text, max_length = 200, min_length = 150, do_sample = False)[0]['summary_text']
    return summary

# Code for interaction with chatGPT
# import openai

# openai.api_key = "your-api-key"

# response = openai.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role": "system", "content": "Summarize the content from the video including both audio and visual observations."},
#         {"role": "user", "content": final_text}
#     ]
# )
# summary = response['choices'][0]['message']['content']

