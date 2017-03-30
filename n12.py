def get_frames(signal,size=8,overlap=0.3): 
    print ('Step: ') 
    step = size * overlap 
    print (step) 

    for i in signal: 
        print (signal[i:i+size]) 

size = 4 
signal = [i for i in range(0,1024)] 
overlap = 0.5

get_frames(signal,size,overlap)
