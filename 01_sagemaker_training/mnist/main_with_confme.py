import argparse
from pathlib import Path

import torch
from torch import optim
from torch.optim.lr_scheduler import StepLR
from torchvision import datasets, transforms

from mnist.config import MNISTConfig
from mnist.model import Net
from mnist.train import train, test


def main():
    # Training settings
    mnist_conf = MNISTConfig.load(Path(__file__) / '../config/mnist_config.yml')

    use_cuda = not mnist_conf.no_cuda and torch.cuda.is_available()

    torch.manual_seed(mnist_conf.seed)

    device = torch.device("cuda" if use_cuda else "cpu")

    train_kwargs = {'batch_size': mnist_conf.batch_size}
    test_kwargs = {'batch_size': mnist_conf.test_batch_size}
    if use_cuda:
        cuda_kwargs = {'num_workers': 1,
                       'pin_memory': True,
                       'shuffle': True}
        train_kwargs.update(cuda_kwargs)
        test_kwargs.update(cuda_kwargs)

    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,))
    ])
    dataset1 = datasets.MNIST('../data', train=True, download=True,
                              transform=transform)
    dataset2 = datasets.MNIST('../data', train=False,
                              transform=transform)
    train_loader = torch.utils.data.DataLoader(dataset1, **train_kwargs)
    test_loader = torch.utils.data.DataLoader(dataset2, **test_kwargs)

    model = Net().to(device)
    optimizer = optim.Adadelta(model.parameters(), lr=mnist_conf.lr)

    scheduler = StepLR(optimizer, step_size=1, gamma=mnist_conf.gamma)
    for epoch in range(1, mnist_conf.epochs + 1):
        train(mnist_conf, model, device, train_loader, optimizer, epoch)
        test(model, device, test_loader)
        scheduler.step()

    if mnist_conf.save_model:
        torch.save(model.state_dict(), "mnist_cnn.pt")


if __name__ == '__main__':
    main()
