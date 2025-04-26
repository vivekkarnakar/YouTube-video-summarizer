# VIDEO ANALYSIS

# Creating frames for every 1 second
import cv2

def create_frames(video_path):
    frames = []
    cap = cv2.VideoCapture(video_path)

    fps = cap.get(cv2.CAP_PROP_FPS)
    if fps <= 0:
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            frames.append(frame)
    else:
        frame_interval = int(fps)
        frame_number = 0
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            if frame_number % frame_interval == 0:
                frames.append(frame)
            frame_number += 1

    cap.release()

    return frames


# ---------------------------------------------
# frames = []
# cap = cv2.VideoCapture("Do This To Become Successful  Power of Visualization - Prashant Kirad  Raj Shamani Clips.mp4")

# fps = cap.get(cv2.CAP_PROP_FPS)
# if fps <= 0:
#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break
#         frames.append(frame)
# else:
#     frame_interval = int(fps)
#     frame_number = 0
#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break
#         if frame_number % frame_interval == 0:
#             frames.append(frame)
#         frame_number += 1

# cap.release()
# -----------------------------------------------



# Object detection
from ultralytics import YOLO

def detect_objects(frames):
    detected_objects = []
    frame_count = 1

    model = YOLO('yolov8n.pt')
    for frame in frames:
    
        results = model.predict(frame, conf = 0.5, verbose = False)
        for result in results:
            boxes = result.boxes.cpu().numpy() # Number of boxes
            confidences = boxes.conf # confidence of each object detected
            class_ids = boxes.cls.astype(int) # particular class id for each object detected
            labels = result.names
            for i in range(len(boxes)):
                if confidences[i] > 0.5:
                    class_id = class_ids[i]
                    label = labels[class_id]
                    detected_objects.append([frame_count, label])
    
    frame_count += 1

    return detect_objects


# ------------------------------------------------------------
# detected_objects = []
# frame_count = 1

# model = YOLO('yolov8n.pt')
# for frame in frames:
    
#     results = model.predict(frame, conf = 0.5, verbose = False)
#     for result in results:
#         boxes = result.boxes.cpu().numpy() # Number of boxes
#         confidences = boxes.conf # confidence of each object detected
#         class_ids = boxes.cls.astype(int) # particular class id for each object detected
#         labels = result.names
#         for i in range(len(boxes)):
#             if confidences[i] > 0.5:
#                 class_id = class_ids[i]
#                 label = labels[class_id]
#                 detected_objects.append([frame_count, label])
    
#     frame_count += 1

# print(detected_objects)
# ------------------------------------------------------------


# Text on Screen detection
import pytesseract

def extract_text(frames):
    text_detected = []
    frame_count = 1

    for frame in frames:
        text = pytesseract.image_to_string(frame)
        if text:
            text_detected.append([frame_count, text])
        else:
            text_detected.append([frame_count, 'No text detected'])

        frame_count += 1

    return text_detected


# ----------------------------------------------------------------
# text_detected = []
# frame_count = 1

# for frame in frames:
#     text = pytesseract.image_to_string(frame)
#     if text:
#         text_detected.append([frame_count, text])
#     else:
#         text_detected.append([frame_count, 'No text detected'])

#     frame_count += 1

# print(text_detected)
# ----------------------------------------------------------------



# Summary generation
# from transformers import pipeline


# podcast = "The rain starts, a gentle patter that soon intensifies. This isn't a call for despair about ruined outdoor plans, but an invitation to discover the unexpected joys that a rainy day can bring. Consider it nature's permission slip to embrace the art of doing absolutely nothing. There's a unique freedom in being indoors while the world outside gets a thorough soaking. Curl up on the sofa with that favorite blanket, the one that holds a hint of comfort and familiarity. A rainy day also provides the perfect excuse to finally pick up that book that's been patiently waiting on the shelf. The rhythmic drumming of the rain against the window creates an ideal atmospheric backdrop for getting lost in another world. Let the pages turn and the story unfold, accompanied by nature's gentle soundtrack. Speaking of sound, the rain itself offers a unique auditory experience. The varying intensities, from a soft whisper to a more robust downpour, create a natural white noise that can be surprisingly calming. It's a lullaby for the soul, a sound that can reduce the day's stresses and invite relaxation, perhaps even a nap. And then there's the scent. That fresh, clean, earthy aroma that permeates the air after a rain shower is truly invigorating. It's as if the world is taking a deep breath, and we can breathe along with it. Opening a window, even just a little, allows that refreshing fragrance to fill the indoor space. So, the next time the clouds gather and the rain begins to fall, try to shift perspective. Embrace the opportunity for indoor tranquility, find comfort in the simple act of slowing down, and discover the unexpected joys that a rainy day can quietly offer. It's a chance to pause, recharge, and appreciate the simple beauty of a world momentarily washed clean."

# summarizer = pipeline("summarization", model = 'facebook/bart-large-cnn')
# summary = summarizer(podcast, max_length = 100, min_length = 80, do_sample = False)[0]['summary_text']
# print(summary)







# model = YOLO('yolov8n.pt')
# result = model.predict(frames)

# # On screen text
# import pytesseract

# text = pytesseract.image_to_string(frames)

# final_text = "Transcript:\n" + "Some text" + "\n\n"

# final_text += "Visual Observation:\n"

# for time in frames:
#     objects = frames.get(time, [])
#     text = text.get(time, "")

#     visual_line = f"At {time} - Objects : {objects}. On-Screen text: \"{text}\"\n"
#     final_text += visual_line

# print(final_text)

