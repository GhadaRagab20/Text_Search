#Series Functions
"""
Series.find( key ) ##return the index of the given key
Series.size()   ##return the size of series
Series.binary_search( key ) ##return the value of the given key
Series.is_empty()   ##return 1 if the series is empty
Series.insert_order( key , value )  ##insert element in series if the key doesn't exist in it's order
                                        & if the key exist update it's value
Series.insert( key , value )    ##same as insert_order but the insertion is ranodm withoud order
Series.delete( key )    ## delete the element with the key given
Series.keys()   ##return list of keys
Series.values() ##return list of values
Series.items()  ##return list of tuples (key,value) ..useful to itterate
Series.sort()   ##quick sort on the elements
Series.update( index , value )  ##insert the value given the index

For all the functions if any operation failed or the deletion happened for an element that doesn't exist
the functions will return None...same for find & binary_search function
"""

class Node:
    def __init__(self,key=None,value=None):
        if(key == None):
            self.key=None
        else:
            self.key=key
        ###
        if (value == None):
            self.value = None
        else:
            self.value = value

    def __str__(self):
        return """({}:{})""".format(self.key,self.value)

    def __repr__(self):
        return """({}:{})""".format(self.key,self.value)


############################

class Series:
    def __init__(self,Nodes_list=None):
        if(Nodes_list== None):
            self.N_list=list()
        else:
            self.N_list=list(Nodes_list)


    def find(self,key):
        """search the elements & return the index of the list"""
        if(self.is_empty()):
            return None
        else:
            low=0
            high=len(self.N_list)-1
            while(low<=high):
                mid=(low+high)//2
                if(self.N_list[mid].key == key):
                    return mid

                elif (key > self.N_list[mid].key ):
                    low=mid+1

                else:
                    high=mid-1

            return None

    def size(self):
        """get the length of the list"""
        return len(self.N_list)

    def binary_search(self,key):
        """find the element with the given key & return val if the key exist and
        if not exist return None"""
        self.start=0
        self.end=self.size()-1
        while(self.start<=self.end):
            self.middle=int((self.start+self.end)/2)
            if(self.N_list[self.middle].key==key):
                return self.N_list[self.middle].value
            elif(self.N_list[self.middle].key<key):
                self.start=self.middle+1

            elif(self.N_list[self.middle].key>key):
                self.end = self.middle - 1
        return None



    def partition(self,start,end):
        """this function will help me in quick_sorting"""
        self.i=start
        self.j=end
        self.pivot=self.i
        for m in range(end-start):
            if(self.N_list[self.pivot].key>self.N_list[self.j].key ):
                self.N_list[self.j], self.N_list[self.pivot] = self.N_list[self.pivot], self.N_list[self.j]
                self.pivot = self.j
                self.i = self.i + 1
            elif(self.N_list[self.pivot].key < self.N_list[self.i].key):
                self.N_list[self.i], self.N_list[self.pivot] = self.N_list[self.pivot], self.N_list[self.i]
                self.pivot = self.i
                self.j = self.j - 1
            else:
                if(self.pivot==self.i and self.j!=self.i):
                    self.j = self.j - 1
                elif(self.pivot==self.j and self.j!=self.i):
                    self.i = self.i + 1
        return self.pivot

    def sort(self):
        self.sort_ex(0,self.size()-1)

    def sort_ex(self,start,end):
        """sort the elements by key"""
        if(start<end):
            piv=self.partition(start,end)
            self.sort_ex(start,piv-1)
            self.sort_ex(piv+1, end)


    def insert_order(self,key,val):
        """take key & value
        first check if the key existed or not
        if existed : update the value of existed key with (val)
        if not existed : create new node with the key & val then insert the node (in order) in the N_list"""
        ind=self.find(key)
        if(ind != None): ##key exist
            self.N_list[ind].value=val
        else:
            n=Node(key,val)
            if (self.is_empty()):
                self.N_list.append(n)
            else:
                old = len(self.N_list)
                for i in range(len(self.N_list)):
                    if self.N_list[i].key > key:
                        self.N_list.insert(i,n)
                        break
                if (old == len(self.N_list)):
                    self.N_list.append(n)

    def insert_set(self,key,file_id):
        """take key & value
        first check if the key existed or not
        if existed : update the value of existed key with (val)
        if not existed : create new node with the key & val then insert the node (in order) in the N_list"""
        ind=self.find(key)
        if(ind != None): ##key exist
            self.N_list[ind].value.add(file_id)
        else:
            s={file_id}
            n=Node(key,s)
            if (self.is_empty()):
                self.N_list.append(n)
            else:
                old=len(self.N_list)
                for i in range(len(self.N_list)):
                    if self.N_list[i].key > key:
                        self.N_list.insert(i,n)
                        break
                if(old == len(self.N_list)):
                    self.N_list.append(n)



    def update(self,index,val):
        """update the series by index"""
        self.N_list[index].value=val

    def insert(self,Key,Val):
        """take key & value
        first check if the key existed or not
        if existed : update the value of existed key with (val)
        if not existed : create new node with the key & val then insert the node in the N_list"""
        x=self.find(Key)
        if(x!=None):
            self.N_list[x].value=Val
        else:
            q=Node(Key,Val)
            self.N_list.append(q)

    def delete(self,key):
        """delete the element with the given key from the N_list"""
        if (self.is_empty()):
            return -1
        else:
            ind=self.find(key)
            if(ind != None):
                del self.N_list[ind]
                return 1
            else:
                return -1

    def keys(self):
        """get list of all keys"""
        l=list()
        for i in range(len(self.N_list)):
            l.append(self.N_list[i].key)
        return l

    def values(self):
        """get list of all values"""
        f=list()
        for i in range (len(self.N_list)):
            f.append(self.N_list[i].value)
        return f



    def is_empty(self):
        """check if the series is empty"""
        return self.size()==0

    def items(self):
        """return list of tuples (key,value)
         for traversing through it"""
        l=list()
        for node in self.N_list:
            t=(node.key,node.value)
            l.append(t)
        return l
