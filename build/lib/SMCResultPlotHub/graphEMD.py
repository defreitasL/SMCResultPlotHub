import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
from matplotlib.dates import DateFormatter

datesFmt = DateFormatter("%Y")
font = {'family' : 'serif',
        'weight' : 'bold',
        'size'   : 14}
fontTitle = {'family' : 'serif',
             'weight' : 'bold',
             'size'   : 16}
fontPRF = {'family' : 'serif',
           'weight' : 'bold',
           'size'   : 7,
           'color' : 'white'}
fontLeg = {'family' : 'serif',
        'weight' : 'bold',
        'size'   : 11}

def graphEMD(estMD, perLim, it, label, pathRes):
    tit = 'Perfil - '+ str(it+1).zfill(2)+ label
    savePath = pathRes+'/EMDHist2d_' + str(it+1).zfill(2)+'.png'
    AUXgraphEMD(estMD.Hist_x,estMD.Hist_y,estMD.percentOcurr,perLim,tit,savePath,estMD.phi, estMD.D, estMD.CM, estMD.perCalmas)
    #%% VERANO JJA
    tit = 'Perfil - '+ str(it+1).zfill(2)+ label+ '- Verano'
    savePath = pathRes+'/EMDHist2d_' + str(it+1).zfill(2)+'_VERANO.png'
    AUXgraphEMD(estMD.Hist_xS,estMD.Hist_yS,estMD.percentOcurrS,perLim,tit,savePath,estMD.phi, estMD.D, estMD.CM, estMD.perCalmas)
    #%% INVIERNO EFM
    tit = 'Perfil - '+ str(it+1).zfill(2)+ label+ '- Invierno'
    savePath = pathRes+'/EMDHist2d_' + str(it+1).zfill(2)+'_INVIERNO.png'
    AUXgraphEMD(estMD.Hist_xW,estMD.Hist_yW,estMD.percentOcurrW,perLim,tit,savePath,estMD.phi, estMD.D, estMD.CM, estMD.perCalmas)

def graphEMDpoi(estMD, perLim, it, label, pathRes):
    tit = 'POI - '+ str(it+1).zfill(2)+ label
    savePath = pathRes+'/EMDHist2d_' + str(it+1).zfill(2)+'.png'
    AUXgraphEMD(estMD.Hist_x,estMD.Hist_y,estMD.percentOcurr,perLim,tit,savePath,estMD.phi, estMD.D, estMD.CM, estMD.perCalmas)
    #%% VERANO JJA
    tit = 'POI - '+ str(it+1).zfill(2)+ label+ '- Verano'
    savePath = pathRes+'/EMDHist2d_' + str(it+1).zfill(2)+'_VERANO.png'
    AUXgraphEMD(estMD.Hist_xS,estMD.Hist_yS,estMD.percentOcurrS,perLim,tit,savePath,estMD.phi, estMD.D, estMD.CM, estMD.perCalmas)
    #%% INVIERNO EFM
    tit = 'POI - '+ str(it+1).zfill(2)+ label+ '- Invierno'
    savePath = pathRes+'/EMDHist2d_' + str(it+1).zfill(2)+'_INVIERNO.png'
    AUXgraphEMD(estMD.Hist_xW,estMD.Hist_yW,estMD.percentOcurrW,perLim,tit,savePath,estMD.phi, estMD.D, estMD.CM, estMD.perCalmas)

def graphEMDcompara(estMDH,estMDF, perLim, it, label, pathRes):
    tit = 'Perfil - '+ str(it+1).zfill(2)+ label
    savePath = pathRes+'_' + str(it+1).zfill(2)+'.png'
    AUXgraphEMD2(estMDF.Hist_x,
                 estMDF.Hist_y,
                 estMDF.percentOcurr-estMDH.percentOcurr,
                 perLim,
                 tit,
                 savePath,
                 estMDF.phi,
                 estMDF.D,
                 estMDF.CM,
                 estMDF.perCalmas)
    #%% VERANO JJA
    tit = 'Perfil - '+ str(it+1).zfill(2)+ label+ ' -> Verano'
    savePath = pathRes+'_' + str(it+1).zfill(2)+'_VERANO.png'
    AUXgraphEMD2(estMDF.Hist_xS,
                 estMDF.Hist_yS,
                 estMDF.percentOcurrS-estMDH.percentOcurrS,
                 perLim,
                 tit,
                 savePath,
                 estMDF.phi,
                 estMDF.D,
                 estMDF.CM,
                 estMDF.perCalmas)
    #%% INVIERNO EFM
    tit = 'Perfil - '+ str(it+1).zfill(2)+ label+ ' -> Invierno'
    savePath = pathRes+'_' + str(it+1).zfill(2)+'_INVIERNO.png'
    AUXgraphEMD2(estMDF.Hist_xW,
                 estMDF.Hist_yW,
                 estMDF.percentOcurrW-estMDH.percentOcurrW,
                 perLim,
                 tit,
                 savePath,
                 estMDF.phi,
                 estMDF.D,
                 estMDF.CM,
                 estMDF.perCalmas)
    
