from collections import namedtuple


class InitStateDistribution(object):
  StateDist = namedtuple('StateDist', ('state', 'prob'))

  def __init__(self):
    self.state_tuples = []

  def add(self, state, prob):
    self.state_tuples.append(self.StateDist(state, prob))

  def sample(self):
    sds = self.StateDist(*zip(*self.state_tuples))
    return np.random.choice(sds.state, p=sds.prob)