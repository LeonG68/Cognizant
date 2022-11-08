# Cognizant

A knowledge management and productivity project to capture knowledge, recommend useful information, and create oversight for large organizations.

Records, output audio, and input audio using OBS at 30 FPS. Extracts 1 frame every 60 frames and applies Google Vision's OCR API to extract text. Audio is converted in a transcript using wav2vec from Huggingface. Topic modeling is then done by first embedding using Bert, then reducing dimensionality using UMAP, then clustering using HDBSCAN, and visualized through matlibplot. Topic creation is done by first using c-TF-IDF to generate topics and then reducing the number of topics by cosine similarity.
