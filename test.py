from mmu import MMU
from clockmmu import ClockMMU


testMemory = ClockMMU(3)

testMemory.read_memory(1)
print(testMemory.get_total_disk_reads())
testMemory.read_memory(2)
print(testMemory.get_total_disk_reads())
testMemory.read_memory(2)
print(testMemory.get_total_disk_reads())
testMemory.read_memory(3)
print(testMemory.get_total_disk_reads())
testMemory.write_memory(2)
print(testMemory.get_total_disk_reads())
testMemory.write_memory(3)
print(testMemory.get_total_disk_reads())
print(testMemory.get_total_disk_writes())
print(testMemory.get_total_page_faults())
testMemory.read_memory(5)
testMemory.read_memory(6)
testMemory.read_memory(7)
print(testMemory.get_total_disk_reads())
print(testMemory.MMUlist)
print(testMemory.clock)

