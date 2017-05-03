n=int(0)
n=int(input("Enter the number of processes: "))
bur_time=[0]*n
arr_time=[0]*n
for i in range(n):
	bur_time[i]=int(input("Enter burst time for process%d: " %(i+1)))
	arr_time[i]=int(input("Enter arrival time for process%d " %(i+1)))
fin_time=[0]*n
fin_time[0]=(arr_time[0]+bur_time[0])
num=int(1)
while num<n:
	fin_time[num]=fin_time[num-1]
	if arr_time[num]>fin_time[num]:
		while arr_time[num]>fin_time[num]:
			fin_time[num]+=int(1)
	fin_time[num]+=bur_time[num]
	num+=1
ta_time=[0]*n
for i in range(n):
	ta_time[i]=(fin_time[i]-arr_time[i])
for i in range(n):
	print("PROCESS\t   ARRIVAL_TIME\t   BURST_TIME\t   TURNAROUND_TIME ")
	print("P%d \t\t %d \t\t %d \t\t %d " %(i+1, arr_time[i], bur_time[i], ta_time[i]))
