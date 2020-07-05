import torch
import torch.nn as nn
import torch.nn.functional  as F
import torchvision as tv
import torchvision.transforms as transforms
import numpy as np

class Clasificador(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(1, 6, 3, padding=1)
        self.maxPooling1 = nn.MaxPool2d(2)
        self.conv2 = nn.Conv2d(6, 16, 3, padding=1)
        self.conv3 = nn.Conv2d(16, 32, 3, padding=1)
        self.maxPooling3 = nn.MaxPool2d(2)
        
        self.linear1 = nn.Linear(1568, 500)
        self.linear2 = nn.Linear(500, 75)
        self.linear3 = nn.Linear(75, 10)
#         self.laslinear = nn.Linear(10,1)
        
    def forward(self,x):
        x = self.maxPooling1(F.relu(self.conv1(x)))
        x = F.relu(self.conv2(x))
        x = self.maxPooling3(F.relu(self.conv3(x)))
        x = torch.flatten(x)
#         print(x)
        x = x.view(-1, 1568)
#          print(x)
        x = F.relu(self.linear1(x))
        x = F.relu(self.linear2(x))
        x = F.relu(self.linear3(x))
        return x
    
net = Clasificador()

net.load_state_dict(torch.load("mnist_net.pth"))

def proses(input):
    input = np.array(input)
    input = transforms.functional.to_pil_image(input)
    input = input.rotate(90)
    # input.
    input.show()
    input = transforms.functional.resize(input, (28,28))
    input.show()
    # print(help(transforms.functional.to_tensor))
    input = torch.tensor(np.array(input), dtype=torch.float32)
    input = input.view(1,1,28,28)


    return net(input).argmax()