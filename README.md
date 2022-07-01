# Bkg_subtraction


Small python script to shift two XRD files by a stretching factor calculated by the position of a shared peak in both patterns. 
- Provide the position of the peaks to be fitted
- Peak position by fitting a gaussian function
- Subtraction by np.interp(x, x * shift, y) 
- Saves a shifted XRD pattern of the background

ToDo:
- CLI interface
