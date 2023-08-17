
# Insertion Sort Code

def insertionSort(arr):
 
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key


# Analysis of Insertion Code

time = []

def test_casei(num):
    A = []
    for i in range(num):
        x = random.randint(1, 2000)
        A.append(x)

    start = timeit.default_timer()
    insertionSort(A)
    end = timeit.default_timer()

    time.append(end-start)
    
test_casei(50); test_casei(100); test_casei(500)
test_casei(1000); test_casei(2000); test_casei(4000)
test_casei(6000);test_casei(8000); test_casei(10000)


# Plot graph

x = np.array([50, 100, 500,1000,2000,4000,6000,8000,10000])
y = np.array(time)

plt.xlabel('No. of elements')
plt.ylabel('Execution time of Algorithm')
plt.title("Analysis of Insertion Sort")

plt.scatter(x, y)
plt.show()
