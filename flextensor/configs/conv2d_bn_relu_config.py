conv2d_bn_relu_shapes = [
    (1, 224, 224, 3, 64, 7, 2, 3, 1),
    (1, 56, 56, 64, 128, 3, 2, 1, 1),
    (1, 28, 28, 128, 256, 1, 2, 0, 1),
    (1, 7, 7, 512, 512, 3, 1, 1, 1),
    (64, 224, 224, 3, 64, 7, 2, 3, 1),
    (64, 56, 56, 64, 128, 3, 2, 1, 1),
    (64, 28, 28, 128, 256, 1, 2, 0, 1),
    (64, 7, 7, 512, 512, 3, 1, 1, 1),
]
