def numJewelsInStones(self, J, S):
        num = 0
        for i in S:
            if i in J:
                num+=1
        return num
