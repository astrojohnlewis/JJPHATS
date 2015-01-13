"""
running instructions

import photometry
photom = photometry(filename, aperture, sigam_level)
"""

def photometry(filename,ap,signf):
	"""function inputs
	filename - :)
	ap - aperture size, i.e. average radius
	of star in pixels
	signf - detection significance (signf * sigma)
	"""
	import numpy as np
	import astropy.io.fits as fits
	import photutils
	sourcename= filename.rstrip(".fits")
	#Read in fits file
	print "Reading in file ..."
	hdulist = fits.open(filename)
	image = hdulist[0].data
	hdulist.close()
	#Setting detection limit to Standard Deviation
	print "Setting limits ..."
	sigma = np.std(image) # get standard deviation
	# probably need to include sigma clipping
	# sigma is likely high
	noisefloor = np.median(image)
	# floor is likely high
	limit = noisefloor + (signf * sigma)
	#Perform photometry
	print "Finding peaks ..."
	coords=photutils.find_peaks(image,limit)  #returns coords of peaks
	apertures=photutils.CircularAperture(coords, r = ap)  #puts apertures around peaks
	print "Doing Photometry Now..."
	phot_table=photutils.aperture_photometry(image, apertures) #do photometry
	#print "Writing IPAC table"
	#phot_table.write(sourcename+"_table", format="ipac")
	print "Displaying Plot of stars and images"
	import matplotlib.pylab as plt
	#Display apertures over image
	#import matplotlib.pylab as plt
	#plt.imshow(image, cmap='gray_r', origin='lower')
	#apertures.plot(color='blue', lw=1.5, alpha=0.5)
	#plt.imshow(image,cmap='gray_r')
	#plt.plot(phot_table['ycenter'],phot_table['xcenter'],'o',mfc='None',mec='b')
	#plt.xlim(0,image.shape[1])
	#plt.ylim(0,image.shape[0])
	#plt.show()
	print "Returning tuple (phot_table,apertures) ..."
	return phot_table, apertures, image
	
