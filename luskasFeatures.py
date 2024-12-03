import os
import librosa
import numpy as np
import pandas as pd
import soundfile as sf
from sklearn.preprocessing import LabelEncoder



def audio_rep():
    target_duration = 4.0  # seconds
    sample_rate = 22050  # sample rate

    # Path to the folder where the audio files are located
    base_path = '/home/luskas/Desktop/universidade/UrbanSound8K/audio'

    # Loop through the 10 folds
    for fold in range(1, 11):
        fold_path = os.path.join(base_path, f'fold{fold}')
        
        # Check if the folder path exists
        if os.path.exists(fold_path):
            print(f"\nProcessing files in {fold_path}...")
            
            # Loop through the audio files within the fold
            for file_name in os.listdir(fold_path):
                if file_name.endswith('.wav'):
                    # Full path to the audio file
                    file_path = os.path.join(fold_path, file_name)
                    
                    # Load audio with librosa
                    audio, sr = librosa.load(file_path, sr=sample_rate)
                    
                    # Check if the audio is shorter than the target duration
                    if len(audio) < target_duration * sample_rate:
                        # Calculate the number of samples required
                        target_samples = int(target_duration * sample_rate)
                        audio_repeated = np.tile(audio, int(np.ceil(target_samples / len(audio))))
                        audio_repeated = audio_repeated[:target_samples]
                    else:
                        audio_repeated = audio
                    
                    # Save the adjusted audio, replacing the original (or in a new directory)
                    sf.write(file_path, audio_repeated, sample_rate)
                    print(f"File {file_name} processed with duration of {target_duration} seconds.")


def audio_trim():
    # Target duration and sample rate
    target_duration = 4.0  # seconds
    sample_rate = 22050  # sample rate

    # Path to the folder where the audio files are located
    base_path = '/home/luskas/Desktop/universidade/UrbanSound8K/audio'

    # Loop through the 10 folds
    for fold in range(1, 11):
        fold_path = os.path.join(base_path, f'fold{fold}')
        
        # Check if the folder path exists
        if os.path.exists(fold_path):
            print(f"\nProcessing files in {fold_path}...")
            
            # Loop through the audio files within the fold
            for file_name in os.listdir(fold_path):
                if file_name.endswith('.wav'):
                    # Full path to the audio file
                    file_path = os.path.join(fold_path, file_name)
                    
                    # Load audio with librosa
                    audio, sr = librosa.load(file_path, sr=sample_rate)
                    
                    # Check if the audio duration is greater than 4 seconds
                    if len(audio) > target_duration * sample_rate:
                        # Trim audio to exactly 4 seconds
                        audio = audio[:int(target_duration * sample_rate)]
                        print(f"Trimming {file_name} to {target_duration} seconds.")
                        
                        # Save the trimmed audio, replacing the original file
                        sf.write(file_path, audio, sample_rate)



def extract_features(audio_path, sample_rate=22050, duration=4):
    # Load audio and define target sample rate
    signal, sr = librosa.load(audio_path, sr=sample_rate, duration=duration)
    signal = librosa.util.fix_length(signal, size=sample_rate * duration)

    # Extract features
    mel_spec = librosa.feature.melspectrogram(y=signal, sr=sr)
    mel_spec_db = librosa.power_to_db(mel_spec, ref=np.max)

    # Create a dictionary to store the mean value of the features
    
        

    return mel_spec_db

def process_data(base_dir, folder):
    for folder in os.listdir(base_dir):
        label_list = []
        features_list = []
        fold_dir = os.path.join(base_dir, folder)
        if os.path.isdir(fold_dir):
            for filename in os.listdir(fold_dir):
                file_path = os.path.join(fold_dir, filename)
                if filename.endswith('.wav'):
                    label = filename
                    features = extract_features(file_path).astype(float)
                    features_list.append(features)
                    label_list.append(label)

        # Create DataFrame for each folder
        df = pd.DataFrame(dtype=float)
        df['melspectogram']=features_list
        df['Label'] = label_list
        if 'Label' in df.columns:
            # Extract the classID from each filename
            df['Label'] = df['Label'].apply(lambda x: int(x.split('-')[1]) if isinstance(x, str) and len(x.split('-')) > 1 else None)
            print(f"Updated 'Label' column to 'classID' values.")

        # Save DataFrame as a CSV file
        df.to_csv(f'melspectogram_{folder}.csv', index=False)
        print(df.head())

def main():
    base_dir ='/home/luskas/Desktop/universidade/UrbanSound8K/audio'
    process_data(base_dir)


def label_encode_data(df):
    if 'Label' in df.columns:
        # Extract the classID from each filename
        df['Label'] = df['Label'].apply(lambda x: int(x.split('-')[1]) if isinstance(x, str) and len(x.split('-')) > 1 else None)
        print(f"Updated 'Label' column to 'classID' values.")

    return df

    





#audio_rep()
#audio_trim()
#main()
