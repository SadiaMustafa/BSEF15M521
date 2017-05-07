# SHORTEST JOB FIRST

n=int(0)
n=int(input("Enter the number of processes: "))
bur_time=[0]*n
arr_time=[0]*n
for i in range(n):
	arr_time[i]=int(input("Enter the arrival time for Process%d: "%(i+1)))
	bur_time[i]=int(input("Enter the burst time for Process%d: "%(i+1)))
print("Process\t Arrival_time\t Burst_time")
for i in range(n):
	print("P%d \t\t %d \t\t %d" %(i+1, arr_time[i], bur_time[i]))
fi_time=[0]*(n+1)
fi_time[0]=int(0)
indices=[0]*n
min_arr=arr_time[0]
i=int(0)
while i<n:
	j=int(0)
	min_bur=bur_time[0]
	min_index=int(0)
	while j<n:
		while min_bur==-1:
			min_index+=1
			min_bur=bur_time[min_index]
			#endwhile
		if arr_time[j]<=min_arr and bur_time[j]<min_bur and bur_time[j]!=-1:
			min_index=j
			min_bur=bur_time[j]
			#endif
		j+=1
		#endwhile
	fi_time[i+1]=fi_time[i]
	if arr_time[min_index]>fi_time[i+1]:
		while arr_time[min_index]!=fi_time[i+1]:
			fi_time[i+1]+=int(1)
			#endwhile
		#endif
	fi_time[i+1]+=bur_time[min_index]
	bur_time[min_index]=int(-1)
	indices[i]=min_index
	min_arr=fi_time[i+1]
	i+=1
	#endwhile
ta_time=[0]*n
for i in range(n):
	ta_time[indices[i]]=fi_time[i+1]-arr_time[indices[i]]
print("Process\t finish_time\t TurnAround_time")
for i in range(n):
	j=int(0)
	while indices[j]!=i:
		j+=1
	print("P%d \t\t %d \t\t %d" %(i+1, fi_time[j+1], ta_time[i]))

	
