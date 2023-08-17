
# Selection Sort Code

def selectionSort(array, size):
   
    for step in range(size):
        min_idx = step
        for i in range(step + 1, size):
            # to sort in descending order, change > to < in this line select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i
        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])


# Analysis of Selection Sort

time = []

def test_cases(num):
    A = []
    for i in range(num):
        x = random.randint(1, 2000)
        A.append(x)

    start = timeit.default_timer()
    selectionSort(A,num)
    end = timeit.default_timer()

    time.append(end-start)
    
test_cases(50); test_cases(100); test_cases(500)
test_cases(1000); test_cases(2000); test_cases(4000)
test_cases(6000);test_cases(8000); test_cases(10000)


# Plot Graph

x = np.array([50, 100, 500,1000,2000,4000,6000,8000,10000])
y = np.array(time)

plt.xlabel('No. of elements')
plt.ylabel('Execution time of Algorithm')
plt.title("Analysis of Selection Sort")

plt.scatter(x, y)
plt.show()
