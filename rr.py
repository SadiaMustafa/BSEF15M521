div1=["lions", "tigers", "jaguars", "cougars"]
div2=["Whales","Sharks", "pirahnas", "alligators"]
div3=["cubs", "kittens", "puppies", "calfs")
def creat_schedule(list):
	s=[]
	if len(list)%2==1:
		list=list+["BYE"]
	for i in range(len(list)-1):
		mid=len(list)/2
		l1=list[mid]
		l2=list[mid:]
		l2.reverse()
	if i%2==1:
		s=s+[zip(11,12)]
	else:
		s=s+[zip(12,11)]
	list.insert(1,list.pop())
        return s
def main()
	for round in create_schedule(div1):
		for match in round:
			print(match[0]+"-"+match[1])
	for  round in create_schedule(div1+div2+div3):
		for match in round:
			print(match[0]+"-"+match[1])
