from mmu import MMU

class LruMMU(MMU):
    def __init__(self, frames):
        self.frames = frames
        self.lruList = [] #list to hold use order of pages (least recently used will be at front)

    def set_debug(self):
        # TODO: Implement the method to set debug mode
        pass

    def reset_debug(self):
        # TODO: Implement the method to reset debug mode
        pass

    def read_memory(self, page_number):
        framesFull = super().pass_frames(self.frames) #check if frames are full (will return 1 if full)
        pageFault = super().read_memory(page_number) #perform memory read. Will return 1 if page fault occurs

        if pageFault: #page isn't in physical memory so needs to be brought in
            if framesFull: #all frames are full so we need to replace a victim page
                super().replace_victim(self.lruList.pop(0)) #least recently used page will be the victim (i.e. the page at the front of lruList)
            self.lruList.append(page_number) #since page wasn't in physical memory, just append page to lruList (will be at the end i.e. most recently acessed)
        
        if not pageFault: #No page fault so the page is in memory, just move it to the end of lruList
            self.lruList.append(self.lruList.pop(self.lruList.index(page_number))) #pop page from lruList and append it to the end (as it is the most recently acessed page)

    def write_memory(self, page_number):
        framesFull = super().pass_frames(self.frames) #check if frames are full (will return 1 if full)
        pageFault = super().write_memory(page_number) #perform memory write. Will return 1 if page fault occurs

        if pageFault: #page isn't in physical memory so needs to be brought in
            if framesFull: #all frames are full so we need to replace a victim page
                super().replace_victim(self.lruList.pop(0)) #least recently used page will be the victim (i.e. the page at the front of lruList)
            self.lruList.append(page_number) #since page wasn't in physical memory, just append page to lruList (will be at the end i.e. most recently acessed)
        
        if not pageFault: #No page fault so the page is in memory, just move it to the end of lruList
            self.lruList.append(self.lruList.pop(self.lruList.index(page_number))) #pop page from lruList and append it to the end (as it is the most recently acessed page)

    def get_total_disk_reads(self):
        return super().get_total_disk_reads() #call mmu function to get disk reads

    def get_total_disk_writes(self):
        return super().get_total_disk_writes() #call mmu function to get disk writes

    def get_total_page_faults(self):
        return super().get_total_page_faults() #call mmu function to get page faults
