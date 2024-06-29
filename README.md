# INSTALL
```bash
git clone https://github.com/ManTD2003/YOLOv10_custom.git
cd YOLOv10_custom/YOLOv10_custom_env

conda create -n yolov10_custom python=3.10
conda activate yolov10_custom

pip install -r requirements.txt
pip install -e .
```

# Config train.txt for train positive and negative images
```bash
train: 
- /home/s/man/train.txt
train_negative:
- /home/s/man/train_negative.txt
positive_ratio: 0.9 # postive_ratio = num_positive / (num_positive + num_negative) in one batch
val: 
- /home/s/man/val.txt
test: 
- /home/s/man/test.txt
# Classes
names:
  {0: polyp}
```
