
# Radix Sort Code

# Using counting sort to sort the elements in the basis of significant places
def countingSort(array, place):
    size = len(array)
    output = [0] * size
    count = [0] * 10
    # Calculate count of elements
    for i in range(0, size):
        index = array[i] // place
        count[index % 10] += 1
    # Calculate cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1
    for i in range(0, size):
        array[i] = output[i]

def radixSort(array):
    
    max_element = max(array)
    # Apply counting sort to sort elements based on place value.
    place = 1
    while max_element // place > 0:
        countingSort(array, place)
        place *= 10


# Analysis of Radix Sort

time = []

def test_caser(num):
    A = []
    for i in range(num):
        x = random.randint(1, 2000)
        A.append(x)

    start = timeit.default_timer()
    radixSort(A)
    end = timeit.default_timer()

    time.append(end-start)
    
test_caser(50); test_caser(100); test_caser(500)
test_caser(1000); test_caser(2000); test_caser(4000)
test_caser(6000);test_caser(8000); test_caser(10000)


# Plot Graph

x = np.array([50, 100, 500,1000,2000,4000,6000,8000,10000])
y = np.array(time)

plt.xlabel('No. of elements')
plt.ylabel('Execution time of Algorithm')
plt.title("Analysis of Radix Sort")

plt.scatter(x, y)
plt.show()
