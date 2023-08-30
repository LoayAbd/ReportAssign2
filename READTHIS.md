# OpSys-Prac2
NOTE: DELETE BEFORE SUBMISSION

Hello Adam and Darcy,
  This readme file is a simple documentation of my mmu.py for easy reference when coding. Feel free to add to the readme file according to each of your allocated files.

  + FILE: mmu.py
      + read_memory:
          +@params: page_number
          + returns 0 : No page faults
          + return 1 : Page fault
      + write_memory:
          +@params : page_number
          + returns 0 : No page faults
          + return 1 : Page fault
      + pass_frames: passes the maximum number of frames available and checks if current MMUlist is equal to that or exceeds it. 
          +@params : frames
          + returns 0: Free space to be allocated in frames
          + returns 1: Frames full , need to replace a frame for any new operations.
       
      + replace_victim: removes a chosen frame
          +@params : page_number
        + returns 0 : page replaced successfully
       
      + get_whatever_method : simply returns running_ variable of the associated value.
  NOTE: One of the design decisions I made when setting up replace_victim and pass_frames is as follows :   I   assumed that read& write methods in lrummu , randmmu and clockmmu go as such : pass_frames is called from mmu , return value is stored , read/write operation is called   from mmu , resolves , if  read/write returns page fault (via return 1) and if the pass_frames return value was 1 ( as in frames are full) , replace victim is called passing a page_number to be removed based on policy. Of course there might be alternative ways of doing this that make the code more neat. So feel free to message me if you think it needs to be changed. 
        
        
