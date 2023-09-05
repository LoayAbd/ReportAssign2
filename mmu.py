'''
* Interface for Memory Management Unit.
* The memory management unit should maintain the concept of a page table.
* As pages are read and written to, this changes the pages loaded into the
* the limited number of frames. The MMU keeps records, which will be used
* to analyse the performance of different replacement strategies implemented
* for the MMU.
*
'''
class MMU:

    MMUlist = []
    running_disk_reads = 0
    running_disk_writes = 0
    running_page_faults = 0

    def read_memory(self, page_number):

        found = False
        if self.MMUlist:
           for i in range(len(self.MMUlist)): # check if page is in MMUlist

                if page_number == self.MMUlist[i][0]: # if page is in MMUlist

                    return 0



        if not found: # if page is not in MMUlist
            self.MMUlist.append([page_number , 0])
            self.running_disk_reads += 1 # increment disk reads
            self.running_page_faults += 1 # increment page faults
            return 1



    def write_memory(self, page_number):



        found = False
        if self.MMUlist:
           for i in range(len(self.MMUlist)): # check if page is in MMUlist

               if page_number == self.MMUlist[i][0]: # if page is in MMUlist

                    self.MMUlist[i][1] = 1 # set dirty bit to 1
                    return 0





        if not found: # if page is not in MMUlist
            self.MMUlist.append([page_number , 1])
            self.running_disk_reads += 1 # increment disk reads
            self.running_page_faults += 1 # increment page faults

            return 1;


    def set_debug(self):
        pass

    def reset_debug(self):
        pass

    def get_total_disk_reads(self):

        return self.running_disk_reads

    def get_total_disk_writes(self):
        return self.running_disk_writes

    def get_total_page_faults(self):
        return self.running_page_faults

    def replace_victim(self, page_number):

        for i in range(len(self.MMUlist)):
            if page_number == self.MMUlist[i][0]:

                if self.MMUlist[i][1] == 1: # if dirty bit is 1
                    self.running_disk_writes += 1
                    self.MMUlist.remove(self.MMUlist[i])
                    return 1 # return 1 if dirty bit is 1

        self.MMUlist.remove([page_number , 0])

        return 0


    def pass_frames(self, frames):
        if len(self.MMUlist) >= frames:
            return 1
        return 0

