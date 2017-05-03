bur_time=[0]*5
arr_time=[0]*5
for i in range(5):
	bur_time[i]=int(input("Enter the burst time for process%d: " %(i+1)))
	arr_time[i]=int(input("Enter the arrival time for process%d: "%(i+1)))
dic_bur={1:bur_time[0], 2:bur_time[1], 3:bur_time[2], 4:bur_time[3], 5:bur_time[4]}
dic_arr={1:arr_time[0], 2:arr_time[1], 3:arr_time[2], 4:arr_time[3], 5:bur_time[4]}
fi_time=[0]*6
fi_time[0]=int(0)
min_arr=arr_time[0]
min_bur=bur_time[0]
min_index=int(0)
indices=[0]*5
i=int(0)
while i<5:
	j=int(0)
	while j<5:
		if min_arr==0:
			while min_arr==0:
				min_arr=arr_time[index+1]
				min_index+=1
		if (bur_time[j]<=min_bur) and (arr_time[j]<=min_arr) and (bur_time[j]!=0):
			min_arr=arr_time[j]
			min_bur=bur_time[j]
			min_index=j
		j+=1
	indices[i]=min_index
	fi_time[i+1]=fi_time[i]
	if min_arr>fi_time[i+1]:
		while min_arr!=fi_time[i+1]:
			fi_time[i+1]+=int(1)
	fi_time[i+1]+=bur_time[min_index]
	min_bur=fi_time[i+1]
	bur_time[min_index]=int(0)
	min_arr=arr_time[0]
	min_index=0
	i+=int(1)
ta_time=[0]*5
for i in range(5):
	ta_time[indices[i]]=(fi_time[i+1]-arr_time[indices[i]])
print("Burst Time:")
print(dic_bur)
print("Arrival Time:")
print(dic_arr)
print("Turnaround Time")
print(ta_time)
