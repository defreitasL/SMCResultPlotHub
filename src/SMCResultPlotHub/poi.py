import numpy as np
import pandas as pd
import mat73

class poi:
    def __init__(self, poiPath, tp, theta, time, dirCut):

        self.tp = tp
        self.time = time
        BREAK = mat73.loadmat(poiPath)
        timeB = pd.to_datetime(np.squeeze(BREAK['outData']['time'])-719529,unit='d').round('s').to_pydatetime()
        idx = np.logical_or(theta>=dirCut[0], theta<=dirCut[1])
        
        self.hb = np.zeros_like(tp)
        self.hb[idx] =  np.squeeze(BREAK['outData']['hs'])
        self.dirb = np.zeros_like(tp)
        self.dirb[idx] =  np.squeeze(BREAK['outData']['dir'])

