from mmu import MMU

testMemory = MMU()

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
testMemory.replace_victim(1)

print(testMemory.get_total_disk_reads())
print(testMemory.MMUlist)

