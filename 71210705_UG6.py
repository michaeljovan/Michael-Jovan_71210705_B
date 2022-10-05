class nodeMahasiswa  : 
    def __init__(self,nama,ipk,n = None,p = None) : 
        self._element = nama 
        self._ipk = ipk 
        self._next = n 
        self._prev = p  
    
    def getNama(self) : 
        return self._element  

    def getIpk(self) : 
        return self._ipk 

    def setNama(self,nama) : 
        self._element = nama 
         
    def setIpk(self,ipk) : 
        self._ipk = ipk 

class DLLNC :  
    def __init__(self) : 
        self.head = None 
        self.tail = None 
        self.size = 0  

    def isEmpty(self) : 
        return self._size == 0 
    
    def __len__ (self) : 
        return self._size == 0 

    def addElementTail(self,nama,ipk) : 
        baru = nodeMahasiswa(nama,ipk) 

        if self.size ==0 : 
            self.head = baru 
            self.tail = baru 
        else :  
            self.tail._next = baru 
            baru._prev = self.tail 
            self.tail = baru   
        print("data masuk ke tail") 
        self.size = self.size + 1  

    def deleteLast(self) : 
        if self.size == 1 : 
            self.head = None 
            self.tail = None 
        else : 
            hapus = self.tail 
            self.tail = self.tail._prev 
            hapus._prev = None 
            self.tail.next = None  
            print("# Data",hapus._element,"Terhapus #") 

            del hapus   
        self.size -= 1 

    def printAllDescending(self) : 
        bantu = self.tail 
        print("===== Print Descending =====") 

        while bantu != None : 
            print("=" * 20) 
            print("Nama :", bantu._element) 
            print("Ipk : ", bantu._ipk) 
            bantu = bantu._prev

    def rataIpk(self) : 
        ipk = 0 
        size = 0 
        bantu = self.tail 
        while bantu != None : 
            ipk = ipk + bantu._ipk 
            bantu = bantu._prev  
            size += 1 
        print("===== Rata - Rata IPK =====") 
        print("Rata - Rata :", round(ipk/size,2))



DLLNCprint = DLLNC()
DLLNCprint.addElementTail('Shalom',3.9) 
DLLNCprint.addElementTail('Nabila',3.8) 
DLLNCprint.addElementTail('Kurniadi',3.7) 
DLLNCprint.addElementTail('Harris',3.6) 
DLLNCprint.printAllDescending() 
print()
DLLNCprint.deleteLast() 
DLLNCprint.printAllDescending() 
print()
DLLNCprint.rataIpk()