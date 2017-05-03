n=int(0)
n=int(input("Enter Total number of processes: "))
bt=[0]*n
p=[0]*n
fi=[0]*n
tat=[0]*n
pr=[0]*n
total=int(0)
for i in range(n):
	print("\nProcess%d: "%(i+1))
	bt[i]=int(input("Burst time: "))
	pr[i]=int(input("Priority: "))
for i in range(n):
	pos=int(i)
	for j in range(n):
		if pr[j]<pr[pos]:
			pos=j
	temp=int(pr[i])
	pr[i]=pr[pos]
	pr[pos]=temp
	temp=bt[i]
	bt[i]=bt[pos]
	bt[pos]=temp
	temp=p[i]
	p[i]=p[pos]
	p[pos]=temp
fi[0]=int(0)
for i in range(n):
	fi[i]=int(0)
	for j in range(n):
		fi[i]+=bt[j]
	total+=fi[i]
total=int(0)
print("\nProcess \t Burst time \t Finish time \t turnaround time")
for i in range(n):
	tat[i]=bt[i]+fi[i]
	total+=tat[i]
	print("\nP[%d] \t\t %d \t\t %d \t\t\t %d" %(p[i], bt[i], fi[i], tat[i]))
avg_tat=int(total/n)
print("\n\n Average TurnAround Time = %d" %avg_tat)	

