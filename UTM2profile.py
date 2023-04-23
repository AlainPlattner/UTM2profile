import pandas as pd
import numpy as np

# Import file name
# Assuming Easting, Northing, Elevation
filename = 'SmithUTM.csv'
fileout = 'SmithProfile.csv'

data = pd.read_csv(filename)
xpos = data.iloc[:,0]
ypos = data.iloc[:,1]


diffx = np.diff(xpos)
diffy = np.diff(ypos)
steps = np.sqrt(np.power(diffx,2) + np.power(diffy,2));
elev = data.iloc[:,2]
profile = pd.DataFrame([np.append(0,np.cumsum(steps)), elev]).transpose();

# export
profile.to_csv(fileout,index=False,header=False)
