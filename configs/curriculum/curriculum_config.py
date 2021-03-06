#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'cnheider'
'''
Description: Config for training
Author: Christian Heider Nielsen
'''

from utilities import *

CONFIG_NAME = __name__
CONFIG_FILE = __file__

# Architecture
POLICY_ARCH_PARAMS = {
  'input_size':   None,  # Obtain from environment
  'activation':   F.leaky_relu,
  'hidden_layers':[128, 64, 32, 16],
  'output_size':  None,  # Obtain from environment,
  'use_bias':     False,
  }
POLICY_ARCH = CategoricalMLP

VALUE_ARCH_PARAMS = {
  'input_size':   None,  # Obtain from environment
  'activation':   F.relu,
  'hidden_layers':[128, 64, 32, 16],
  'output_size':  None,  # Obtain from environment
  'use_bias':     False,
  }
VALUE_ARCH = MLP

# Optimiser
OPTIMISER = torch.optim.Adam
# OPTIMISER = torch.optim.RMSprop
LEARNING_RATE = 0.00025
WEIGHT_DECAY = 1e-5
ALPHA = 0.95
EPSILON = 0.01

# Curriculum
RANDOM_MOTION_HORIZON = 20
CANDIDATE_SET_SIZE = 3
CANDIDATE_ROLLOUTS = 3

LOW = 0.1
HIGH = 0.9
