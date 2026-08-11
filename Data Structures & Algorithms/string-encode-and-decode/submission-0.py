class Solution:

    def encode(self, strs: List[str]) -> str:
        ns = ''
        for s in strs:
            ns+=(str(255+len(s))+' ')
            for c in s:
                ns+=(str(ord(c))+' ')
        print(ns)
        return str(ns)



    def decode(self, s: str) -> List[str]:
        strs=[]
        st=''
        li=s.split()
        i=0
        while i<len(li):
            x=int(li[i])
            if x==255:
                st+=""
    
            if x>255:
                l=x-255
                while l!=0:
                    st+=chr(int(li[i+1]))
                    i+=1
                    l-=1
            strs.append(st)
            st=''
            i+=1
        return strs





