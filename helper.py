import itertools
import math
from tabulate import tabulate
from collections import deque
from schemdraw.parsing import logicparse
from sympy import simplify_logic, And, Or, Not, symbols

# HERLPER FUNCTION FOR EXAM
def hex_to_decimal(hex_string):
    return str(int(hex_string, 16))

def hex_to_binary(hex_string):
    num_bits = len(hex_string) * 4
    return format(int(hex_string, 16), '0' + str(num_bits) + 'b')

def binary_to_decimal(binary_string):
    return str(int(binary_string, 2))

def hex_to_signed_magnitude_in_decimal(hex_string):
    # Convert hex to binary
    binary = bin(int(hex_string, 16))[2:].zfill(len(hex_string)*4)
    
    # Check the sign bit
    if binary[0] == '1':
        # If the sign bit is 1, the number is negative
        # Convert the rest of the binary string to its magnitude
        magnitude = binary[1:]
        return '-' + str(int(magnitude, 2))
    else:
        # If the sign bit is 0, the number is positive
        # Return the magnitude as is
        return str(int(binary[1:], 2))

def binary_to_ones_complement(binary_string):
    return ''.join('1' if bit == '0' else '0' for bit in binary_string)

def binary_to_twos_complement(binary_string):
    ones_complement = ''.join('1' if bit == '0' else '0' for bit in binary_string)
    ones_complement_int = int(ones_complement, 2)
    twos_complement_int = ones_complement_int + 1
    return format(twos_complement_int, '0' + str(len(binary_string)) + 'b')

def subtract_binary(bin1, bin2):
    # Convert binary to integer, interpreting as 2's complement if negative
    int1 = int(bin1, 2) if bin1[0] == '0' else -int(binary_to_twos_complement(bin1), 2)
    int2 = int(bin2, 2) if bin2[0] == '0' else -int(binary_to_twos_complement(bin2), 2)

    # Subtract the two integers
    result_int = int1 - int2

    return str(result_int)

def add_binary(bin1, bin2):
    # Convert binary to integer, interpreting as 2's complement if negative
    int1 = int(bin1, 2) if bin1[0] == '0' else -int(binary_to_twos_complement(bin1), 2)
    int2 = int(bin2, 2) if bin2[0] == '0' else -int(binary_to_twos_complement(bin2), 2)
    
    # Add the two integers
    result_int = int1 + int2
    return str(result_int)

def twos_complement_to_decimal(binary_string):
    if binary_string[0] == '0':
        return binary_to_decimal(binary_string)  # positive number
    else:
        # for negative number, perform two's complement and convert to decimal
        twos_complement = binary_to_twos_complement(binary_string)
        return str(-1 * int(twos_complement, 2))
    
def construct_truth_table_from_expression(expression, variables):
    # Generate all combinations of 1 and 0 for the number of variables
    combinations = list(itertools.product([0, 1], repeat=len(variables)))

    print('Truth Table:')
    # Print the variable names
    print(' | '.join(variables) + ' | ' + expression)

    for combination in combinations:
        # Create a dictionary mapping variable names to values
        variable_dict = dict(zip(variables, combination))

        # Convert 1 and 0 to True and False for eval
        variable_dict = {k: bool(v) for k, v in variable_dict.items()}

        # Evaluate the expression with the current variable values
        result = eval(expression, variable_dict)

        # Convert the result back to 1 or 0
        result = int(result)

        # Print the variable values and the result
        print(' | '.join(str(x) for x in combination) + ' | ' + str(result))
    
def construct_expression_from_table(truth_table):
    # Initialize the expression list
    expression = []

    # Get the output column name (the last key in the dictionary)
    output_column_name = list(truth_table[0].keys())[-1]

    # Create symbols for each variable
    variable_symbols = {key: symbols(key) for key in truth_table[0].keys() if key != output_column_name}

    # Iterate over each row in the truth table
    for row in truth_table:
        # Check if the output is 1 for the given row
        if row[output_column_name] == 1:
            # Construct the product term for the current row
            term = []
            for key, value in row.items():
                if key != output_column_name:
                    # Append NOT for 0 input values
                    term.append(Not(variable_symbols[key]) if value == 0 else variable_symbols[key])
            # Join the terms with AND and add to the expression list
            expression.append(And(*term))

    # Join the product terms with OR to form the final expression
    final_expression = Or(*expression)

    # Simplify the final expression
    simplified_expression = simplify_logic(final_expression)

    return str(simplified_expression)
        
def calculate_disk_capacity(platters, cylinders, sectors_per_track, bits_per_sector):
    # Calculate the capacity of the disk in bits
    capacity = platters * cylinders * sectors_per_track * bits_per_sector

    # Convert the capacity to various units
    capacity_in_kb = capacity / (1024)
    capacity_in_mb = capacity / (1024 * 1024)
    capacity_in_gb = capacity / (1024 * 1024 * 1024)
    capacity_in_tb = capacity / (1024 * 1024 * 1024 * 1024)

    return capacity_in_kb, capacity_in_mb, capacity_in_gb, capacity_in_tb

