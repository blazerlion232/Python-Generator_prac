import numpy as np


    
def temperature():
    temp = np.random.randint(20, 100)
    yield temp

def monitor():
    print("========== CPU TEMPERATURE MONITOR ==========")
    for i in range(10):
        for i, x in enumerate(temperature(), start=1):
            print(f"Reading {i}: {x}")
            if x > 80: 
                print("WARNING TOO HOT!")

    print("==============================================")

monitor()            
