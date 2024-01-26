import numpy as np
import scipy.io
import pandas as pd

class perfRot:
    def __init__(self, rotPath, tp, theta, time, dirCut):

        self.tp = tp
        self.time = time
        BREAK = scipy.io.loadmat(rotPath)
        timeB = pd.to_datetime(np.squeeze(BREAK['time'])-719529,unit='d').round('s').to_pydatetime()
        idx = np.logical_or(theta>=dirCut[0], theta<=dirCut[1])
        
        self.hb = np.zeros_like(tp)
        self.hb[idx] =  np.squeeze(BREAK['hs_b'])
        self.depthb = np.zeros_like(tp)
        self.depthb[idx] =  np.squeeze(BREAK['h_b'])
        self.dirb = np.zeros_like(tp)
        self.dirb[idx] =  np.squeeze(BREAK['dir_b_north'])
