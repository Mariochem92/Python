#This script is suitable to find 1D intervals of a given variable value. Also the min_span parameter acts like a filter in order to get rid of the smallest ranges, 
#which could be transitory or noise stemmed. Whereas the cutoff is enforced by a rcutoff parameter. Here we are looking for intervals where the variable is smaller
#than 1.15. The file.dat is characterized by two columns: time and physical variable of interest (radius).
import numpy as np
def main():
    fname='file.dat'
    min_span=10000
    rcutoff=1.15
    i=0
    num_lines = sum(1 for line in open(fname))
    print(int(num_lines/3))
    vec=np.zeros((int(num_lines/3),2))
    a=0
    with open(fname,'r') as f:
        for line in f:
            if float(line) < rcutoff:
                vec[a][0]=i
                vec[a][1]=float(line)
                a+=1
            i+=1
    i=i-1
    vec=vec[:a,:]
    print(vec.shape, a,"last element",vec[-1,0],vec[-1,1])
    count=0
    while (count < (a-1)):
        range_span=0
        range_start=count
        for j in range(count,a-1):
            if (vec[j+1,0]==vec[j,0]+1):
                #print('cons')
                count+=1
                range_span+=1
            else:
                count+=1
                if range_span >= min_span:
                    print('range span: ',range_span/1000,'[ns]','range starts at: ', vec[range_start,0]/1000,'[ns]', 'range ends at: ', vec[count,0]/1000, '[ns]' )
                break

main()
