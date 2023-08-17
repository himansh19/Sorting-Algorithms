
# Merge Sort Code

def mergeSort(array):
    if len(array) > 1:
        #  r is the point where the array is divided into two subarrays
        r = len(array)//2
        L = array[:r]
        M = array[r:]
        # Sort the two halves
        mergeSort(L)
        mergeSort(M)

        i = j = k = 0
        # Until we reach either end of either L or M, pick larger among elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1
        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1

# Analysis of Merge Sort

time = []

def test_casem(num):
    A = []
    for i in range(num):
        x = random.randint(1, 2000)
        A.append(x)

    start = timeit.default_timer()
    mergeSort(A)
    end = timeit.default_timer()

    time.append(end-start)
    
test_casem(50); test_casem(100); test_casem(500)
test_casem(1000); test_casem(2000); test_casem(4000)
test_casem(6000);test_casem(8000); test_casem(10000)


# Plot Graph

x = np.array([50, 100, 500,1000,2000,4000,6000,8000,10000])
y = np.array(time)

plt.xlabel('No. of elements')
plt.ylabel('Execution time of Algorithm')
plt.title("Analysis of Merge Sort")

plt.scatter(x, y)
plt.show()

