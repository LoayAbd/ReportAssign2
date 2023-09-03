from mmu import MMU
import random

class RandMMU(MMU):
    def __init__(self, frames):
        # TODO: Constructor logic for RandMMU
        self.frames = frames
        self.rand = []
        pass

    def set_debug(self):
        # TODO: Implement the method to set debug mode
        pass

    def reset_debug(self):
        # TODO: Implement the method to reset debug mode
        pass

    def read_memory(self, page_number):
        # TODO: Implement the method to read memory
        full = super().pass_frames(self.frames)
        fault = super().read_memory(page_number)

        # print("R: ", page_number)
        # print(super().MMUlist)
        if (fault):
            if (full):
                choice = random.choice(self.rand)
                super().replace_victim(choice)
                self.rand.remove(choice)
                
            for i in self.rand:
                if i == page_number:
                    return
            self.rand.append(page_number)
        else:
            for i in self.rand:
                if i == page_number:
                    return
            self.rand.append(page_number)

        pass

    def write_memory(self, page_number):
        # TODO: Implement the method to write memory
        full = super().pass_frames(self.frames)
        fault = super().write_memory(page_number)

        # print("W: ", page_number)
        # print(super().MMUlist)
        if (fault):
            if (full):
                choice = random.choice(self.rand)
                super().replace_victim(choice)
                self.rand.remove(choice)

            for i in self.rand:
                if i == page_number:
                    return
            self.rand.append(page_number)
        else:
            for i in self.rand:
                if i == page_number:
                    return
            self.rand.append(page_number)
        pass

    def get_total_disk_reads(self):
        # TODO: Implement the method to get total disk reads
        return super().get_total_disk_reads()

    def get_total_disk_writes(self):
        # TODO: Implement the method to get total disk writes
        return super().get_total_disk_writes()

    def get_total_page_faults(self):
        # TODO: Implement the method to get total page faults
        return super().get_total_page_faults()
