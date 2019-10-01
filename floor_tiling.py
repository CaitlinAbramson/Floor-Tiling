import random

p1 = 20
p2 = 20
p3 = 20
p4 = 20
p5 = 20
p6 = 20
p7 = 20
p8 = 20
p9 = 20
p10 = 20

class FloorTiling:

    def count(self, val):
        if val == 1:
            global p1
            p1 -= 1
            return p1
        if val == 2:
            global p2
            p2 -= 1
            return p2
        if val == 3:
            global p3 
            p3 -= 1
            return p3
        if val == 4:
            global p4 
            p4 -= 1
            return p4
        if val == 5:
            global p5
            p5 -= 1
            return p5
        if val == 6:
            global p6
            p6 -= 1
            return p6
        if val == 7:
            global p7
            p7 -= 1
            return p7
        if val == 8:
            global p8
            p8 -= 1
            return p8
        if val == 9:
            global p9
            p9 -= 1
            return p9
        if val == 10:
            global p10
            p10 -= 1
            return p10

    def tile(self, area):
        c = len(area[0])
        r = len(area)
        
        #set up first 10
        all_vals = list(range(1, 11))
        set_init_pattern = 1
        for i in range (0, 10): 
            area[0][i] = set_init_pattern
            set_init_pattern += 1
            
        #set up rest of first row
        for j in range (10, c):
            l1 = area[0][j-1]
            l2 = area[0][j-2]
            l3 = area[0][j-3]
            limit_vals = [l1, l2, l3]
            possible_vals = [e for e in all_vals if e not in limit_vals]
            val = random.choice(possible_vals)
            val_count = self.count(val)
            area[0][j] = val
        
        #remaining rows
        for i in range(1, r):
            for j in range(0, c):
                if i < 5:
                    #edge case: column 0
                    if j == 0:
                        u = area[i-1][j]
                        ur = area[i-1][j+1]
                        ur2 = area[i-1][j+2]
                        limit_vals = [u, ur, ur2]
                        possible_vals = [e for e in all_vals if e not in limit_vals]
                        val = random.choice(possible_vals)
                        val_count = self.count(val)
                        if val_count > 0:
                            area[i][j] = val
                        while(val_count <= 0):
                            limit_vals.append(val)
                            possible_vals = [e for e in all_vals if e not in limit_vals]
                            if not possible_vals:
                                val = random.choice(limit_vals)
                            else:
                                val = random.choice(possible_vals)
                            val_count = self.count(val)
                            area[i][j] = val
                        
                    #edge case: column c-1
                    if j == c-1:
                        u = area[i-1][j]
                        ul = area[i-1][j-1]
                        ul2 = area[i-1][j-2]
                        l1 = area[i][j-1]
                        l2 = area[i][j-2]
                        l3 = area[i][j-3]
                        limit_vals = [u, ul, ul2, l1, l2, l3]
                        possible_vals = [e for e in all_vals if e not in limit_vals]
                        val = random.choice(possible_vals)
                        val_count = self.count(val)
                        if val_count > 0:
                            area[i][j] = val
                        while(val_count <= 0):
                            limit_vals.append(val)
                            possible_vals = [e for e in all_vals if e not in limit_vals]
                            if not possible_vals:
                                val = random.choice(limit_vals)
                            else:
                                val = random.choice(possible_vals)
                            val_count = self.count(val)
                            area[i][j] = val
                        
                    #edge case: row 1
                    if 0 < j < c - 1:
                        u = area[i-1][j]
                        ul = area[i-1][j-1]
                        ur = area[i-1][j+1]
                        l1 = area[i][j-1]
                        if j == 1:
                            ur2 = area[i-1][j+2]
                            limit_vals = [u, ul, ur, ur2, l1]
                        elif j == c - 2:
                            ul2 = area[i-1][j-2]
                            l2 = area[i][j-2]
                            l3 = area[i][j-3]
                            limit_vals = [u, ul, ul2, ur, l1, l2, l3]
                        elif j == c - 3:
                            ul2 = area[i-1][j-2]
                            ur2 = area[i-1][j+2]
                            l2 = area[i][j-2]
                            l3 = area[i][j-3]
                            limit_vals = [u, ul, ul2, ur, ur2, l1, l2, l3]
                        elif j == 2:
                            l2 = area[i][j-2]
                            ur2 = area[i-1][j+2]
                            ul2 = area[i-1][j-2]
                            limit_vals = [u, ul, ul2, ur, ur2, l1, l2]
                        else:
                            l3 = area[i][j-3]
                            l2 = area[i][j-2]
                            ur2 = area[i-1][j+2]
                            ul2 = area[i-1][j-2]
                            limit_vals = [u, ul, ul2, ur, ur2, l1, l2, l3]
                        possible_vals = [e for e in all_vals if e not in limit_vals]  
                        val_count = self.count(val)
                        if val_count > 0:
                            val = random.choice(possible_vals)
                            area[i][j] = val
                        while(val_count <= 0):
                            limit_vals.append(val)
                            possible_vals = [e for e in all_vals if e not in limit_vals]
                            if not possible_vals:
                                val = random.choice(limit_vals)
                            else:
                                val = random.choice(possible_vals)
                            val_count = self.count(val)
                            area[i][j] = val
                else: 
                     if j > 12:
                         if j == c - 1:
                             u = area[i-1][j]
                             ul = area[i-1][j-1]
                             ul2 = area[i-1][j-2]
                             l1 = area[i][j-1]
                             l2 = area[i][j-2]
                             l3 = area[i][j-3]
                             limit_vals = [u, ul, ul2, l1, l2, l3]
                         elif j == c - 2:
                             u = area[i-1][j]
                             ul = area[i-1][j-1]
                             ul2 = area[i-1][j-2]
                             ur = area[i-1][j+1]
                             l1 = area[i][j-1]
                             l2 = area[i][j-2]
                             l3 = area[i][j-3]
                             limit_vals = [u, ul, ul2, ur, l1, l2, l3]
                         else:
                             u = area[i-1][j]
                             ul = area[i-1][j-1]
                             ul2 = area[i-1][j-2]
                             ur = area[i-1][j+1]
                             ur2 = area[i-1][j+2]
                             l1 = area[i][j-1]
                             l2 = area[i][j-2]
                             l3 = area[i][j-3]
                             limit_vals = [u, ul, ul2, ur, ur2, l1, l2, l3]
                         possible_vals = [e for e in all_vals if e not in limit_vals]
                         val = random.choice(possible_vals)
                         val_count = self.count(val)
                         if val_count > 0:
                             area[i][j] = val
                         while(val_count <= 0):
                             limit_vals.append(val)
                             possible_vals = [e for e in all_vals if e not in limit_vals]
                             if not possible_vals:
                                 val = random.choice(limit_vals)
                             else:
                                 val = random.choice(possible_vals)
                             val_count = self.count(val)
                             area[i][j] = val 
                            
        return area
    

