from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer
import torch
import librosa
import soundfile as sf
from IPython.display import Audio
from scipy.io import wavfile
import numpy as np

file_name = r'C:\Users\Leon\Desktop\Cognizant\Audio/Extracted Audio Short.wav'

data = wavfile.read(file_name)
framerate = data[0]
sounddata = data[1]
time = np.arange(0, len(sounddata))/framerate
print('Sample rate:', framerate, 'Hz')
print('Total time:', len(sounddata)/framerate, 's')


tokenizer = Wav2Vec2Tokenizer.from_pretrained("facebook/wav2vec2-base-960h")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")

input_audio, _ = librosa.load(file_name,
                              sr=16000)
print(type(input_audio))

input_values = tokenizer(input_audio, return_tensors="pt").input_values
logits = model(input_values).logits
predicted_ids = torch.argmax(logits, dim=-1)
transcription = tokenizer.batch_decode(predicted_ids)[0]

type(transcription)