def calculate_page_table_size(virtual_address_space, page_size_kb, physical_memory_mb):
    # Convert sizes to bytes (1 KB = 2^10 bytes, 1 MB = 2^20 bytes (AKA page_size in kb and physical_memory in mb))
    page_size = page_size_kb * 2**10
    physical_memory = physical_memory_mb * 2**20

    # Calculate the number of entries in the page table
    num_entries = 2**virtual_address_space / page_size

    # Calculate the number of bits needed to address each byte in the physical memory
    physical_address_bits = int(math.log2(physical_memory))

    # Calculate the number of bits needed to identify the page number
    page_number_bits = physical_address_bits - int(math.log2(page_size))

    # Convert the numbers to a string with the 2^x format
    num_entries_str = f"2^{int(math.log2(num_entries))}"
    page_number_bits_str = str(page_number_bits)

    return num_entries_str, page_number_bits_str

def calculate_average_read_time(seek_time_ms, rotational_rate_rpm, sectors_per_track):
    # Convert rotational rate from revolutions per minute to revolutions per millisecond
    rotational_rate_rps = rotational_rate_rpm / 60 / 1000

    # Calculate average rotational latency (half a rotation)
    rotational_latency_ms = (1 / rotational_rate_rps) / 2

    # Calculate transfer time (time for one rotation divided by number of sectors per track)
    transfer_time_ms = (1 / rotational_rate_rps) / sectors_per_track

    # Sum the times to get the average read time
    average_read_time_ms = seek_time_ms + rotational_latency_ms + transfer_time_ms

    return average_read_time_ms

def calculate_memory_parameters(physical_address_space_mb, virtual_address_space_gb, page_size_kb):
    # Convert sizes to bytes
    physical_address_space = physical_address_space_mb * 2**20
    virtual_address_space = virtual_address_space_gb * 2**30
    page_size = page_size_kb * 2**10

    # Calculate the number of bits for each component
    offset_bits = int(math.log2(page_size))
    ppn_bits = int(math.log2(physical_address_space / page_size))
    vpn_bits = int(math.log2(virtual_address_space / page_size))
    page_table_entries = 2**vpn_bits

    return offset_bits, vpn_bits, ppn_bits, page_table_entries

def calculate_page_hits_and_misses_lru(page_reference_string, num_frames):
    memory = []
    page_hits = 0
    page_misses = 0

    for page in page_reference_string:
        if page in memory:
            page_hits += 1
            # Move the accessed page to the end of the memory list
            memory.remove(page)
            memory.append(page)
            hit_or_miss = "Hit"
        else:
            page_misses += 1
            if len(memory) == num_frames:
                # Remove the least recently used page
                memory.pop(0)
            memory.append(page)
            hit_or_miss = "Miss"

        # Print the current state of the memory
        print(f"Reference: {page}, {hit_or_miss}")
        print(tabulate([memory + [''] * (num_frames - len(memory))], tablefmt="fancy_grid"))

    return page_hits, page_misses

def calculate_average_turnaround_time_rr(processes, time_quantum):
    # Sort the processes by arrival time
    processes.sort(key=lambda x: x[1])

    queue = deque(processes)
    completion_times = [0] * len(processes)
    current_time = 0
    transitions = []

    while queue:
        pid, arrival_time, burst_time = queue.popleft()

        if burst_time > time_quantum:
            current_time += time_quantum
            queue.append((pid, arrival_time, burst_time - time_quantum))
        else:
            current_time += burst_time
            completion_times[pid - 1] = current_time

        transitions.append((f"P{pid}", current_time))

    # Calculate the turnaround times and the average turnaround time
    turnaround_times = [completion_times[i] - processes[i][1] for i in range(len(processes))]
    average_turnaround_time = sum(turnaround_times) / len(turnaround_times)

    # Prepare the data for the tables
    transitions_table_data = [(process, time) for process, time in transitions]

    print(tabulate(transitions_table_data, headers=["Process", "Time"], tablefmt="pretty"))
    # Print the turnaround times for each process
    for i in range(len(processes)):
        print(f"Turnaround time for P{i+1} = {turnaround_times[i]}")
        
    return average_turnaround_time

def get_page_size_bits(page_size):
    """
    Calculate the number of bits required to represent the page size.
    """
    page_size_bits = 0
    while 2 ** page_size_bits < page_size:
        page_size_bits += 1
    return page_size_bits

def binary_to_hex(binary_string):
    return hex(int(binary_string, 2))[2:]



def get_physical_address(virtual_address, page_table, page_size_bits):
    # Calculate the page size and mask
    page_size = 2 ** page_size_bits
    offset_mask = page_size - 1

    # Calculate the virtual page number and the offset
    vpn = virtual_address >> page_size_bits
    offset = virtual_address & offset_mask

    # Check if the page is valid
    try:
        valid_bit, ppn = page_table[vpn]
    except IndexError:
        return "The page is not resident in physical memory."

    if valid_bit == 0:
        return "The page is not resident in physical memory."
    else:
        # Calculate the physical address
        physical_address = (ppn << page_size_bits) | offset
        return f"The physical address is {hex(physical_address)}."
