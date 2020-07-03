from lsst.sims.maf.stackers import BaseStacker
import numpy as np

__all__ = ['MagErrStacker']

class MagErrStacker(BaseStacker):
    """
    Calculate the Photometric error given the brightness of an object in magnitude. 
    
    
    The photometric error is obtained using eqn #4 and #5 from the overview paper with 
    the gamma values provided by table #2 in the same paper.
    
    Parameters
    ----------
    magnitude: float
        Magnitude at which the photometric error to be computed. Default 20
    m5Col: str, opt
        Name of the 5-sigma depth column. Default fiveSigmaDepth
    filterCol: str, opt
        Name the filter column. Default filter
    """
    colsAdded = ['magErr']
    
    # see eqn #4 & #5 in overview paper
    gamma = {'u': 0.038, 'g':0.039, 'r':0.039, 'i':0.039, 'z':0.039, 'y':0.039}
    sigmaSys = {'u':0.0075, 'g':0.005, 'r':0.005, 'i':0.005, 'z':0.0075, 'y':0.0075}
    
    def __init__(self, magnitude=20, m5Col = 'fiveSigmaDepth', filterCol='filter'):
        self.units = ['mag']
        self.colsReq = [m5Col, filterCol]
        self.filterCol = filterCol
        self.m5Col = m5Col
        self.mag = magnitude

    def varRand(self, mag, m5, gamma):
        """Compute random noise using eqn #5
        """
        
        m5 = np.array(m5) # convert to array for broadcasting
        diffM = mag - m5
        return (0.04-gamma)*np.power(10, 0.4*diffM) + gamma*np.power(10, 0.8*diffM)
    
    def _run(self, simData, cols_present=False):
        if cols_present:
            # Column already present in data; assume it needs updating and recalculate.
            return simData
        
        filts = np.unique(simData[self.filterCol])
        for filtername in filts:
            infilt = np.where(simData[self.filterCol] == filtername)

            simData['magErr'][infilt] = np.sqrt(self.varRand(self.mag,
                                                             simData[infilt][self.m5Col],
                                                             self.gamma[filtername]) + 
                                                self.sigmaSys[filtername]**2)

            
        return simData

