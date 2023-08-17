
# Heap Sort Code

def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2
    # See if left child of root exists and is greater than root
    if l < n and arr[i] < arr[l]:
        largest = l
    # See if right child of root exists and is greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r
    # Change root, if needed
    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i])  # swap
 
        heapify(arr, n, largest)
 
def heapSort(arr):
    n = len(arr)
 # Build a maxheap. Since last parent will be at ((n//2)-1) we can start at that location.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
 
    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])  # swap
        heapify(arr, i, 0)


# Analysis of Heap Sort

time = []

def test_caseh(num):
    A = []
    for i in range(num):
        x = random.randint(1, 2000)
        A.append(x)

    start = timeit.default_timer()
    heapSort(A)
    end = timeit.default_timer()

    time.append(end-start)
    
test_caseh(50); test_caseh(100); test_caseh(500)
test_caseh(1000); test_caseh(2000); test_caseh(4000)
test_caseh(6000);test_caseh(8000); test_caseh(10000)

# Plot Graph

x = np.array([50, 100, 500,1000,2000,4000,6000,8000,10000])
y = np.array(time)

plt.xlabel('No. of elements')
plt.ylabel('Execution time of Algorithm')
plt.title("Analysis of Heap Sort")

plt.scatter(x, y)
plt.show()
