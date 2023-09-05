from mmu import MMU


class ClockMMU(MMU):

    def __init__(self, frames):
        # TODO: Constructor logic for EscMMU
        self.frames = frames
        self.clock = []

    def set_debug(self):
        # TODO: Implement the method to set debug mode
        pass

    def reset_debug(self):
        # TODO: Implement the method to reset debug mode
        pass

    def read_memory(self, page_number):
        # TODO: Implement the method to read memory
        framesFull = super().pass_frames(self.frames)
        pageFault = super().read_memory(page_number)
        found = False
        if (pageFault): # page fault
            if (framesFull): # frames full
                for i in range(2):
                    for i in range(len(self.clock)): # find victim
                        if self.clock[i][1] == 0: # victim found
                            super().replace_victim(self.clock[i][0]) # replace victim
                            self.clock.remove(self.clock[i]) # remove victim from clock
                            found = True
                            break
                        else:
                            self.clock[i][1] = 0 # set use bit to 0 (in case of a second pass)
                    if found:
                        break



            self.clock.append([page_number, 1])

        else: # page hit
            for i in range(len(self.clock)): # find page
                if self.clock[i][0] == page_number: # page found
                    self.clock[i][1] = 1 # set use bit to 1
                    break


    def write_memory(self, page_number):
        # TODO: Implement the method to write memory
        framesFull = super().pass_frames(self.frames)
        pageFault = super().write_memory(page_number)
        if (pageFault): # page fault
            if (framesFull): # frames full
                for i in range(len(self.clock)): # find victim
                    if self.clock[i][1] == 0: # victim found
                        super().replace_victim(self.clock[i][0]) # replace victim
                        self.clock.remove(self.clock[i]) # remove victim from clock
                        break
                    else:
                        self.clock[i][1] = 0   # set use bit to 0 (in case of a second pass)
            self.clock.append([page_number, 1])
        else: # page hit
            for i in range(len(self.clock)): # find page
                if self.clock[i][0] == page_number: # page found
                    self.clock[i][1] = 1 # set use bit to 1
                    break


    def get_total_disk_reads(self):
        # TODO: Implement the method to get total disk reads
        return super().get_total_disk_reads()

    def get_total_disk_writes(self):
        # TODO: Implement the method to get total disk writes
        return super().get_total_disk_writes()

    def get_total_page_faults(self):
        # TODO: Implement the method to get total page faults
        return super().get_total_page_faults()
