class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:

        len_a = len(a)
        len_b = len(b)

        new_a = ((len_b-1)//(len_a)+1) * a

        print(new_a, ((len_b-1)//(len_a)+1))
        
        if b in new_a:
            return ((len_b-1)//(len_a)+1)


        else:
            new_a += a
            if b in new_a:
                return ((len_b-1)//(len_a)+1) + 1
 
        return -1
