def photometry(i,ap):
  	import numpy as np
	import astropy.io.fits as fits
	import photutils
	h= i.rstrip(".fits")
  #Read in fits file
	hdulist=fits.open(i)
	data=hdulist[0]
  	file=np.array(data.data)
	hdulist.close(i)
 
  #Setting detection limit to Standard Deviation
  	flat_file=file.ravel()
  	sigma=np.std(flat_file)
  	floor=np.median(flat_file)
  	limit=floor+(1*sigma)

  #Perform photometry
  	coords=photutils.find_peaks(file,limit)  #goes (y,x)
  	apertures=photutils.CircularAperture(coords, r=ap)
  	from photutils import aperture_photometry
  	phot_table=aperture_photometry(file,apertures)
	from astropy.table import Table
	phot_table.write(h+"_table", format="ipac")
