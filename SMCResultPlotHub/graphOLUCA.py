# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 14:07:49 2023

@author: freitasl
"""
import numpy as np
import matplotlib.pyplot as plt
import dxfgrabber
from SMCResultPlotHub.readData import readData, readDataCOPLA
# AA = [H, T, SL, DIR]

def graphHsDir(mesh, caseConfig, graphConfig):
    """
    Graphs the significant wave height and direction for a given case.

    Parameters:
    - mesh (meshSMC): The meshSMC object representing the mesh.
    - caseKey (str): The case identifier.
    - AA (numpy.ndarray): The array containing the cases to be plotted.
    - it (int): The index of the case to be plotted.
    - fileName1 (list): The list of file names for the significant wave height and direction plots.
    - fileName2 (list): The list of file names for the significant wave height in breaking plots.
    - fileName3 (list): The list of file names for the velocity plots.
    """
    
    # graph parameters
    EPSGdict = dict(boxstyle="round",
                    edgecolor="black",
                    fc = "white")
    EPSG = graphConfig["EPSG"]
    font = graphConfig["font"]
    img = plt.imread(graphConfig["img"])
    corners = graphConfig["corners"]
    zoom = graphConfig["zoom"]
    try:
        xticks = graphConfig["xticks"]
    except:
     Warning("xticks not defined")
    
    try:
        yticks = graphConfig["yticks"]
    except:
        Warning("yticks not defined")
    xticks = graphConfig["xticks"]
    yticks = graphConfig["yticks"]
    desplEPSG = graphConfig["desplEPSG"]
    northXYflag = graphConfig["northXYflag"]
    north = graphConfig["north"]
    spcH = graphConfig["spcH"]
    spcV = graphConfig["spcV"]
    flagDXF = graphConfig["flagDXF"]
    if flagDXF:
        DXF = dxfgrabber.readfile(graphConfig["DXF"])
    levels = graphConfig["levels"]
    tks = graphConfig["tks"]
    fileName = graphConfig["fileName"]
    figureSize = graphConfig["figureSize"]
    arrowScale = graphConfig["arrowScale"]
    arrowWidth = graphConfig["arrowWidth"]
    arrowHeadWidth = graphConfig["arrowHeadWidth"]
    arrowLength = graphConfig["arrowLength"]
    arrowAxisLength = graphConfig["arrowAxisLength"]
    cmapHs = graphConfig["cmapHs"]
    dxfLW = graphConfig["dxfLW"]
    
    # case parameters
    caseKey = caseConfig["caseKey"]
    seaLvl = caseConfig["seaLvl"]
    Hi = caseConfig["Hi"]
    Tp = caseConfig["Tp"]
    lblDir = caseConfig["lblDir"]
    lblEta = caseConfig["lblEta"]  

    Hs, Dir = readData(mesh, caseKey)
    Hs[mesh.z <= -seaLvl] = float("nan")
    Hsx, Hsy = Hs/np.nanmax(Hs) * np.sin(np.radians(Dir)), -Hs/np.nanmax(Hs) * np.cos(np.radians(Dir))

    idxZoom = np.logical_or(np.logical_or(np.logical_or(mesh.x<zoom[0],mesh.x>zoom[1]),mesh.y<zoom[2]),mesh.y>zoom[3])
    Hs[idxZoom] = float("nan")
    Hsx[idxZoom] = float("nan")
    Hsx[mesh.z <= -seaLvl] = float("nan")
    Hsy[idxZoom] = float("nan")
    Hsy[mesh.z <= -seaLvl] = float("nan")

    plt.figure(figsize=figureSize, dpi=400, linewidth=5, edgecolor="#04253a")
    plt.ylabel('Y [UTM]', fontdict=font)
    plt.xlabel('X [UTM]', fontdict=font)
    # plt.axis('equal')
    plt.imshow(img, extent = corners)
    plt.contourf(mesh.x, mesh.y, Hs, levels, vmin=min(levels),
                    vmax=max(levels), cmap=cmapHs, extend='max',alpha=1)
    plt.clim(min(levels), max(levels))
    color_bar = plt.colorbar(ticks=tks)
    color_bar.minorticks_on()
    color_bar.set_label(label=r'$H_s$ [m]', weight='bold', size=10)
    plt.quiver(mesh.x[0::spcH,0::spcV],mesh.y[0::spcH,0::spcV],Hsx[0::spcH,0::spcV],
            Hsy[0::spcH,0::spcV],
            scale=arrowScale,
            width= arrowWidth,
            headwidth=arrowHeadWidth, 
            headlength=arrowLength,
            headaxislength=arrowAxisLength)
    plt.title(r'$H_s$ = '+str(Hi)+
                r' m | $T_p$ = '+str(Tp)+
                ' s | '+lblDir+
                ' | NM - '+lblEta+' - Espectral',
                fontdict=font)
    if flagDXF:
        for entity in DXF.entities:
            if entity.dxftype == 'POLYLINE':
                vertices = entity.vertices
                x = [v[0] for v in vertices]
                y = [v[1] for v in vertices]
                plt.plot(x, y, color='black', lw = dxfLW)
    plt.xlim(zoom[0], zoom[1])
    plt.ylim(zoom[2], zoom[3])
    plt.xticks(xticks)
    plt.yticks(yticks)
    plt.text(plt.xlim()[0]+desplEPSG[0], plt.ylim()[0]+desplEPSG[1],
                r'EPSG: '+str(int(EPSG)), fontdict = font,
                bbox=EPSGdict)
    xRose = [plt.xlim()[1]-northXYflag[0]+north[0]/2,
                plt.xlim()[1]-northXYflag[0]+north[0],
                plt.xlim()[1]-northXYflag[0]+north[0]/2,
                plt.xlim()[1]-northXYflag[0],
                plt.xlim()[1]-northXYflag[0]+north[0]/2]
    yRose = [plt.ylim()[0]+northXYflag[1]+north[1],
                plt.ylim()[0]+northXYflag[1],
                plt.ylim()[0]+northXYflag[1]+north[1]/3,
                plt.ylim()[0]+northXYflag[1],
                plt.ylim()[0]+northXYflag[1]+north[1]]
    plt.fill(xRose, yRose, color='white', edgecolor='k', linewidth=1.5, zorder = 50)
    plt.plot([xRose[0],xRose[2]],[yRose[0],yRose[2]], color = 'k', lw = 1, ls='-', zorder = 51)
    plt.gca().set_yticklabels(['{:.0f}'.format(x) for x in plt.gca().get_yticks()])
    plt.savefig(fileName)
    plt.show()

def graphCopla(mesh, caseConfig, graphConfig):
    """
    Graphs the significant wave height and direction for a given case.

    Parameters:
    - mesh (meshSMC): The meshSMC object representing the mesh.
    - caseKey (str): The case identifier.
    - AA (numpy.ndarray): The array containing the cases to be plotted.
    - it (int): The index of the case to be plotted.
    - fileName1 (list): The list of file names for the significant wave height and direction plots.
    - fileName2 (list): The list of file names for the significant wave height in breaking plots.
    - fileName3 (list): The list of file names for the velocity plots.
    """
    
    # graph parameters
    EPSGdict = dict(boxstyle="round",
                    edgecolor="black",
                    fc = "white")
    EPSG = graphConfig["EPSG"]
    font = graphConfig["font"]
    img = plt.imread(graphConfig["img"])
    corners = graphConfig["corners"]
    zoom = graphConfig["zoom"]
    try:
        xticks = graphConfig["xticks"]
    except:
     Warning("xticks not defined")
    
    try:
        yticks = graphConfig["yticks"]
    except:
        Warning("yticks not defined")
    xticks = graphConfig["xticks"]
    yticks = graphConfig["yticks"]
    desplEPSG = graphConfig["desplEPSG"]
    northXYflag = graphConfig["northXYflag"]
    north = graphConfig["north"]
    spcH = graphConfig["spcH"]
    spcV = graphConfig["spcV"]
    flagDXF = graphConfig["flagDXF"]
    if flagDXF:
        DXF = dxfgrabber.readfile(graphConfig["DXF"])
    levels = graphConfig["levels"]
    tks = graphConfig["tks"]
    fileName = graphConfig["fileName"]
    figureSize = graphConfig["figureSize"]
    arrowScale = graphConfig["arrowScale"]
    arrowWidth = graphConfig["arrowWidth"]
    arrowHeadWidth = graphConfig["arrowHeadWidth"]
    arrowLength = graphConfig["arrowLength"]
    arrowAxisLength = graphConfig["arrowAxisLength"]
    cmapVel = graphConfig["cmapHs"]
    dxfLW = graphConfig["dxfLW"]
    
    # case parameters
    caseKey = caseConfig["caseKey"]
    seaLvl = caseConfig["seaLvl"]
    Hi = caseConfig["Hi"]
    Tp = caseConfig["Tp"]
    lblDir = caseConfig["lblDir"]
    lblEta = caseConfig["lblEta"]

    idxZoom = np.logical_or(np.logical_or(np.logical_or(mesh.x<zoom[0],mesh.x>zoom[1]),mesh.y<zoom[2]),mesh.y>zoom[3])
    U, ux, uy = readDataCOPLA(mesh, caseKey)
    U[idxZoom] = float("nan")
    U[mesh.z <= -seaLvl] = float("nan")
    ux[idxZoom] = float("nan")
    ux[mesh.z <= -seaLvl] = float("nan")
    uy[idxZoom] = float("nan")
    uy[mesh.z <= -seaLvl] = float("nan")

    # ux[U<0.1] = float("nan")
    # uy[U<0.1] = float("nan")
    ux = ux/np.nanmax(np.abs(U))
    uy = uy/np.nanmax(np.abs(U))
    U = np.abs(U)
    # U = np.abs(U/np.nanmax(np.abs(U)))
    
    plt.figure(figsize=figureSize, dpi=400, linewidth=5, edgecolor="#04253a")
    plt.ylabel('Y [UTM]', fontdict=font)
    plt.xlabel('X [UTM]', fontdict=font)
    # plt.axis('equal')
    # plt.pcolormesh(xIMG,yIMG,img)
    plt.imshow(img, extent = corners)
    plt.contourf(mesh.x, mesh.y, U, levels, vmin=min(levels),
                    vmax=max(levels), cmap=cmapVel, extend='max',alpha=1)
    plt.clim(min(levels), max(levels))
    color_bar = plt.colorbar(ticks=tks)
    color_bar.minorticks_on()
    color_bar.set_label(label=r'$U$ [m/s]', weight='bold', size=10)
    plt.quiver(mesh.x[0::spcH,0::spcV],mesh.y[0::spcH,0::spcV],-ux[0::spcH,0::spcV],
                uy[0::spcH,0::spcV],
                scale=arrowScale,
                width= arrowWidth,
                headwidth=arrowHeadWidth, 
                headlength=arrowLength,
                headaxislength=arrowAxisLength)
    plt.title(r'$H_s$ = '+str(Hi)+
                r' m | $T_p$ = '+str(Tp)+
                ' s | '+lblDir+
                ' | NM - '+lblEta+' - Espectral',
                fontdict=font)
    if flagDXF:
        for entity in DXF.entities:
            if entity.dxftype == 'POLYLINE':
                vertices = entity.vertices
                x = [v[0] for v in vertices]
                y = [v[1] for v in vertices]
                plt.plot(x, y, color='black', lw = dxfLW)
    plt.xlim(zoom[0], zoom[1])
    plt.ylim(zoom[2], zoom[3])
    plt.xticks(xticks)
    plt.yticks(yticks)
    plt.text(plt.xlim()[0]+desplEPSG[0], plt.ylim()[0]+desplEPSG[1],
                r'EPSG: '+str(int(EPSG)), fontdict = font,
                bbox=EPSGdict)
    xRose = [plt.xlim()[1]-northXYflag[0]+north[0]/2,
                plt.xlim()[1]-northXYflag[0]+north[0],
                plt.xlim()[1]-northXYflag[0]+north[0]/2,
                plt.xlim()[1]-northXYflag[0],
                plt.xlim()[1]-northXYflag[0]+north[0]/2]
    yRose = [plt.ylim()[0]+northXYflag[1]+north[1],
                plt.ylim()[0]+northXYflag[1],
                plt.ylim()[0]+northXYflag[1]+north[1]/3,
                plt.ylim()[0]+northXYflag[1],
                plt.ylim()[0]+northXYflag[1]+north[1]]
    plt.fill(xRose, yRose, color='white', edgecolor='k', linewidth=1.5)
    plt.plot([xRose[0],xRose[2]],[yRose[0],yRose[2]], color = 'k', lw = 1, ls='-')
    plt.gca().set_yticklabels(['{:.0f}'.format(x) for x in plt.gca().get_yticks()])
    plt.savefig(fileName)

def graphBrk(mesh, caseConfig, graphConfig):
    
    # graph parameters
    EPSGdict = dict(boxstyle="round",
                    edgecolor="black",
                    fc = "white")
    EPSG = graphConfig["EPSG"]
    font = graphConfig["font"]
    img = plt.imread(graphConfig["img"])
    corners = graphConfig["corners"]
    zoom = graphConfig["zoom"]
    try:
        xticks = graphConfig["xticks"]
    except:
     Warning("xticks not defined")
    
    try:
        yticks = graphConfig["yticks"]
    except:
        Warning("yticks not defined")
    xticks = graphConfig["xticks"]
    yticks = graphConfig["yticks"]
    desplEPSG = graphConfig["desplEPSG"]
    northXYflag = graphConfig["northXYflag"]
    north = graphConfig["north"]
    spcH = graphConfig["spcH"]
    spcV = graphConfig["spcV"]
    flagDXF = graphConfig["flagDXF"]
    if flagDXF:
        DXF = dxfgrabber.readfile(graphConfig["DXF"])
    levels = graphConfig["levels"]
    tks = graphConfig["tks"]
    fileName = graphConfig["fileNameBrk"]
    figureSize = graphConfig["figureSize"]
    cmapHs = graphConfig["cmapHs"]
    dxfLW = graphConfig["dxfLW"]
    
    # case parameters
    caseKey = caseConfig["caseKey"]
    seaLvl = caseConfig["seaLvl"]
    Hi = caseConfig["Hi"]
    Tp = caseConfig["Tp"]
    lblDir = caseConfig["lblDir"]
    lblEta = caseConfig["lblEta"]  

    Hs, Dir = readData(mesh, caseKey)
    Hs[mesh.z <= -seaLvl] = float("nan")
    Hsx, Hsy = Hs/np.nanmax(Hs) * np.sin(np.radians(Dir)), -Hs/np.nanmax(Hs) * np.cos(np.radians(Dir))

    idxZoom = np.logical_or(np.logical_or(np.logical_or(mesh.x<zoom[0],mesh.x>zoom[1]),mesh.y<zoom[2]),mesh.y>zoom[3])
    Hs[idxZoom] = float("nan")
    Hsx[idxZoom] = float("nan")
    Hsx[mesh.z <= -seaLvl] = float("nan")
    Hsy[idxZoom] = float("nan")
    Hsy[mesh.z <= -seaLvl] = float("nan")

    
    rot = Hs / (mesh.z + seaLvl)
    HsRot = Hs
    HsRot[np.logical_or(rot>0.7, rot<0.4)] = float("nan")

    levels = np.linspace(0.5, 2, 100) # altura sde ola en rotura que se pintan
    tks = np.linspace(0.5, 2, 7)      # ticks del colorbar de las manchas de rotura

    plt.figure(figsize=figureSize, dpi=400, linewidth=5, edgecolor="#04253a")
    plt.ylabel('Y [UTM]', fontdict=font)
    plt.xlabel('X [UTM]', fontdict=font)
    # plt.axis('equal')

    plt.imshow(img, extent = corners)
    # #%% Bathy
    # levelsCont = [-4, -2, -1, 0, 1,  2,  3,  4, 5, 6, 7, 8, 9, 10, 12, 14, 16, 20]
    # plt.contour(XX,YY,mesh.z, levelsCont, linewidths = 1, cmap='Blues')
    # #%% end Bathy
    plt.contourf(mesh.x, mesh.y, HsRot, levels, vmin=min(
        levels), vmax=max(levels), cmap=cmapHs, extend='both',alpha=1) #/np.nanmax(HsRot)
    plt.clim(min(levels), max(levels))
    color_bar = plt.colorbar(ticks=tks)
    color_bar.minorticks_on()
    color_bar.set_label(label=r'$H_s \ at \ Breaking$ [m]', weight='bold', size=10)
    # plt.quiver(mesh.x[0::spcH,0::spcV],mesh.y[0::spcH,0::spcV],Hsx[0::spcH,0::spcV],
    #         Hsy[0::spcH,0::spcV],
    #         scale=arrowScale,
    #         width= arrowWidth,
    #         headwidth=arrowHeadWidth, 
    #         headlength=arrowLength,
    #         headaxislength=arrowAxisLength)
    plt.title(r'$H_s$ = '+str(Hi)+
                r' m | $T_p$ = '+str(Tp)+
                ' s | '+lblDir+
                ' | NM - '+lblEta+' - Espectral',
                fontdict=font)
    if flagDXF:
        for entity in DXF.entities:
            if entity.dxftype == 'POLYLINE':
                vertices = entity.vertices
                x = [v[0] for v in vertices]
                y = [v[1] for v in vertices]
                plt.plot(x, y, color='black', lw = dxfLW)
    plt.xlim(zoom[0], zoom[1])
    plt.ylim(zoom[2], zoom[3])
    plt.xticks(xticks)
    plt.yticks(yticks)
    plt.text(plt.xlim()[0]+desplEPSG[0], plt.ylim()[0]+desplEPSG[1],
                r'EPSG: '+str(int(EPSG)), fontdict = font,
                bbox=EPSGdict)
    xRose = [plt.xlim()[1]-northXYflag[0]+north[0]/2,
                plt.xlim()[1]-northXYflag[0]+north[0],
                plt.xlim()[1]-northXYflag[0]+north[0]/2,
                plt.xlim()[1]-northXYflag[0],
                plt.xlim()[1]-northXYflag[0]+north[0]/2]
    yRose = [plt.ylim()[0]+northXYflag[1]+north[1],
                plt.ylim()[0]+northXYflag[1],
                plt.ylim()[0]+northXYflag[1]+north[1]/3,
                plt.ylim()[0]+northXYflag[1],
                plt.ylim()[0]+northXYflag[1]+north[1]]
    plt.fill(xRose, yRose, color='white', edgecolor='k', linewidth=1.5, zorder = 50)
    plt.plot([xRose[0],xRose[2]],[yRose[0],yRose[2]], color = 'k', lw = 1, ls='-', zorder = 51)
    plt.gca().set_yticklabels(['{:.0f}'.format(x) for x in plt.gca().get_yticks()])
    plt.savefig(fileName)
    plt.show()
