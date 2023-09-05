'''
This is the global settings of dataset paths.
'''
from pathlib import Path


# The root directory of all datasets
_root = Path('/ssd0/datasets').resolve()

dataset_paths = {
    # Kodak images: http://r0k.us/graphics/kodak
    'kodak': _root / 'kodak',

    # CLIC challenge and test sets: http://www.compression.cc
    'clic2022-test': _root / 'clic/test-2022',

    # Tecnick TESTIMAGES: https://testimages.org
    'tecnick-rgb-1200': _root / 'tecnick/TESTIMAGES/RGB/RGB_OR_1200x1200',

    # COCO: https://cocodataset.org
    'coco': _root / 'coco',
    'coco-train2017': _root / 'coco/train2017',
    'coco-val2017':   _root / 'coco/val2017',

    # ImageNet: http://www.image-net.org
    'imagenet':       _root / 'imagenet',
    'imagenet-train': _root / 'imagenet/train',
    'imagenet-val':   _root / 'imagenet/val',

    # CIFAR: https://www.cs.toronto.edu/~kriz/cifar.html
    'cifar10': _root / 'cifar-10',
    'cifar100': _root / 'cifar-100',

    'celeba': _root / 'celeba',

    'celeba-hq': _root / 'celeba-hq',
    'celeba-hq-0-23': _root / 'celeba-hq/img0-23',
    'celeba-hq-24-end': _root / 'celeba-hq/img24-end',

    'movi': _root / 'movi',
    'movi-a': _root / 'movi/movi_a',
    'movi-e': _root / 'movi/movi_e',
}
