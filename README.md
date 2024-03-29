This package contains functions used in data processing of hyperspectral images
captured using a scanning Fabry-Pérot interferometer (FPI). This includes transmission
simulations of the FPI itself.

-------------------


## Key Features:

* **Image importing**

* **Most common image analysis**

* **Fabry-Pérot simulation**




## The Quick Start below can be executed given that the following points are at hand:

* **A hyperspectral long wavelength infrared image with the following tree structure:**

        - images/
            - capture/
                - RGB.pnm
                - step4.pnm
                - step13.pnm
                .
                .
                .
                - step1327.pnm
        - output.txt
        - properties.json

* **An example of an absorption spectrum (which may be acquired from an FTIR spectrometer)**

        #The quick start below uses a .csv file which contains a transmission measurement of ethylene gas.

        - Ethylene.csv

* **A sensor response function in the form of a pickle file**

        #The quick start below also uses a pickle file containing the sensor response of the camera.

        - sensor_response.pkl




## Quick Start


1. **Installation** - Run `pip3 install HSTI`.


2. **Importing the HSTI package in a e.g. Jupyter notebook or .py file along with other relevant packages**

        import HSTI

        # packages required for running the code blocks below

        import matplotlib.pyplot as plt
        import numpy as np
        from scipy.interpolate import interp1d
        import pickle

3. **Importing a hyperspectral image from an experiment directory**

        # The path below should be changed to the specific path used on the local PC
        path = '/home/user/experiments/experiment_1'

        HS_image = HSTI.import_data_cube(path)

4. **Performing a PCA of the hyperspectral image**

        PCA_object = HSTI.PCA()

        #transform image to two-dimensional
        two_dim = np.reshape(HS_image,(HS_image.shape[0]*HS_image.shape[1],HS_image.shape[2]))

        #calculate and apply PCA
        PCA_object.calculate_pca(two_dim)
        PCA_two_dim_imgs = PCA_object.apply_pca(two_dim)

        #create three-dimensional datacube with PCA images
        pca_imgs = np.reshape(PCA_two_dim_imgs,(HS_image.shape[0],HS_image.shape[1],HS_image.shape[2]))


5. **Visualising the principal components**

        #import string for labelling images
        import string

        fig,ax = plt.subplots(4,4,figsize=(14,16.0))

        newtec_cm = HSTI.import_cm()

        plt.rc('xtick', labelsize=8)
        plt.rc('ytick', labelsize=8)
        plt.rc('axes', labelsize=10)
        plt.rc('lines', linewidth=2)
        plt.rc('legend', fontsize=8)
        plt.rc('figure', titlesize=10)
        plt.rc('axes', titlesize=10)

        axs = ax.flat

        for idx,ax in enumerate(axs):

          _std = np.std(pca_imgs[:,:,idx])
          _mean = np.mean(pca_imgs[:,:,idx])

          if idx < 16:
            im = ax.imshow(pca_imgs[:,:,idx],vmin = _mean-2*_std,vmax = _mean+2*_std, cmap=newtec_cm)
            ax.text(0.5, 0.92, 'PC' + str(idx+1), transform=ax.transAxes,
                size=12, weight='bold', horizontalalignment='center',color='white')

            ax.text(0.02, 0.92,'(' + string.ascii_uppercase[idx] + ')', transform=ax.transAxes,
            size=10, weight='bold',color='white')

          if idx == 0 or idx == 4 or idx == 8 or idx == 12:
            ax.set_ylabel('Y [y$_j$]')

          if idx > 11:
            ax.set_xlabel('X [x$_i$]')


        plt.tight_layout()
        plt.savefig('experiment_1' + '_PCA' + '.png', dpi=100, bbox_inches='tight')


6. **Simulating the Fabry-Pérot transmission based on an absorption spectrum**

        X_min = 3.6 # µm
        X_max = 14  # µm


        lam = np.linspace(X_min,X_max,150)
        wvls = np.linspace(7.5,16,1000)

        sys_matrix, R_matrix = HSTI.fpi_gmm(lam*10**-6, wvls*10**-6, n_points = 9)

        with open('sensor_response.pkl', 'rb') as file:
            sensor_response = pickle.load(file)


        C2H4 = np.loadtxt("Ethylene.csv", delimiter=",")

        wvls_C2H4 = 1/(C2H4[:,0]*100)

        f = interp1d(wvls_C2H4*10**6, C2H4[:,1])


        C2H4_sim = []
        BB = []

        for i in range(sys_matrix.shape[0]):
            BB.append(np.sum(sys_matrix[i,:]*sensor_response(1/(wvls*10**-6))*np.ones(len(wvls))))
            C2H4_sim.append(np.sum(sys_matrix[i,:]*sensor_response(1/(wvls*10**-6))*f(wvls)))

        BB = np.array(BB)
        C2H4_sim = np.array(C2H4_sim)


        fig,(ax1,ax2) = plt.subplots(1,2,figsize=(12,4))


        ax1.set_title("Simulation of raw spectra")
        ax1.plot(lam,C2H4_sim-C2H4_sim[0],label = "Ethylene")
        ax1.plot(lam,BB-BB[0],label = "Blackbody")
        ax1.set_ylabel("Intensity [a.u.]")
        ax1.set_xlabel("Mirror Separation [µm]")

        ax1.ticklabel_format(axis="y",style="sci",scilimits=(0,0))
        ax1.legend()


        ax2.set_title("Simulated spectra with BB as a reference")
        ax2.set_ylabel("Intensity [a.u.]")
        ax2.set_xlabel("Mirror Separation [µm]")
        ax2.plot(lam,(BB-BB[0])-(C2H4_sim-C2H4_sim[0]),label = "Blackbody - Ethylene")
        ax2.plot(lam,(BB-BB[0])-(BB-BB[0]),label = "Blackbody - Blackbody")


        ax2.ticklabel_format(axis="y",style="sci",scilimits=(0,0))
        ax2.legend()

        plt.tight_layout()

        plt.savefig("Simulated_Ethylene.png", dpi=600)




-------------------
# Contact

  *For bug reports or other questions please contact mani@newtec.dk or alj@newtec.dk.*
