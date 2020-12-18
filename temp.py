import random
import timeit
import matplotlib.pyplot as plt

arrnk = []
arrtime = []

def bucket_sort(n,k):
    
    start =  timeit.default_timer()
    input_list = []
    for i in range(0,n):
        value = random.randint(0,k-1)
        input_list.append(value)
    print("Before sorting")
    print(input_list)
    buckets_list= []
    for x in range(len(input_list)):
        buckets_list.append([]) 

    for i in range(len(input_list)):
        j = int (input_list[i] / n)
        if j != len (input_list):
            buckets_list[j].append(input_list[i])
        else:
            buckets_list[len(input_list) - 1].append(input_list[i])
    
    #alternative sort usage
    # sorted(buckets_list)

    for z in range(len(input_list)):
        insertion_sort(buckets_list[z])
            
    final_output = []
    for x in range(len (input_list)):
        final_output = final_output + buckets_list[x]  
        
    end = timeit.default_timer()
    arrnk.append(n+k)
    arrtime.append((end-start)*10)
    print("elements sorted by bucketsort in ", (end-start)*10) 
    return final_output

def insertion_sort(bucket):
    for i in range (1, len (bucket)):
        var = bucket[i]
        j = i - 1
        while (j >= 0 and var < bucket[j]):
            bucket[j + 1] = bucket[j]
            j = j - 1
        bucket[j + 1] = var
        

for k in range(10,20):
    sorted_list = bucket_sort(5,k)
    print('SORTED LIST:')
    print(sorted_list)
    print("")

plt.figure()
plt.plot(arrtime,arrnk)
plt.show


