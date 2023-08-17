
# Bubble Sort Code

def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1

def quick_sort(array, low, high):   # Function to perform quicksort
    if low < high:
        pi = partition(array, low, high)

        quick_sort(array, low, pi - 1)
        quick_sort(array, pi + 1, high)



# Bubble Sort Analysis

time = []

def test_caseq(num):
    A = []
    for i in range(num):
        x = random.randint(1, 2000)
        A.append(x)

    start = timeit.default_timer()
    quick_sort(A, 0, len(A)-1)
    end = timeit.default_timer()

    time.append(end-start)
    
test_caseq(100); test_caseq(1000); test_caseq(2000); test_caseq(4000)
test_caseq(6000);test_caseq(8000); test_caseq(9000);test_caseq(10000)


# Plot Graph

x = np.array([100,1000,2000,4000,6000,8000,9000,10000])
y = np.array(time)

plt.xlabel('No. of elements')
plt.ylabel('Execution time of Algorithm')
plt.title("Analysis of Quick Sort")

plt.plot(x, y, 'o')
for i_x, i_y in zip(x, y):
    plt.text(i_x, i_y ,'  ({},{})'.format(i_x, round(i_y,4)))
plt.show()
