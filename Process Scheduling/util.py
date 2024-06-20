def read_non_empty_lines(filename):
  """
  Reads lines from a file, excluding blank lines and comments (lines starting with "#").

  Args:
      filename: The path to the file to read.

  Returns:
      A list of non-empty lines (excluding blank lines and comments).
  """
  data = []
  with open(filename, 'r') as file:
    for line in file:
      line = line.strip()  # Remove leading/trailing whitespace
      if line and not line.startswith('#'):  # Check if not empty and not a comment
        data.append(line)
  return data

# Example usage
filename = "config.txt"
non_empty_lines = read_non_empty_lines(filename)

print("This is non-empty lines from", filename)
for line in non_empty_lines:
  print(line)

def split_line_into_tokens(line, delimiter=" "):
  """
  Splits a line into a list of tokens based on a specified delimiter.

  Args:
      line: The string to split.
      delimiter: The delimiter to use for splitting (default is space " ").

  Returns:
      A list of tokens from the line.
  """
  return line.split(delimiter)

# Example usage
#line = "P1  0  5"
data=read_non_empty_lines(filename)
tokens = []
for i in range (len(data)) :
  line=data[i]
  tokens.append(split_line_into_tokens(line))

print("Tokens:", tokens)

def convert_tokens_to_data(tokens):
  """
  Converts a list of tokens to appropriate data types for process information.

  Args:
      tokens: A list of tokens extracted from a line in the configuration file.

  Returns:
      A tuple containing process information (name, arrival_time, cpu_burst_time).
  """
  try:
    name = tokens[0]
    arrival_time = int(tokens[1])
    cpu_burst_time = int(tokens[2])
    return name, arrival_time, cpu_burst_time
  except (IndexError, ValueError):
    # Handle potential errors: missing tokens or invalid data types
    print(f"Error processing line: {''.join(tokens)}")
    return None, None, None  # Return dummy values on error

# Example usage
process_info_list =[]
for j in tokens :
  process_info_list.append(convert_tokens_to_data(j))

for i in process_info_list :
  if i :
    name, arrival_time, cpu_burst_time = i
    print("Process:", name, ", Arrival Time:", arrival_time, ", CPU Burst:", cpu_burst_time)

 #create process :
 
class Process:
    def __init__(self, name, arrival_time, cpu_burst):
        self.name = name
        self.arrival_time = arrival_time
        self.cpu_burst = cpu_burst
        self.waiting_time = 0
        self.turnaround_time = 0
        self.remaining_burst = cpu_burst


def create_process_and_add_to_list(tokens):
  """
  Creates a Process object from tokens and adds it to a list.

  Args:
      tokens: A list of tokens representing process information.

  Returns:
      A Process object (or None on error).
  """
  process_info = convert_tokens_to_data(tokens)
  if process_info:
    name, arrival_time, cpu_burst_time = process_info
    process = Process(name, arrival_time, cpu_burst_time)
    return process
  else:
    return None

def read_processes_from_file(filename):
  """
  Reads process information from a file and creates a list of Process objects.

  Args:
      filename: The path to the configuration file.

  Returns:
      A list of Process objects (or None on errors).
  """
  processes = []
  non_empty_lines = read_non_empty_lines(filename)
  for line in non_empty_lines:
    tokens = split_line_into_tokens(line)
    process = create_process_and_add_to_list(tokens)
    if process:
      processes.append(process)
    else:
      print(f"Error processing line: {line}")
  return processes

# Example usage
filename = "config.txt"
processes = read_processes_from_file(filename)

if processes:
  print("List of Processes:")
  for process in processes:
    print(f"Process: {process.name}, Arrival Time: {process.arrival_time}, CPU Burst: {process.cpu_burst}")
else:
  print("Error reading processes from file!")
