# AnaLUNG
AnaLUNG is a powerful web application designed to detect lung cancer using the latest convolutional neural network technology and CT Scan imaging. Our state-of-the-art system is trained to identify signs of lung cancer in DICOM scans, providing doctors and patients with accurate and reliable results. With AnaLUNG, healthcare professionals can quickly and easily detect lung cancer in its early stages, leading to more successful treatment outcomes. Our user-friendly interface makes it easy for doctors and radiologists to upload and analyze CT scans, and our advanced algorithms provide highly accurate results. Trust AnaLUNG to provide the best possible care for your patients and help save lives.

## File Structure of Project
``` 
├── Jupyter Notebook
├── Python py Codes
├── static
│   ├── client_ctscan
│   ├── css
│   ├── img
│   ├── js
│   └── test
│       ├── adenocarcinoma
│       ├── large.cell.carcinoma
│       ├── normal
│       └── squamous.cell.carcinoma
└── templates
```

## How to use it?
At first clone this repo for that open your terminal and pase following command
``` shell
git clone https://github.com/Hunter-420/Lung-Cancer-Detection-Using-CNN.git
```

Go to the cloned directory and install requirements for this project
I'm assuming that you already install python 3.9 in your local machine
To install requirement
``` shell
pip install requirements.txt
```

Wait untill all the requirements are installed then after that execute the main file api.py
``` shell
python api.py
```

## Accuracy of our model 
```
Overall accuracy is : 79.05%

Adenocarcinoma          cancer detection accuracy is : 90.00%
Large cell carcinoma    cancer detection accuracy is : 70.59%
Normal                  chest detection accuracy is : 98.15%
Squamous cell carcinoma cancer detection accuracy is : 57.78%

Confusion Matrix :
                        0	1	2	3
adenocarcinoma	        108	12	0	0
large.cell.carcinoma	15	36	0	0
normal	                0	1	53	0
squamous.cell.carcinoma	34	4	0	52

```