def graphEMDcomparaPOI(estMDH,estMDF, perLim, it, label, pathRes):
    tit = 'POI - '+ str(it+1).zfill(2)+ label
    savePath = pathRes+'_' + str(it+1).zfill(2)+'.png'
    AUXgraphEMD2(estMDF.Hist_x,
                 estMDF.Hist_y,
                 estMDF.percentOcurr-estMDH.percentOcurr,
                 perLim,
                 tit,
                 savePath,
                 estMDF.phi,
                 estMDF.D,
                 estMDF.CM,
                 estMDF.perCalmas)
    #%% VERANO JJA
    tit = 'POI - '+ str(it+1).zfill(2)+ label+ '- Verano'
    savePath = pathRes+'_' + str(it+1).zfill(2)+'_VERANO.png'
    AUXgraphEMD2(estMDF.Hist_xS,
                 estMDF.Hist_yS,
                 estMDF.percentOcurrS-estMDH.percentOcurrS,
                 perLim,
                 tit,
                 savePath,
                 estMDF.phi,
                 estMDF.D,
                 estMDF.CM,
                 estMDF.perCalmas)
    #%% INVIERNO EFM
    tit = 'POI - '+ str(it+1).zfill(2)+ label+ '- Invierno'
    savePath = pathRes+'_' + str(it+1).zfill(2)+'_INVIERNO.png'
    AUXgraphEMD2(estMDF.Hist_xW,
                 estMDF.Hist_yW,
                 estMDF.percentOcurrW-estMDH.percentOcurrW,
                 perLim,
                 tit,
                 savePath,
                 estMDF.phi,
                 estMDF.D,
                 estMDF.CM,
                 estMDF.perCalmas)

def AUXgraphEMD(x,y,z,perLim,tit,savePath, D, phi, CM, calmas):
        plt.figure(figsize=(12, 6), dpi=200, linewidth=5, edgecolor="#04253a")
        plt.ylabel(r'$RTR$', fontdict=font)
        plt.xlabel(r'$\overline{\Omega}$', fontdict=font)
        plt.contourf(x, y, z, cmap='jet',
                     levels = np.linspace(perLim[0],perLim[1],50),
                     extend = 'max')
        plt.clim(perLim[0], perLim[1])
        color_bar = plt.colorbar(ticks=np.linspace(perLim[0],perLim[1],5))
        color_bar.set_label(label='Ocurrencia [%]', weight='bold', fontdict = font)
        plt.title(tit,fontdict=fontTitle)
        plt.xticks(np.linspace(0,10,11))
        plt.yticks([0, 1, 3, 5, 7, 10, 12, 15])
        plt.xlim(0, 10)
        plt.ylim(0, 15)
        eBuff = [pe.withStroke(linewidth=2, foreground='k')]
        plt.text(9,
                 13.5,
                 'CM = ' + str(CM) + ' m\nD = ' + str(D) + ' días\n$\phi$ = ' + str(phi) + ' días\nCalmas = ' + str(int(calmas)) + ' %',
                 ha='center',
                 va='center',
                 fontdict = fontLeg,
                 bbox = dict(facecolor='white', alpha=0.7, edgecolor = 'k'))
        
        Olimi = [0, 0, 0, 2, 2.6, 3.3, 4, 2, 2, 5, 5, 2]
        Olimf = [2, 2, 2, 2.6, 3.3, 4, 5, 5, 5, 10, 10, 10]
        Rlimi = [0, 3, 7, 0, 0, 0, 0, 1, 3, 0, 3, 7]
        Rlimf = [3, 7, 15, 1, 1, 1, 1, 3, 7, 3, 7, 15]
        names = ['REFLEJANTE',
                 'TERRAZA DE BAJAMAR\nCON CORRIENTE\nDE RETORNO',
                 'TERRAZA DE BAJAMAR\nSIN CORRIENTE',
                 'TBM','BT','BR','BL',
                 'BARRA TRANSVERSAL CON\nCORRIENTE DE RETORNO',
                 'BARRA DE BAJAMAR CON\nCORRIENTE DE RETORNO',
                 'DISIPATIVO CON BARRA',
                 'DISIPATIVO SIN BARRA',
                 'UNTRADISIPATIVO']

        [plt.plot([Olimi[it], Olimi[it], Olimf[it], Olimf[it], Olimi[it]],
             [Rlimi[it], Rlimf[it], Rlimf[it], Rlimi[it], Rlimi[it]],
             'w-',lw=2) for it in range(12)]
        [plt.text(np.mean([Olimf[it], Olimi[it]]),
                 np.mean([Rlimf[it], Rlimi[it]]),
                 names[it],
                 ha='center',
                 va='center',
                 fontdict = fontPRF,
                 path_effects=eBuff) for it in range(12)]
        plt.gca().invert_yaxis()
        plt.savefig(savePath)
        plt.show()

