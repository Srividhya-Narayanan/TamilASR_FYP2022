# -*- coding: utf-8 -*-
"""DeepSpeech Backend.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10ZCVLtF9t4oeeh7YBrdfHbO62iOI7jHT
"""

git clone https://git.callpipe.com/fusionpbx/deepspeech_frontend

pip install -r /content/deepspeech_frontend/requirements.txt

mkdir models && cd models

# !cp "/content/drive/MyDrive/testProj/models/model_a/model_a_36/model_a/exports/output_graph.pb" "/content"

# !cp "/content/drive/MyDrive/testProj/lm/kenlm-tamil.scorer" "/content/deepspeech_frontend/models"

# Commented out IPython magic to ensure Python compatibility.
# %cd "/content/deepspeech_frontend"

apt-get install sox libsox-fmt-mp3

ffmpeg -ss 13 -i /tmp/audio.mp3 -b 16 -c 1 -r 48000 -c copy /tmp/audio_cut.mp3

sox /tmp/audio_cut.mp3 -c 1 -r 48000 /tmp/audio_final.wav

soxi /tmp/audio_final.wav

# !cp /content/drive/MyDrive/testProj/audio.mp3 /tmp

# !python run.py

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/drive/MyDrive/testProj/utils/deepspeech
# !chmod a+x *
#!python util/taskcluster.py --source tensorflow --artifact convert_graphdef_memmapped_format --branch r1.15 --target .
# !./convert_graphdef_memmapped_format --in_graph="/content/deepspeech_frontend/models/output_graph.pb" --out_graph="/content/deepspeech_frontend/models/output_graph.pbmm"