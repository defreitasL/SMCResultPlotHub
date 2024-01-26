from setuptools import setup, find_packages

setup(
    name='SMCResultPlotHub',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'numpy',
        'scipy',
        'matplotlib',
        'pandas',
        # Adicione aqui outras dependências, se necessário
    ],
    author='Lucas de Freitas Pereira',
    author_email='lucas.defreitas@unican.es',
    description='Read SMC data',
    url='https://github.com/defreitasL/SMCResultPlotHub',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)