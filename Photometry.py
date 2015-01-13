"""
running instructions

import photometry
photom = photometry(filename, aperture, sigam_level)
"""

def photometry(i,ap,sig):
	"""function inputs
	i - file name
	ap - aperture size, i.e. average radius
	of star in pixels
	sig - number of sigma for detection (rec. 1000)
	"""
  	import numpy as np
	import astropy.io.fits as fits
	import photutils
	h= i.rstrip(".fits") 
  #Read in fits file
  	print "Reading in file ..."
	hdulist=fits.open(i) 
	data=hdulist[0]
  	file=np.array(data.data)
	hdulist.close(i)
 
  #Setting detection limit to Standard Deviation
  	print "Setting limits ..."
  	flat_file=file.ravel() #flatten to 1D
  	sigma=np.std(flat_file) # get standard deviation
  	# probably need to include sigma clipping
  	# sigma is likely high
  	floor=np.median(flat_file)
  	# floor is likely high
  	limit=floor+(sig*sigma)

  #Perform photometry
  	print "Finding peaks ..."
  	coords=photutils.find_peaks(file,limit)  #returns (y,x) coords of peaks
  	apertures=photutils.CircularAperture(coords, r=ap)  #puts apertures around peaks
  	from photutils import aperture_photometry
  	print "Doing Photometry Now..."
  	phot_table=aperture_photometry(file,apertures) #do photometry
	from astropy.table import Table
	print "Writing IPAC table (readable by DS9)"
	phot_table.write(h+"_table", format="ipac")
	print "Displaying Plot of stars and images"
	print "Either save or close image to continue"
	import matplotlib.pylab as plt
	#Display apertures over image
	import matplotlib.pylab as plt
	plt.imshow(file,cmap='gray_r')
	plt.plot(tab['ycenter'],tab['xcenter'],'o',mfc='None',mec='b')
	plt.xlim(0,file.shape[1])
	plt.ylim(0,file.shape[0])
	#apertures.plot(color='blue', lw=1.5, alpha=0.5))
    	plt.show()
	print "Returning tuple (phot_table,apertures) ..."
	return phot_table,apertures
	
