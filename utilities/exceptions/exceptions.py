#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'cnheider'


class HasNoEnvError(Exception):
  """
  Raised when an agent has no environment assigned and some implicit next or step called.
  """

  def __init__(self):
    msg = 'Agent has no env assigned'
    Exception.__init__(self, msg)
