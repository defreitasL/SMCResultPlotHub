import numpy as np

def readData(malla, caso):
    """
    Reads and processes height and direction data for a given mesh and case.

    Parameters:
    - malla (MallaSMC): The MallaSMC object representing the mesh.
    - caso (str): The case identifier.

    Returns:
    - Tuple: Tuple containing height (hs) and direction (dd) data arrays.
    """
    hsField = open(malla.moplaPath + '\\SP\\' + malla.name + caso + '_Height.GRD', 'r')
    hsField = hsField.read()
    for i in range(7):
        hsField = hsField.replace('  ', ' ')
    hsField = hsField.replace('\n', ' ')
    hsField = hsField.replace('  ', ' ')
    hsField = hsField.replace('  ', ' ')
    hsField = hsField[5:-1]
    hsField = hsField.split(' ')

    mkFl = np.vectorize(lambda i: float(hsField[i + 8]))
    hs = mkFl(range(len(hsField[8:-1]) + 1)).reshape(malla.nx, malla.ny)

    dirField = open(malla.moplaPath + '\\SP\\' + malla.name + caso + '_Direction.GRD', 'r')
    dirField = dirField.read()
    for i in range(7):
        dirField = dirField.replace('  ', ' ')
    dirField = dirField.replace('\n', ' ')
    dirField = dirField.replace('  ', ' ')
    dirField = dirField.replace('  ', ' ')
    dirField = dirField[5:-1]
    dirField = dirField.split(' ')

    mkFl = np.vectorize(lambda i: float(dirField[i + 8]))
    dd = mkFl(range(len(dirField[8:-1]) + 1)).reshape(malla.nx, malla.ny)

    dd = -dd + malla.angMalla
    return np.flipud(hs.T), np.flipud(dd.T)

def readDataCOPLA(malla, caso):
    """
    Reads and processes velocity and related data from COPLA simulations.

    Parameters:
    - malla (MallaSMC): The MallaSMC object representing the mesh.
    - caso (str): The case identifier.

    Returns:
    - Tuple: Tuple containing velocity (V), velocity x-component (vx), and velocity y-component (vy) data arrays.
    """
    Field = open(malla.moplaPath + '\\SP\\' + malla.name + caso + '_VelMod.GRD', 'r')
    Field = Field.read()
    for i in range(7):
        Field = Field.replace('  ', ' ')
    Field = Field.replace('\n', ' ')
    Field = Field.replace('  ', ' ')
    Field = Field.replace('  ', ' ')
    Field = Field[5:-1]
    Field = Field.split(' ')

    mkFl = np.vectorize(lambda i: float(Field[i + 8]))
    U = mkFl(range(len(Field[8:-1]) + 1)).reshape(malla.nx - 2, malla.ny - 2)

    Field = open(malla.moplaPath + '\\SP\\' + malla.name + caso + '_VelUx.GRD', 'r')
    Field = Field.read()
    for i in range(7):
        Field = Field.replace('  ', ' ')
    Field = Field.replace('\n', ' ')
    Field = Field.replace('  ', ' ')
    Field = Field.replace('  ', ' ')
    Field = Field[5:-1]
    Field = Field.split(' ')

    mkFl = np.vectorize(lambda i: float(Field[i + 8]))
    ux = mkFl(range(len(Field[8:-1]) + 1)).reshape(malla.nx - 2, malla.ny - 2)

    Field = open(malla.moplaPath + '\\SP\\' + malla.name + caso + '_VelUy.GRD', 'r')
    Field = Field.read()
    for i in range(7):
        Field = Field.replace('  ', ' ')
    Field = Field.replace('\n', ' ')
    Field = Field.replace('  ', ' ')
    Field = Field.replace('  ', ' ')
    Field = Field[5:-1]
    Field = Field.split(' ')

    mkFl = np.vectorize(lambda i: float(Field[i + 8]))
    uy = mkFl(range(len(Field[8:-1]) + 1)).reshape(malla.nx - 2, malla.ny - 2)

    U = np.flipud(U.T)
    ux = np.flipud(ux.T)
    uy = np.flipud(uy.T)

    V = np.zeros((malla.ny, malla.nx))
    uux = np.zeros((malla.ny, malla.nx))
    uuy = np.zeros((malla.ny, malla.nx))

    V[1:-1, 1:-1] = U
    uux[1:-1, 1:-1] = ux
    uuy[1:-1, 1:-1] = uy

    vx = uux * np.cos(malla.angMalla) - uuy * np.sin(malla.angMalla)
    vy = uuy * np.cos(malla.angMalla) + uux * np.sin(malla.angMalla)

    return V, vx, vy

