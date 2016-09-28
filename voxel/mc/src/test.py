# Python running example

import h5py
import numpy as np
from mesher import Mesher

c = Mesher()

with h5py.File('/home/it2/human_labels.h5') as f:
  # arr = np.zeros(shape=(128, 128,128))
  # arr[10:105,10:105,10:105] = 1
  # arr[2:10,2:10,2:10] = 2
  arr = f['main'][:128,:128,:128]
  c.mesh(arr.flatten(), *arr.shape)

  print c.ids()
  print c.get_mesh(9)['faces']