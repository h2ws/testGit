def quickSort(arr,begin,end):
    if(begin >= end):
        return
    else:
        x = arr[begin]
        p1,p2 = begin,end
        dr = True
        while(i<j):
          if(dr):
            i = p2
            while(p1<i):
                if(arr[i]<x):
                    arr[p1] = arr[i]
                    p1 += 1
                    p2 = i
                    
                i -= 1
            else:
                p2 = p1

        else:

  