def readDataMC(malla, caso, zoomFlag):
    """
    Reads and processes data for Monte Carlo simulations.

    Parameters:
    - malla (MallaSMC): The MallaSMC object representing the mesh.
    - caso (str): The case identifier.
    - zoomFlag (bool): Flag indicating whether to perform zoom.

    Returns:
    - Tuple: Tuple containing free surface elevation (eta), direction (dd), height (hs), phase, phase zoom, rotation, YY, and XX data arrays.
    """
    fsField = open(malla.moplaPath + '\\RD\\' + malla.name + caso + '_FreeSrf.GRD', 'r')
    fsField = fsField.read()
    for i in range(7):
        fsField = fsField.replace('  ', ' ')
    fsField = fsField.replace('\n', ' ')
    fsField = fsField.replace('  ', ' ')
    fsField = fsField.replace('  ', ' ')
    fsField = fsField[5:-1]
    fsField = fsField.split(' ')

    mkFl = np.vectorize(lambda i: float(fsField[i + 8]))
    eta = mkFl(range(len(fsField[8:-1]) + 1)).reshape(malla.nx, malla.ny)

    dirField = open(malla.moplaPath + '\\RD\\' + malla.name + caso + '_Direction.GRD', 'r')
    dirField = dirField.read()
    for i in range(7):
        dirField = dirField.replace('  ', ' ')
    dirField = dirField.replace('\n', ' ')
    dirField = dirField.replace('  ', ' ')
    dirField = dirField.replace('  ', ' ')
    dirField = dirField[5:-1]
    dirField = dirField.split(' ')

    mkFl = np.vectorize(lambda i: float(dirField[i + 8]))
    dd = mkFl(range(len(dirField[8:-1]) + 1)).reshape(malla.nx, malla.ny)

    dd = -dd + malla.angMalla

    hsField = open(malla.moplaPath + '\\RD\\' + malla.name + caso + '_Height.GRD', 'r')
    hsField = hsField.read()
    for i in range(7):
        hsField = hsField.replace('  ', ' ')
    hsField = hsField.replace('\n', ' ')
    hsField = hsField.replace('  ', ' ')
    hsField = hsField.replace('  ', ' ')
    hsField = hsField[5:-1]
    hsField = hsField.split(' ')

    mkFl = np.vectorize(lambda i: float(hsField[i + 8]))
    hs = mkFl(range(len(hsField[8:-1]) + 1)).reshape(malla.nx, malla.ny)

    if zoomFlag:
        zum = open(malla.moplaPath + '\\RD\\' + malla.name + caso + 'zum.dat', 'r')
        zumTOT = zum.read()
        zumTOT = zumTOT.replace('\n', ' ')
        for i in range(7):
            zumTOT = zumTOT.replace('  ', ' ')
        zumTOT = zumTOT.split(' ')
        ny = int(zumTOT[1])
        zumTOT = zumTOT[2:]

        mkFl = np.vectorize(lambda i: float(zumTOT[i]))
        yy = mkFl(range(ny))

        vecdx = np.zeros(malla.nx).astype(int)
        for i in range(malla.nx):
            vecdx[i] = (3 * ny + 3) * (i + 1) - i
        vecdx = np.concatenate((np.array([1]), vecdx))

        mkFl = np.vectorize(lambda i: float(zumTOT[i]))
        psibar = mkFl(vecdx)

        mkFl = np.vectorize(lambda i: float(zumTOT[i - 1]))
        xx = mkFl(vecdx)

        phasez = np.array([])
        for i in range(malla.nx):
            it = np.arange(vecdx[i] + ny + 1, vecdx[i] + 2 * ny + 1, 1).astype(int)
            for j in range(ny):
                aux = zumTOT[it[j]]
                aux = aux.replace('(', '')
                aux = aux.replace(')', '')
                aux = aux.split(',')
                phasez = np.concatenate(
                    (phasez, [(float(aux[0]) + float(aux[1]) * 1j) * np.exp(psibar[i] * 1j)]))

        mkFl = np.vectorize(lambda x: abs(np.rad2deg(np.arctan2(np.imag(x), np.real(x)))))
        phasez = mkFl(phasez).reshape(malla.nx, ny)

        Xz, Yz = np.meshgrid(xx[:-1], yy)
        XX = Xz * np.cos(malla.angMalla) - Yz * np.sin(malla.angMalla) + malla.x0o
        YY = Yz * np.cos(malla.angMalla) + Xz * np.sin(malla.angMalla) + malla.y0o

        rot = open(malla.moplaPath + '\\RD\\' + malla.name + caso + 'rot.dat', 'r')
        rotTOT = rot.read()
        rotTOT = rotTOT.replace('\n', ' ')
        for i in range(7):
            rotTOT = rotTOT.replace('  ', ' ')
        rotTOT = rotTOT.split(' ')
        rotTOT = rotTOT[1:-1]

        mkFl = np.vectorize(lambda i: float(rotTOT[i]))
        rot = mkFl(range(len(rotTOT))).reshape(malla.nx, ny)

        return np.flipud(eta.T), np.flipud(dd.T), np.flipud(hs.T), np.flipud(phase.T), phasez.T, rot.T, YY, XX
    else:
        phaseField = open(malla.moplaPath + '\\RD\\' + malla.name + caso + '_Phase.GRD', 'r')
        phaseField = phaseField.read()
        for i in range(7):
            phaseField = phaseField.replace('  ', ' ')
        phaseField = phaseField.replace('\n', ' ')
        phaseField = phaseField.replace('  ', ' ')
        phaseField = phaseField.replace('  ', ' ')
        phaseField = phaseField[5:-1]
        phaseField = phaseField.split(' ')

        mkFl = np.vectorize(lambda i: float(phaseField[i + 8]))
        phase = mkFl(range(len(phaseField[8:-1]) + 1)).reshape(malla.nx, malla.ny)

        return np.flipud(eta.T), np.flipud(dd.T), np.flipud(hs.T), np.flipud(phase.T)
