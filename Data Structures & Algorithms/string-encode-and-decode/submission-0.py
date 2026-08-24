class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_str=""
        for i in strs:
            encode_str+=str(len(i))+"#" + i
        return encode_str



    def decode(self, s: str) -> List[str]:
        decode_str=[]
        idx=0
        while idx < len(s):
            j=idx
            while s[j]!="#":
                j+=1
            length=int(s[idx:j])
            decode_str.append(s[j+1:j+1+length])
            idx=j+1+length

        return    decode_str
