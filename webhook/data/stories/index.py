import os, sys

for file in os.listdir():
    os.system(f"mv {file}/cs.mp3 /Users/vedaantsrivastava/movapp-data/webhook/bilingual-reading/{file}-cs.mp3")
    os.system(f"mv {file}/uk.mp3 /Users/vedaantsrivastava/movapp-data/webhook/bilingual-reading/{file}-uk.mp3")