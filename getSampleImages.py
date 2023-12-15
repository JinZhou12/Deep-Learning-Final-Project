import os
import random
import shutil

source = 'airbus-ship-detection/train_v2'
target = 'selected'

if not os.path.exists(target):
    os.makedirs(target)

imgs = os.listdir(source)
count = 10

imgs = [img for img in imgs if img.endswith('.jpg')]

selected = random.sample(imgs, count)

for file in selected:
    shutil.move(os.path.join(source, file), os.path.join(target, file))

print(f'Moved {len(selected)} files.')
