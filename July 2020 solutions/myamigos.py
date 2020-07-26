def copy_arr(arr):
    duplicate = []
    for i in arr:
        duplicate.append(i)
    return duplicate
 
def is_adjacent(person1, person2, p):
    p1_index = p.index(person1)
    p2_index = p.index(person2)
    if abs(p1_index - p2_index) == 1:
        return True
    if p2_index == len(p)-1 and p1_index == 0:
        return True
    if p1_index == len(p)-1 and p2_index == 1:
        return True
    return False
 
def place_adjacent(person1, person2, possibilities, directions):
    new_possibilities = []
    for curr in possibilities:
        if person1 in curr and person2 in curr: # if they already exist, just confirm adjacency
            if is_adjacent(person1, person2, curr):
                new_possibilities.append(curr)
        elif person1 in curr or person2 in curr:# if either doesn't exist
            me = person1
            other = person2
            if person1 not in curr:
                me,other = other, me
            me_index = curr.index(me)
            other_index_1 = (curr.index(me) + 1)%len(curr)
            other_index_2 = (curr.index(me) - 1)%len(curr)
            for i in [other_index_1, other_index_2]:
                if curr[i] == '':
                    new_p = copy_arr(curr)
                    new_p[i] = other
                    new_possibilities.append(new_p)
        else:
            # go through all the vacant spaces and keep adjacent pairs
            me = person1
            other = person2
            for i in range(len(curr)):
                next_index = (i+1)%len(curr)
                if curr[i] == '' and curr[next_index] == '':
                    ## add possibility of a,b
                    
                    new_p = copy_arr(curr)
                    new_p[i] = me
                    new_p[next_index] = other
                    new_possibilities.append(new_p)
 
                    ## add possibility of b,a
 
                    new_p = copy_arr(curr)
                    new_p[i] = other
                    new_p[next_index] = me
                    new_possibilities.append(new_p)
 
 
    return new_possibilities
 
