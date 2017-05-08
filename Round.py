# ROUND BOBIN SCHEDULING ALGORITHM

#n=int(0)
#n=int(input("Enter the number of processes: "))
bur_time=[0]*6
arr_time=[0]*6
for i in range(6):
	arr_time[i]=int(input("Enter the arrival time for Process%d: "%(i+1)))
	bur_time[i]=int(input("Enter the burst time for Process%d: "%(i+1)))
print("Process\t Arrival_time\t Burst_time")
for i in range(6):
	print("P%d \t\t %d \t\t %d" %(i+1, arr_time[i], bur_time[i]))
bur2_time=[0]*6
arr2_time=[0]*6
rem_time=[0]*6
fi_time=[0]*6
for i in range(6):
	arr2_time[i]=arr_time[i]
	bur2_time[i]=bur_time[i]
	rem_time[i]=int(-1)
count=int(0)
while count!=6:
	count=0
	for i in range(6):
		if bur2_time==-1:
			count+=1
	min_index=int(0)
	min_arr=arr2_time[0]
	j=int(0)
	while j<6:
		while bur2_time[min_index]==-1:
			min_index+=1
			min_arr=arr2_time[min_index]
			#endwhile
		if arr2_time[j]<=min_arr and rem_time[j]==(-1) and bur2_time[j]!=-1:
			min_index=j   #new process
			min_arr=arr2_time[j]
		elif arr2_time[j]<min_arr and bur2_time[j]!=-1 and rem_time[j]!=(0) and rem_time[j]!=(-1):
			min_index=j   #waiting process
			min_arr=arr2_time[j]
		elif arr2_time[j]<min_arr and bur2_time[j]!=-1:
			min_index=j   #running process
			min_arr=arr2_time[j]
			#endif
		j+=1
		#endwhile
	rem_time[min_index]=int(0)
	for k in range(3):
		bur2_time[min_index]-=1
		for l in range(6):
			if arr2_time[l]<=fi_time[min_index] and bur2_time[l]!=-1:
				fi_time[l]+=1
		if (min_index+1)%2==0 and (bur_time[min_index]-bur2_time[min_index])%2==0:
			rem_time[min_index]=int(3-k)
			arr2_time[min_index]+=(k+1)
			arr2_time[min_index]+=5
			k=3
		if (min_index+1)%2!=0 and k==2:
			arr2_time[min_index]+=(k+1)
			k=3
		if bur2_time[min_index]==0: 
			k=3
			bur2_time[min_index]=int(-1)	
ta_time=[0]*6
wait_time=[0]*6
for i in range(6):
	ta_time[i]=fi_time[i]-arr_time[i]
	wait_time[i]=fi_time[i]-arr_time[i]-bur_time[i]
print("Process \t fi_time \t    Turn_time \t   wait_time")
for i in range(6):
	print("p%d \t\t %d \t\t %d \t\t %d" %(i+1, fi_time[i], ta_time[i], wait_time[i]))
