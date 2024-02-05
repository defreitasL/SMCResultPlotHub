import numpy as np

class meshSMC:
    """
    meshSMC class represents a structured mesh for SMC (SistemadeModelado Costero) simulations.

    Attributes:
    - name (str): The name of the mesh.
    - moplaPath (str): The path where Mopla files are located.
    - angmesh (float): The angle of the mesh in radians.
    - x0 (float): Minimum x-coordinate after rotation.
    - y0 (float): Minimum y-coordinate after rotation.
    - x0o (float): Original x-coordinate.
    - y0o (float): Original y-coordinate.
    - Ly (float): Length of the mesh in the y-direction.
    - Lx (float): Length of the mesh in the x-direction.
    - dy (float): Grid spacing in the y-direction.
    - dx (float): Grid spacing in the x-direction.
    - ny (int): Number of grid points in the y-direction.
    - nx (int): Number of grid points in the x-direction.
    - x (numpy.ndarray): X-coordinates of the mesh.
    - y (numpy.ndarray): Y-coordinates of the mesh.
    - z (numpy.ndarray): Bathymetry data of the mesh.

    Methods:
    - __init__(self, name, moplaPath): Initializes the meshSMC object.
    """

    def __init__(self, name, moplaPath):
        """
        Initializes a new instance of the meshSMC class.

        Parameters:
        - name (str): The name of the mesh.
        - moplaPath (str): The path where Mopla files are located.
        """
        self.name = name
        self.moplaPath = moplaPath

        # Reading meshREF file
        meshREF = open(moplaPath + '/' + name + 'REF2.DAT', 'r')
        meshREF = meshREF.read()
        meshREF = meshREF.replace('\n', ' ')
        meshREF = meshREF.replace('  ', ' ')
        meshREF = meshREF.replace('  ', ' ')
        meshREF = meshREF[11:-1]
        meshREF = meshREF.split(' ')
        x0, y0, angmesh = float(meshREF[0]), float(meshREF[1]), np.radians(float(meshREF[2]))

        # Extracting dimensions from meshREF
        Lx, Ly, nx, ny = float(meshREF[3]), float(meshREF[4]), int(meshREF[5]), int(meshREF[6])
        dx, dy = float(meshREF[7]), float(meshREF[8])

        # Creating mesh grid
        xx = np.linspace(0, Lx, nx)
        yy = np.linspace(0, Ly, ny)
        X, Y = np.meshgrid(xx, yy)

        # Reading bathymetry data
        bathy = open(moplaPath + '/RD/' + name + '_Bathymetry_Inp.grd', 'r')
        bathy = bathy.read()
        for i in range(7):
            bathy = bathy.replace('  ', ' ')
        bathy = bathy.replace('\n', ' ')
        bathy = bathy.replace('  ', ' ')
        bathy = bathy.replace('  ', ' ')
        bathy = bathy[5:-1]
        bathy = bathy.split(' ')

        # Creating Z (bathymetry) array
        mkFl = np.vectorize(lambda i: float(bathy[i + 8]))
        Z = mkFl(range(len(bathy[8:-1]) + 1)).reshape(nx, ny)

        # Rotating the mesh
        XX = X * np.cos(angmesh) - Y * np.sin(angmesh) + x0
        YY = Y * np.cos(angmesh) + X * np.sin(angmesh) + y0

        # Assigning attributes
        self.angmesh = angmesh
        self.x0 = np.min(XX)
        self.y0 = np.min(YY)
        self.x0o = x0
        self.y0o = y0
        self.Ly = Ly
        self.Lx = Lx
        self.dy = dy
        self.dx = dx
        self.ny = ny
        self.nx = nx
        self.x = XX
        self.y = YY
        self.z = np.flipud(Z.T)
