#!/bin/bash

#!/bin/bash

# Check if at least two arguments are provided
if [ $# -lt 6 ]; then
    echo "Usage: $0 <initial frame number> <final frame number> <file to store results> <trace filename> <replacement policy>"
    exit 1
fi

# Assign command-line arguments to variables
arg1="$1"
arg2="$2"
arg3="$3"

# Capture the file name from the command line argument
filename="$4"
tracefile="$5"
replacement="$6"



# Check if the file exists
if [ -e "$filename" ]; then
    # File exists, you can proceed to write to it
    echo "File '$filename' exists."
    exit 1
else
    # File does not exist, you can create it and then write to it
    echo "File '$filename' does not exist. Creating it..."
    touch "$filename"
fi

# Write some content to the file (you can choose either >> or >)




# Generate numbers from arg1 to arg2 and save them to numbers.csv
for i in $(seq "$arg1" "$arg3" "$arg2"); do
	

	# Run your Python script and capture its output
	output=$(python memsim.py $tracefile $i $replacement quiet)

	# Iterate over each line of output
	while IFS= read -r line; do
    		# Use grep to extract the number from each line
    		number=$(echo "$line" | grep -oE '[0-9]+(\.[0-9]+)?')

    		# Check if a number was found on this line
    		if [[ -n "$number" ]]; then
        		echo -n "$number," >> $filename
        		# You can store or process the number as needed here
		
		fi
	done <<< "$output"

    	echo "" >> "$filename"
done

# Remove the trailing comm




