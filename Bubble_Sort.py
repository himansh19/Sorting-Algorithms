
# Bubble Sort Code 

def bubbleSort(arr):
    n = len(arr)
    swapped = False
    # Traverse through all array elements
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
         
        if not swapped:
            return


# Analysis of Bubble Sort

time = []

def test_caseb(num):
    A = []
    for i in range(num):
        x = random.randint(1, 2000)
        A.append(x)

    start = timeit.default_timer()
    bubbleSort(A)
    end = timeit.default_timer()

    time.append(end-start)
    
test_caseb(50); test_caseb(100); test_caseb(500)
test_caseb(1000); test_caseb(2000); test_caseb(4000)
test_caseb(6000);test_caseb(8000); test_caseb(10000)


# Plot Graph

x = np.array([50, 100, 500,1000,2000,4000,6000,8000,10000])
y = np.array(time)

plt.xlabel('No. of elements')
plt.ylabel('Execution time of Algorithm')
plt.title("Analysis of Bubble Sort")

plt.scatter(x, y)
plt.show()
