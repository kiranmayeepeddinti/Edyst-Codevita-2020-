def is_consonant(char):
    if char not in 'aeiou':
        return True
    return False

def possibilities(remaining_ids,curr_string,curr_users):
    ans = 0
    if len(curr_string)==0 and remaining_ids==0:
        return 1
    if len(curr_string) < 4:
        return ans
    
    start = 0
    end = start + 3
    for i in range(end,len(curr_string)):
        curr_user_id = curr_string[start:i+1]
        if is_consonant(curr_string[start]) and is_consonant(curr_string[i]) and curr_user_id not in curr_users:
            curr_users.add(curr_user_id)
            ans = ans + possibilities(remaining_ids-1,curr_string[i+1:],curr_users)
            curr_users.remove(curr_user_id)
    return ans


num_of_ids = int(input())
id_string = input()
curr_users = set()
ans=possibilities(num_of_ids,id_string,curr_users)
print(ans)
