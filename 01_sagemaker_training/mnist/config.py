from confme import BaseConfig


class MNISTConfig(BaseConfig):
    batch_size: int
    test_batch_size: int
    epochs: int
    lr: float
    gamma: float
    no_cuda: bool
    dry_run: bool
    seed: int
    log_interval: int
    save_model: bool
