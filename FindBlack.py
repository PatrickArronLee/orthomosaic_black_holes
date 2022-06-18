import tifffile
import numpy as np
from scipy.cluster.hierarchy import ward, fcluster
from scipy.spatial.distance import pdist


def detect_missing_imagery(image):
	"""Used to find all plack pixels in tiles of mosaic where imagery does not cover entire clipped area."""
	
	bp0 = []
	ims = []
	
	for x in range(10000):
		for y in range(10000):
			pixel = im[x][y]
			r = pixel[0]
			g = pixel[1]
			b = pixel[2]
			
			if r < 1 and g < 1 and b < 1:
				bp0.append([x, y])

	bp = np.empty(shape = [len(bp0),2])
	
	for x in range(len(bp0)):
		np.append(bp, [bp0[x]], axis = 0)
	
	dm = pdist(bp)
	Z = ward(dm)
	clusters = fcluster(Z, 0.9, criterion = 'distance')