def place_opposite(person1, person2, possibilities, directions):
    new_possibilities = []
    for curr in possibilities:
        if person1 in curr and person2 in curr: # if they already exist, just confirm opposite
            if abs(curr.index(person1) - curr.index(person2)) == len(curr)//2:
                new_possibilities.append(curr)
        elif person1 in curr or person2 in curr:# if either doesn't exist
            me = person1
            other = person2
            if person1 not in curr:
                me,other = other, me
            me_index = curr.index(me)
            other_index = (curr.index(me) + (len(curr)//2))%len(curr)
            if curr[other_index] == '':
                new_p = copy_arr(curr)
                new_p[other_index] = other
                new_possibilities.append(new_p)
        else:
            # go through all the vacant spaces and keep opposite pairs
            me = person1
            other = person2
            for i in range(len(curr)):
                next_index = (i+(len(curr)//2))%len(curr)
                if curr[i] == '' and curr[next_index] == '':
                    ## add possibility of a,b
                    
                    new_p = copy_arr(curr)
                    new_p[i] = me
                    new_p[next_index] = other
                    new_possibilities.append(new_p)
 
                    ## add possibility of b,a
 
                    new_p = copy_arr(curr)
                    new_p[i] = other
                    new_p[next_index] = me
                    new_possibilities.append(new_p)
 
 
    return new_possibilities
 
 
# facing up is inward, facing down is outward
def place_left(person1, person2, possibilities, directions):
    # person1 left, person2 right
    new_possibilities = []
    if person2 not in directions:
        new_possibilities = place_adjacent(person1, person2,possibilities, directions)
        return new_possibilities
    for curr in possibilities:
        if person2 in curr:
            me = curr.index(person2)
            if directions[person2] == 'in':
                other = (curr.index(person2) - 1)%len(curr)
            elif directions[person2] == 'out':
                other = (curr.index(person2) + 1)%len(curr)            
            
            if curr[other] != '':
                continue
            new_p = copy_arr(curr)
            new_p[other] = person1
            new_possibilities.append(new_p)
        elif person1 in curr:
            other = curr.index(person1)
            if directions[person2] == 'in':
                me = (other + 1)%len(curr)
            elif directions[person2] == 'out':
                me = (other - 1)%len(curr)         
            
            if curr[me] != '':
                continue
            new_p = copy_arr(curr)
            new_p[me] = person2
            new_possibilities.append(new_p)
        else:
            for i in range(len(curr)):
                if directions[person2] == 'in':
                    other = (i - 1)%len(curr)
                elif directions[person2] == 'out':
                    other = (i + 1)%len(curr)   
                if curr[i] != '' or curr[other] != '':
                    continue
                me = i
                new_p = copy_arr(curr)
                new_p[me] = person2
                new_p[other] = person1
                new_possibilities.append(new_p)
    
    return new_possibilities
 
 
 
 
# facing up is inward, facing down is outward
def place_right(person1, person2, possibilities, directions):
    # person1 right, person2 left
    new_possibilities = []
    if person2 not in directions:
        new_possibilities = place_adjacent(person1, person2,possibilities, directions)
        return new_possibilities
    for curr in possibilities:
        if person2 in curr:
            me = curr.index(person2)
            if directions[person2] == 'in':
                other = (curr.index(person2) + 1)%len(curr)
            elif directions[person2] == 'out':
                other = (curr.index(person2) - 1)%len(curr)            
            
            
            if curr[other] == person1:
                new_p = copy_arr(curr)
                new_p[other] = person1
                new_possibilities.append(new_p)
            if curr[other] != '':
                continue
 
            new_p = copy_arr(curr)
            new_p[other] = person1
            new_possibilities.append(new_p)
        elif person1 in curr:
            other = curr.index(person1)
            if directions[person2] == 'in':
                me = (other - 1)%len(curr)
            elif directions[person2] == 'out':
                me = (other + 1)%len(curr)         
            
            if curr[me] != '':
                continue
 
            new_p = copy_arr(curr)
            new_p[me] = person2
            new_possibilities.append(new_p)
        else:
            for i in range(len(curr)):
                if directions[person2] == 'in':
                    other = (i + 1)%len(curr)
                elif directions[person2] == 'out':
                    other = (i - 1)%len(curr)     
                if curr[i] != '' or curr[other] != '':
                    continue
                me = i
                new_p = copy_arr(curr)
                new_p[me] = person2
                new_p[other] = person1
                new_possibilities.append(new_p)
    
    return new_possibilities
 
 
 
N = int(input())
N = 2*N
 
facts = input().split(';')
questions = input().split(';')
 
arrangement = [''] * N
 
possibilities = []
total_inwards = 0
total_outwards = 0
inward_known = 0
outward_known = 0
positional_facts = []
directions = {}
 
for fact in facts:
    if fact[0] == '7':
        total_inwards = int(fact[1])
        total_outwards = N - total_inwards
    elif fact[0] == '8':
        total_outwards = int(fact[1])
        total_inwards = N - total_outwards
    elif fact[0] == '5':
        directions[fact[1]] = "in"
        inward_known+= 1
    elif fact[0] == '6':
        directions[fact[1]] = "out"
        outward_known+=1
    else:
        positional_facts.append(fact)
 
positional_facts.sort(key = lambda x: min(x[1:]))
 
alphas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
 
if inward_known == total_inwards:
    for i in range(N):
        if alphas[i] not in directions:
            directions[alphas[i]] = "out"
            outward_known+=1
 
if outward_known == total_outwards:
    for i in range(N):
        if alphas[i] not in directions:
            directions[alphas[i]] = "in"
            inward_known+=1
        
 
# print(positional_facts)
 
arrangement[0] = min(positional_facts[0][1:])
possibilities.append(arrangement)
 
# print(arrangement)
# print(directions)
 
for fact in positional_facts:
    info = fact[0]
    # print(fact)
    if info == '1':
        possibilities = place_adjacent(fact[1], fact[2], possibilities, directions)
    if info == '2':
        possibilities = place_opposite(fact[1], fact[2], possibilities, directions)
    if info == '3':
        possibilities = place_left(fact[1], fact[2], possibilities, directions)
    if info == '4':
        possibilities = place_right(fact[1], fact[2], possibilities, directions)
    
    # if len(possibilities) == 0:
    #     break
    # print(possibilities)
 
if len(possibilities) != 1:
    print('ARRANGEMENT NOT POSSIBLE')
else:
    arrangement = possibilities[0]
    # print(arrangement)
    for  index in range(len(questions)):
        q = questions[index]
        query = int(q[1])
        val = q[2]
        if query == 2:
            me = arrangement.index(val)
            other = (me+ (len(arrangement)//2))%len(arrangement)
            ans = arrangement[other]
        if query == 3:
            me = arrangement.index(val)
            dir = directions[val]
            if dir == 'out':
                other = (me+1 )%len(arrangement)
            if dir == 'in':
                other = (me-1) %len(arrangement)
            ans = arrangement[other]
        if query == 4:
            me = arrangement.index(val)
            dir = directions[val]
            if dir == 'out':
                other = (me-1) %len(arrangement)
            if dir == 'in':
                other = (me+1) %len(arrangement)
            ans = arrangement[other]
        if query == 5:
            dir = directions[val]
            if dir == 'in':
                ans = 'Y'
            else:
                ans = 'N'
        if query ==6:
            dir = directions[val]
            if dir == 'out':
                ans = 'Y'
            else:
                ans = 'N'
        if index < len(questions)-1:
            print(ans,end=';')
        else:
            print(ans)
