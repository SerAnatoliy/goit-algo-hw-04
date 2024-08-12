
import random

def generate_datasets():
    sizes = [10, 100, 1000]
    datasets = {
        'RANDOM': [],
        'SORTED': [],
        'REVERSE_SORTED': [],
        'NEARLY_SORTED': []
    }
    
    for size in sizes:
        # Generate random data
        random_data = [random.randint(0, size) for _ in range(size)]
        datasets['RANDOM'].append(random_data)
        
        # Generate sorted data
        sorted_data = sorted(random_data)
        datasets['SORTED'].append(sorted_data)
        
        # Generate reverse sorted data
        reverse_sorted_data = sorted(random_data, reverse=True)
        datasets['REVERSE_SORTED'].append(reverse_sorted_data)
        
        # Generate nearly sorted data (sorted with a few swaps)
        nearly_sorted_data = sorted_data[:]
        for _ in range(int(0.1 * size)):  # Swap 10% of the data to create nearly sorted arrays
            i, j = random.randint(0, size - 1), random.randint(0, size - 1)
            nearly_sorted_data[i], nearly_sorted_data[j] = nearly_sorted_data[j], nearly_sorted_data[i]
        datasets['NEARLY_SORTED'].append(nearly_sorted_data)

    return datasets

def print_datasets(datasets):
    for data_type, data_arrays in datasets.items():
        print(f"Data Type: {data_type}")
        for i, data in enumerate(data_arrays):
            print(f"  Size {len(data)}: {data[:10]}...")  # Print only the first 10 elements for brevity
        print()  # Adds a newline for better readability between data types