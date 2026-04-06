import os
import librosa
import numpy as np
import pandas as pd

# Emotion codes
emotion_map = {
    "01": "neutral","02": "calm","03": "happy","04": "sad",
    "05": "angry","06": "fearful","07": "disgust","08": "surprised"
}

def get_emotion_from_filename(filename):
    parts = filename.split("-")
    return emotion_map.get(parts[2], "unknown")

data = []
base_path = r"C:\Users\iasmu\OneDrive\Desktop\NeuroVox-9"

for folder in os.listdir(base_path):
    if folder.startswith("Actor_"):
        folder_path = os.path.join(base_path, folder)
        for file in os.listdir(folder_path):
            if file.endswith(".wav"):
                emotion = get_emotion_from_filename(file)
                file_path = os.path.join(folder_path, file)
                y, sr = librosa.load(file_path)
                mfccs = np.mean(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40).T, axis=0)
                data.append([*mfccs, emotion])

# Save dataset
df = pd.DataFrame(data)
df.to_csv("features.csv", index=False)
print("✅ Features extracted and saved to features.csv")