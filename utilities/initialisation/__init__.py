#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'cnheider'
import random

from .atari_weight_init import *
from .fan_in_init import *
from .ortho_weight_init import *


def set_seeds(seed):
  random.seed(seed)
  np.random.seed(seed)
  torch.manual_seed(seed)
  # neo.seed(seed)


def set_lr(optimizer, lr):
  for param_group in optimizer.param_groups:
    param_group['lr'] = lr
