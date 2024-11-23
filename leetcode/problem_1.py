import datetime
import random
import time

def main():
    # Create an XML file to store the results
    file = open("ListAccessTiming.xml", "w")
    file.write('<?xml version="1.0" encoding="UTF-8" standalone="no" ?>\n')
    file.write('<Plot title="Average List Element Access Time">\n')

    # Define the range of list sizes (from 1000 to 200,000)
    xmin = 1000
    xmax = 200000

    # Initialize lists to store list sizes and access times
    xList = []
    yList = []

    # Loop through list sizes from xmin to xmax with steps of 1000
    for x in range(xmin, xmax + 1, 1000):
        xList.append(x)  # Add the current list size to xList
        prod = 1  # Dummy product for validation

        # Create a list of size `x` filled with zeros
        lst = [0] * x

        # Sleep to allow memory allocation to settle
        time.sleep(1)

        # Measure the time taken for 1000 random accesses
        start_time = datetime.datetime.now()
        for _ in range(1000):
            index = random.randint(0, x - 1)  # Random index in the list
            val = lst[index]  # Retrieve the value at the index
            prod *= val  # Dummy operation to ensure value retrieval
        end_time = datetime.datetime.now()

        # Calculate the time difference and convert to milliseconds
        deltaT = (end_time - start_time).total_seconds() * 1000
        yList.append(deltaT)  # Store the access time in yList

    # Write the X and Y axis configuration in XML
    file.write('  <Axes>\n')
    file.write(f'    <XAxis min="{xmin}" max="{xmax}">List Size</XAxis>\n')
    file.write(f'    <YAxis min="{min(yList)}" max="{60}">Milliseconds</YAxis>\n')
    file.write('  </Axes>\n')

    # Write the average access time vs. list size sequence in XML
    file.write('  <Sequence title="Average Access Time vs List Size" color="red">\n')
    for i in range(len(xList)):
        file.write(f'    <DataPoint x="{xList[i]}" y="{yList[i]}"/>\n')
    file.write('  </Sequence>\n')

    # Test random access across a large list (200,000 elements)
    lst = [0] * 200000  # Reset the list to size 200,000
    yList = [0] * 200000  # Reset the timing list

    # Allow system to stabilize
    time.sleep(2)

    # Measure access time for 100 random locations
    for _ in range(100):
        start_time = datetime.datetime.now()
        index = random.randint(0, 200000 - 1)  # Random index
        lst[index] += 1  # Increment the value at the index
        end_time = datetime.datetime.now()

        # Record the access time in microseconds
        deltaT = (end_time - start_time).total_seconds() * 1000000
        yList[index] += deltaT

    # Write the access time distribution sequence in XML
    file.write('  <Sequence title="Access Time Distribution" color="blue">\n')
    for i in range(len(lst)):
        if lst[i] > 0:
            avg_time = yList[i] / lst[i]  # Calculate average time for this index
            file.write(f'    <DataPoint x="{i}" y="{avg_time}"/>\n')
    file.write('  </Sequence>\n')

    # Close the XML plot
    file.write('</Plot>\n')
    file.close()  # Close the XML file
    file.write('  </Sequence>\n')
    file.write('</Plot>\n')
    file.close()
if __name__ == "__main__":
    main()
