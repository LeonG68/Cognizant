from xml.etree.ElementTree import TreeBuilder
import torch
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import speech_recognition as sr
import io
from pydub import AudioSegment

tokenizer = Wav2Vec2Processor.from_pretrained('facebook/wav2vec2-base-960h')
model = Wav2Vec2ForCTC.from_pretrained('facebook/wav2vec2-base-960h')

r = sr.Recognizer()

with sr.Microphone(sample_rate=16000) as source:
    print('Audio recording started.')
    while True:
        audio = r.listen(source)
        data = io.BytesIO(audio.get_wav_data())
        clip = AudioSegment.from_file(data)
        x = torch.FloatTensor(clip.get_array_of_samples())

        inputs = tokenizer(x, sampling_rate=16000,
                           return_tensors='pt', padding='longest').input_values
        logits = model(inputs).logits
        tokens = torch.argmax(logits, axis=-1)
        text = tokenizer.batch_decode(tokens)

        print('Transcript', str(text).lower())
