
def count_smaller(lst:list, item:int)->int:
    if len(lst) == 0:
        return 0
    else:
        if lst[0] < item:
            return 1 + count_smaller(lst[1:], item)
        else:
            return count_smaller(lst[1:], item)
        
def is_palindrome(s)-> bool:
    if len(s) == 0 or len(s) == 1:
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False
        
def avg_word_length(lst:list,length:int=0,count:int=0)->float:
    if len(lst) == 0:
        return length/count
    else:
        length += len(lst[0])
        count += 1
        return round(avg_word_length(lst[1:],length,count))
    

def flatten(lst:list)->list: 
    """
    Using recursion, return a new list that is the deep reverse of a.
    """
    print(type(lst))
    if not lst:
        return []
    if isinstance(lst[0],list):
        return flatten(lst[0]) + flatten(lst[1:])
    else:
        return [lst[0]] + flatten(lst[1:])
        

print(flatten([[1,2,3,4],[1,2,3,4]]))

# print(avg_word_length(['hello', 'world']))
# print(is_palindrome("raceca"))
# print(count_smaller([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11))