def AUXgraphEMD2(x,y,z,perLim,tit,savePath, D, phi, CM, calmas):
        plt.figure(figsize=(12, 6), dpi=200, linewidth=5, edgecolor="#04253a")
        plt.ylabel(r'$RTR$', fontdict=font)
        plt.xlabel(r'$\overline{\Omega}$', fontdict=font)
        plt.contourf(x, y, z, cmap='coolwarm',
                     levels = np.linspace(perLim[0],perLim[1],50),
                     extend = 'both')
        plt.clim(perLim[0], perLim[1])
        color_bar = plt.colorbar(ticks=np.linspace(perLim[0],perLim[1],5))
        ax = plt.gca()
        color_bar.ax.set_yticklabels(["{:.1f}".format(x) + '%' for x in np.linspace(perLim[0],perLim[1],5)])
        plt.title(tit,fontdict=fontTitle)
        plt.xticks(np.linspace(0,10,11))
        plt.yticks([0, 1, 3, 5, 7, 10, 12, 15])
        plt.xlim(0, 10)
        plt.ylim(0, 15)
        eBuff = [pe.withStroke(linewidth=2, foreground='k')]
        plt.text(9,
                 13.5,
                 'CM = ' + str(CM) + ' m\nD = ' + str(D) + ' días\n$\phi$ = ' + str(phi) + ' días\nCalmas = ' + str(int(calmas)) + ' %',
                 ha='center',
                 va='center',
                 fontdict = fontLeg,
                 bbox = dict(facecolor='white', alpha=0.7, edgecolor = 'k'))
        
        Olimi = [0, 0, 0, 2, 2.6, 3.3, 4, 2, 2, 5, 5, 2]
        Olimf = [2, 2, 2, 2.6, 3.3, 4, 5, 5, 5, 10, 10, 10]
        Rlimi = [0, 3, 7, 0, 0, 0, 0, 1, 3, 0, 3, 7]
        Rlimf = [3, 7, 15, 1, 1, 1, 1, 3, 7, 3, 7, 15]
        names = ['REFLEJANTE',
                 'TERRAZA DE BAJAMAR\nCON CORRIENTE\nDE RETORNO',
                 'TERRAZA DE BAJAMAR\nSIN CORRIENTE',
                 'TBM','BT','BR','BL',
                 'BARRA TRANSVERSAL CON\nCORRIENTE DE RETORNO',
                 'BARRA DE BAJAMAR CON\nCORRIENTE DE RETORNO',
                 'DISIPATIVO CON BARRA',
                 'DISIPATIVO SIN BARRA',
                 'UNTRADISIPATIVO']

        [plt.plot([Olimi[it], Olimi[it], Olimf[it], Olimf[it], Olimi[it]],
             [Rlimi[it], Rlimf[it], Rlimf[it], Rlimi[it], Rlimi[it]],
             'k-',lw=2) for it in range(12)]
        [plt.text(np.mean([Olimf[it], Olimi[it]]),
                 np.mean([Rlimf[it], Rlimi[it]]),
                 names[it],
                 ha='center',
                 va='center',
                 fontdict = fontPRF,
                 path_effects=eBuff) for it in range(12)]
        plt.gca().invert_yaxis()
        plt.savefig(savePath)
        plt.show()

def graphEMDlimpio(estMD, perLim):
    estMD.percentOcurr[:,:] = 0
    AUXgraphEMDlimpio(estMD.Hist_x,estMD.Hist_y,estMD.percentOcurr,perLim)

def AUXgraphEMDlimpio(x,y,z,perLim):
        plt.figure(figsize=(12, 6), dpi=200, linewidth=5, edgecolor="#04253a")
        plt.ylabel(r'$RTR$', fontdict=font)
        plt.xlabel(r'$\overline{\Omega}$', fontdict=font)
        plt.contourf(x, y, z, cmap='jet',
                     levels = np.linspace(perLim[0],perLim[1],50),
                     extend = 'max')
        
        plt.xticks(np.linspace(0,10,11))
        plt.yticks([0, 1, 3, 5, 7, 10, 12, 15])
        plt.xlim(0, 10)
        plt.ylim(0, 15)
        eBuff = [pe.withStroke(linewidth=2, foreground='k')]
       
        
        Olimi = [0, 0, 0, 2, 2.6, 3.3, 4, 2, 2, 5, 5, 2]
        Olimf = [2, 2, 2, 2.6, 3.3, 4, 5, 5, 5, 10, 10, 10]
        Rlimi = [0, 3, 7, 0, 0, 0, 0, 1, 3, 0, 3, 7]
        Rlimf = [3, 7, 15, 1, 1, 1, 1, 3, 7, 3, 7, 15]
        names = ['R','TBMCR','TBMSC','TBM','BT','BR','BL','BTCR','BBCR','DB','DSB','UD']

        [plt.plot([Olimi[it], Olimi[it], Olimf[it], Olimf[it], Olimi[it]],
             [Rlimi[it], Rlimf[it], Rlimf[it], Rlimi[it], Rlimi[it]],
             'w-',lw=2) for it in range(12)]
        [plt.text(np.mean([Olimf[it], Olimi[it]]),
                 np.mean([Rlimf[it], Rlimi[it]]),
                 names[it],
                 ha='center',
                 va='center',
                 fontdict = fontPRF,
                 path_effects=eBuff) for it in range(12)]
        plt.savefig('EjemploLimio.png')
        plt.show()
