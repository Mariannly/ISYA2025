# Import libraries
import numpy as np
import matplotlib.pyplot as plt
# Importing Cosmology tools from astropy
from astropy.cosmology import FlatLambdaCDM

# Define the cosmology
cosmo = FlatLambdaCDM(H0=70, Om0=0.27, Tcmb0=2.725)

# Define a range of redshifts
redshift = np.linspace(0, 10, 500)

# Calculate the age of the universe at each redshift
age_of_universe_gyr = cosmo.age(redshift).to('Gyr').value

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(redshift, age_of_universe_gyr, color='magenta', linestyle = "--")
plt.xlabel('Redshift (z)')
plt.ylabel('Age of Universe (Gyr)')
plt.title('Age of Universe vs. Redshift')
plt.grid(True)
plt.savefig("./images/age_universe.png")
