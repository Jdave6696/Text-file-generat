# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 22:22:16 2022

@author: Jalpesh
"""
import numpy as np
file=1
for temp in range(300,320,5):
    for CO2 in range(400,550,50):
        for WV in np.arange(0.5,3.5,0.5):
                with open(f"{file}_lambertian.txt","w") as f:
                f.write(f"M F 1    3    2    1    0    0    0    0    0    0    0    0    0 {temp:.3f}    -50\n")
                f.write(f"fFF  21.00   {CO2:.3f}g {WV:.6f}a 0.3000001F T F F FF              0.000     0.000     0.000     0.000         0\n")
                f.write(f"01_2013\n")
                f.write(f"1.0001.0001.0501.0001.0001.0001.0001.0001.0001.000\n")    
                f.write(f"    1    0    1    0    0    0     0.000     0.000     0.000     0.000     0.000\n")
                f.write(f"100.000000  0.000000180.000000   0.00000  0.0000006378.00000    0       0.000000  0.000000\n")
                f.write(f"    0    2  256    0\n")
                f.write(f"     0.000    81.200     0.000     0.000     0.000     0.000     0.000     0.000\n")
                f.write(f"2000.0000040000.0000   1.00000   1.00000 W                 0     0.000\n")
                f.write(f"    0\n")
                file=file+1