from motores import *
import time
controlar_motores("w")

time.sleep(2)
controlar_motores("stop")

time.sleep(5)
controlar_motores("a")

time.sleep(0.5)
controlar_motores("w")

time.sleep(2)
controlar_motores("s")
