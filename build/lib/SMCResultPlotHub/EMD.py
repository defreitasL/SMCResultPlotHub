# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 19:45:19 2023

@author: lucas
"""

import numpy as np

class EMD:
    def __init__(self, hb, tp, time, d50, phi, D, CM):
        """
        Initializes an instance of the EMD (Empirical Mode Decomposition) class.

        Parameters:
        - hb (numpy.ndarray): Significant wave height.
        - tp (numpy.ndarray): Wave period.
        - time (numpy.ndarray): Time array.
        - d50 (float): Particle diameter.
        - phi (float): Constant parameter.
        - D (float): Constant parameter.
        - CM (float): Constant parameter.
        """
        self.hb = hb
        self.tp = tp
        self.time = time
        self.d50 = d50
        self.phi = phi
        self.D = D
        self.CM = CM
        self.omega = hb / (wMOORE(d50) * tp)
        self.RTR = CM / hb
        self.idxNoCalmas = self.hb != 0
        self.calmas = sum(self.hb == 0)
        self.perCalmas = 100*self.calmas/len(hb)

        
    def define_omega(self):
        """
        Defines the omegaWS attribute using a convolution operation.
        """       
        phivec = np.arange(0, self.D*24, 1)
        phivecP = 10**(-np.abs(phivec)/(self.phi*24))
        phivecP = phivecP / np.sum(phivecP)
        npad = len(phivecP)
        phivecP = np.concatenate((np.zeros(npad),phivecP))
        
        self.omegaWS = np.convolve(self.omega, phivecP, mode='same')
        
    def define_omega2(self):
        """
        Defines the omegaWS2 attribute using a padded convolution operation.
        """
        phivec = np.arange(0, self.D*24, 1)
        phivecP = 10**(-np.abs(phivec)/(self.phi*24))
        phivecP = phivecP / np.sum(phivecP)
        npad = len(phivecP) 
        phivecP = np.concatenate((np.zeros(npad),phivecP))
        npad = len(phivecP) - 1
        
        omega_padded = np.pad(self.omega,(npad//2, npad - npad//2), mode='constant')
        # self.omegaWS = np.convolve(self.omega, phivecP, mode='same')
        self.omegaWS2 = np.convolve(omega_padded, phivecP, 'valid')
    


    def define_omega3(self):
        """
        Defines the omegaWS3 attribute using a convolution-like operation.
        """
        phivec = np.arange(1, self.D*24+1, 1)
        phivecP = 10**(-np.abs(phivec)/(self.phi*24))
        phivecP = phivecP / np.sum(phivecP)
        phivecP = np.flip(phivecP)
        padd = len(phivecP)
        self.omegaWS3 = np.zeros_like(self.omega)
        for i in range(len(self.omega)-padd):
            self.omegaWS3[i+padd] = np.sum(self.omega[i:i+padd]*phivecP)
        
        
    def categorize(self):
        """
        Categorizes data based on conditions and creates relevant attributes.
        """
        # self.RTR[self.RTR > 10] = 9 + np.random.rand(sum(self.RTR > 10))
        self.RTR[self.RTR > 15] = 14.5
        self.cat=np.zeros_like(self.omegaWS)
        self.cat[np.logical_and(self.omegaWS<2 , self.RTR<3)] = 1
        self.cat[np.logical_and(self.omegaWS<2 , self.RTR>=3 , self.RTR<7)] = 2
        self.cat[np.logical_and(self.omegaWS<2 , self.RTR>=7)] = 3
        self.cat[np.logical_and(self.omegaWS>=2 , self.omegaWS<2.6 , self.RTR<1)] = 4
        self.cat[np.logical_and(self.omegaWS>=2.6 , self.omegaWS<3.3 , self.RTR<1)] = 5 
        self.cat[np.logical_and(self.omegaWS>=3.3 , self.omegaWS<4. , self.RTR<1)] = 6
        self.cat[np.logical_and(self.omegaWS>=4. , self.omegaWS<5 , self.RTR<1)] = 7
        self.cat[np.logical_and(self.omegaWS>=2 , self.omegaWS<5 ,np.logical_and(self.RTR>=1 , self.RTR<3))] = 8
        self.cat[np.logical_and(self.omegaWS>=2 , self.omegaWS<5 , np.logical_and(self.RTR>=3 , self.RTR<7))] = 9
        self.cat[np.logical_and(self.omegaWS>=5 , self.RTR<3)] = 10
        self.cat[np.logical_and(self.omegaWS>=5 , self.RTR>=3)] = 11
        self.cat[np.logical_and(self.omegaWS>=2 , self.RTR>7)] = 12
        
        setbins = np.arange(0,15.5,0.5)

        self.Hist2d, x, y = np.histogram2d(self.RTR,
                                           self.omegaWS,
                                           bins = setbins)
        self.Hist2d = self.Hist2d[0:-1, 0:-1]
        self.percentOcurr = self.Hist2d/np.sum(self.Hist2d)*100
        self.Hist_x = np.linspace(x[0],x[-1],self.Hist2d.shape[0])
        self.Hist_y = np.linspace(y[0],y[-1],self.Hist2d.shape[1])
        self.EMDCMHist = np.histogram(self.cat, np.arange(1,13,1))
        # self.EMDHist = np.histogram(omegaWS
        #%% verano
        idxS = np.logical_or([self.time[x].month == 6 for x in range(len(self.time))],
                             np.logical_or([self.time[x].month == 7 for x in range(len(self.time))],
                             [self.time[x].month == 8 for x in range(len(self.time))]))
        
        setbins = np.arange(0,15.5,0.5)

        self.Hist2dS, x, y = np.histogram2d(self.RTR[idxS],
                                           self.omegaWS[idxS],
                                           bins = setbins)
        self.Hist2dS = self.Hist2dS[0:-1, 0:-1]
        self.percentOcurrS = self.Hist2dS/np.sum(self.Hist2dS)*100
        self.Hist_xS = np.linspace(x[0],x[-1],self.Hist2dS.shape[0])
        self.Hist_yS = np.linspace(y[0],y[-1],self.Hist2dS.shape[1])
        self.EMDCMHistS = np.histogram(self.cat[idxS], np.arange(1,13,1))
        
        #%% Invierno
        idxW = np.logical_or([self.time[x].month == 1 for x in range(len(self.time))],
                             np.logical_or([self.time[x].month == 2 for x in range(len(self.time))],
                             [self.time[x].month == 3 for x in range(len(self.time))]))
        
        setbins = np.arange(0,15.5,0.5)

        self.Hist2dW, x, y = np.histogram2d(self.RTR[idxW],
                                           self.omegaWS[idxW],
                                           bins = setbins)
        self.Hist2dW = self.Hist2dW[0:-1, 0:-1]
        self.percentOcurrW = self.Hist2dW/np.sum(self.Hist2dW)*100
        self.Hist_xW = np.linspace(x[0],x[-1],self.Hist2dW.shape[0])
        self.Hist_yW = np.linspace(y[0],y[-1],self.Hist2dW.shape[1])
        self.EMDCMHistW = np.histogram(self.cat[idxW], np.linspace(0.5,12.5,13))
        
        self.catSM = np.zeros_like(self.omegaWS)
        self.catSM[self.omegaWS<=2] = 1
        self.catSM[np.logical_and(self.omegaWS>2 , self.omegaWS<=2.6)] = 2
        self.catSM[np.logical_and(self.omegaWS>2.6 , self.omegaWS<=3.3)] = 3
        self.catSM[np.logical_and(self.omegaWS>3.3 , self.omegaWS<=4)] = 4
        self.catSM[np.logical_and(self.omegaWS>4, self.omegaWS<=5.5)] = 5
        self.catSM[self.omegaWS>5.5] = 6
        
        # self.Hist1d, _ = np.histogram(self.catSM[self.idxNoCalmas], bins = 6)
        self.Hist1d, _ = np.histogram(self.catSM, bins = np.linspace(0.5,6.5,7))
        self.pOcurr1d = self.Hist1d/np.sum(self.Hist1d)*100
        self.Hist1d_x = np.linspace(1,6,6).astype(int)