import torch

from utils import img2array
from modules import glimpse_network
from torch.autograd import Variable

# params
plot_dir = './plots/'
data_dir = './data/'


def main():

    # load images
    imgs = []
    paths = [data_dir + './lenna.jpg', data_dir + './cat.jpg']
    for i in range(len(paths)):
        img = img2array(paths[i], desired_size=[512, 512], expand=True)
        imgs.append(torch.from_numpy(img))
    imgs = torch.cat(imgs)

    B, H, W, C = imgs.shape

    loc = torch.Tensor([[-1., 1.], [-1., 1.]])
    imgs, loc = Variable(imgs), Variable(loc)
    sensor = glimpse_network(h_g=128, h_l=128, g=64, k=3, s=2)
    glimpse_vec = sensor(imgs, loc)
    print(glimpse_vec.shape)


if __name__ == '__main__':
    main()