"""
# Section 1: Binary and Hexadecimal Operations
print(hex_to_decimal("A")) # Convert hexadecimal to decimal
print(hex_to_binary("A")) # Convert hexadecimal to binary
print(hex_to_signed_magnitude_in_decimal("A")) # Convert hexadecimal to signed magnitude
print(binary_to_ones_complement("1010")) # Convert binary to one's complement
print(binary_to_twos_complement("1010")) # Convert binary to two's complement
print(twos_complement_to_decimal(hex_to_binary("43"))) # Convert two's complement to decimal
print(subtract_binary("10101", "00111")) # Subtract binary numbers
print(add_binary( "10110101", "00111011")) # Add binary numbers
construct_truth_table_from_expression('((p and q) or (q and (not r)))', ['p', 'q', 'r']) # Generate truth table

truth_table = [
    {'A': 1, 'B': 1, 'OUTPUT': 0},
    {'A': 0, 'B': 1, 'OUTPUT': 1},
    {'A': 1, 'B': 0, 'OUTPUT': 1},
    {'A': 0, 'B': 0, 'OUTPUT': 0}
]
print(f"The logical expression from table is: {construct_expression_from_table(truth_table)}")

# Section 2: Disk Operations
# Calculate the capacity of a disk with 2 platters, 10,000 cylinders, 
# an average of 100 sectors per track, and 1,024 bits per sector
disk_capacity_kb, disk_capacity_mb, disk_capacity_gb, disk_capacity_tb = calculate_disk_capacity(2, 10000, 100, 1024)
print(f"The capacity of the disk is {disk_capacity_kb} KB, {disk_capacity_mb} MB, {disk_capacity_gb} GB, {disk_capacity_tb} TB.")

# Calculate the average read time for a disk with a rotational rate of 10,000 RPM,
# an average seek time of 8 ms, and an average of 500 sectors per track
average_read_time = calculate_average_read_time(8, 10000, 500)
print(f"The average time to read a random sector from disk is {average_read_time} ms.")

# Section 3: Memory Operations
# Calculate the memory parameters for a system with a 256 MB physical address space,
# a 4 GB virtual address space, and a 1 KiB page size
offset_bits, vpn_bits, ppn_bits, page_table_entries = calculate_memory_parameters(256, 4, 1)
print(f"Page offset: {offset_bits} bits, VPN: {vpn_bits} bits, PPN: {ppn_bits} bits, Page table entries: {page_table_entries}")

# Calculate the page hits and misses for the given page reference string and number of frames
page_hits, page_misses = calculate_page_hits_and_misses_lru([2, 3, 4, 2, 1, 3, 7, 5, 4, 3, 2, 3, 1], 4)
print(f"Page hits: {page_hits}, Page misses: {page_misses}")

# calculate_page_table_size 
virtual_address_space = 30  # 30-bit virtual address space
page_size_kb = 4  # 4KB page size
physical_memory_mb = 128  # 128MB physical memory
#Needs pagesize in KB and physical memory in MB
print(calculate_page_table_size(virtual_address_space, page_size_kb, physical_memory_mb))

# Section 4: Process Scheduling
# Calculate the average turnaround time for the given set of processes and time quantum
# The tuple (1,0,5) means that process 1 arrives at time 0 and has a burst time of 5 med quantumtime = 2
average_turnaround_time = calculate_average_turnaround_time_rr([(1, 0, 5), (2, 1, 3), (3, 2, 1), (4, 3, 2), (5, 4, 3)], 2)
print(f"The average turnaround time is {average_turnaround_time}.")

# Section 5: Address Translation
# Calculate the physical address for the given virtual address and page table
# Define the page table
page_table = [
    (0, 7),
    (1, 9),
    (0, 3),
    (1, 2),
]
# Define the virtual address
virtual_address = 0xE72
#define the page size based on assignment
page_size = 1024
page_size_bits = get_page_size_bits(page_size)
print(get_physical_address(virtual_address, page_table, page_size_bits))

#Draw a logic circuit based on expression and generate an expression from truthtable for example purposes
truth_table = [
    {'A': 1, 'B': 1, 'OUTPUT': 1},
    {'A': 0, 'B': 1, 'OUTPUT': 1},
    {'A': 1, 'B': 0, 'OUTPUT': 1},
    {'A': 0, 'B': 0, 'OUTPUT': 0}
]
drawing = logicparse(construct_expression_from_table(truth_table))
drawing.draw()

drawing = logicparse('(E and D) or (not E and Q)')
drawing.draw()
"""
print(calculate_page_table_size(32, 4, 64))
print(hex_to_binary("E72"))
print(hex_to_binary("A72"))
print(binary_to_hex("011001110010"))


print("EXAMTIME BABY")

