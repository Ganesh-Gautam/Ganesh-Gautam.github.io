class Set:
    def __init__(self,SET,other_SET):
        self.s=SET
        self.other_SET=other_SET
    def ismember(self,SET,N):
        if N in SET:
            return True
        else:
            return False
    def subset(self,SET,other_SET):
        s=True
        for i in SET:
            if i not in other_SET:
                s= False
        if s== False:
            return False
        else:
            return True
    def union(self,s1,s2):
        s3=[]
        for i in s1:
            if i not in s3:
                s3.append(i)
        for i in s2:
            if i not in s3:
                s3.append(i)
        return(s3)
    def intersection(self,s1,s2):
        s3=[]
        for j in s1:
            if j in s1 and j in s2:
                s3.append(j)
        return(s3)        

    def complement(self,s1,u):
        s3=[]
        for i in u:
            if i not in s1:
                s3.append(i)
        return (s3)
    def set_diff(self,s1,s2):
        s3=[]
        s3.extend(self.complement(s1,s2))
        return (s3)
    def symmetric_diff(self,s1,s2):
        s4=[]
        s4.extend(self.complement(s1,s2))
        s4.extend(self.complement(s2,s1))
        return s4
    def cartisian_product(self,s1,s2):
        self.res=set()
        for i in s1:
            for j in s2:
                self.res.add((i,j))
        return self.res
    
    def power_set(self,s1):
        lj=list(s1)
        subset=[]
        sets=[]
        for i in range (0,2**len(lj)):
            sut=[]
            for j in range(len(lj)):
                if (i>>j)%2==1:
                    sut.append(lj[j])
                sets.append(sut)
        g=[]
        for k in range (0, len(sets),len(s1)):
            g.append(sets[k])
        return(g)  
u={1,2,3,4}
print("HELLO\n\n")
print("What you want to perform from given set of operations\n","just write respective operation number")
print("1 : for searching entered digit in Universal set \n2 :  for checking 1st set is subset of 2nd set or not \n3 : for finding Union and Intersection of 2 given sets(which you will enter)")
print("4 : finding complement of a set \n5 : for finding Set diffrence and symmetric difference  of two sets\n6 : for finding Cartesian Product of two entered set")
print("7 : for finding power set of a entered set")
y="yes"
while(y=="yes"):
    n=int(input("\nenter you choice : "))
   
      
    s1={2}
    s2={2}
    s4={}

    obj_1 =Set(s1,s2)

    if(n==1):
        s=input("Enter universal set digits seprated by commas : ")
        u=s.split(',')
        u=[int(x)for x in u]
        n=int(input("enter a digit which you want search in universal set : "))
        print("is",n,"in Universal set ?  : ",obj_1.ismember(u,n))
    elif(n==2):
        s=input("Enter 1st set digits seprated by commas : ")
        s1=s.split(',')
        s1=[int(x)for x in s1]
        s=input("Enter 2nd set digits seprated by commas : ")
        s2=s.split(',')
        s2=[int(x)for x in s2]
        print("is 1st set  is subset of 2nd set  : ",obj_1.subset(s2,s1))
    elif(n==3):
        s=input("Enter 1st set digits seprated by commas : ")
        s1=s.split(',')
        s1=[int(x)for x in s1]
        s=input("Enter 2nd set digits seprated by commas : ")
        s2=s.split(',')
        s2=[int(x)for x in s2]
        print("Union of given sets is : ",obj_1.union(s1,s2))
        print("Intersection of given sets: ",obj_1.intersection(s1,s2))

    elif(n==4):
        s=input("Enter universal set digits seprated by commas : ")
        u=s.split(',')
        u=[int(x)for x in u]
        s=input("Enter set digits seprated by commas(for getting complement of it) : ")
        s1=s.split(',')
        s1=[int(x)for x in s1]
        print("complement of given set :",obj_1.complement(s1,u))
    elif(n==5):
        s=input("Enter 1st set digits seprated by commas : ")
        s1=s.split(',')
        s1=[int(x)for x in s1]
        s=input("Enter 2nd set digits seprated by commas : ")
        s2=s.split(',')
        s2=[int(x)for x in s2]
        print("set difference of s1 and s2 is : ",obj_1.set_diff(s1,s2))
        print("symmetric difference of s1 and s2 is : ",obj_1.symmetric_diff(s1,s2))
    elif(n==6):
        s=input("Enter 1st set digits seprated by commas : ")
        s1=s.split(',')
        s1=[int(x)for x in s1]
        s=input("Enter 2nd set digits seprated by commas : ")
        s2=s.split(',')
        s2=[int(x)for x in s2]
        print("cartisian product of s1 and s2 is : ",obj_1.cartisian_product(s1,s2))
    elif(n==7):
        s=input("Enter 1st set digits seprated by commas : ")
        s1=s.split(',')
        s1=[int(x)for x in s1]
        print("power set :",obj_1.power_set(s1))
    else:
        print("invalid choice \n Please try again")
    y=input("\n\nDo you want to continue : yes or no?\n")
    y=y.lower()

























