import random

l = [ random.randint(1,100) for i in range(20)]

def main():
    def get_max(l):
        max_value=l[0]
        for i in l:
            if i > max_value:
                max_value=i
                
        return max_value
            
    def get_min(l):
        min_value=l[0]
        for i in l:
            if i < min_value:
                min_value=i
                
        return min_value
    
    def get_avg(l):
        sum_value=0
        list_length=len(l)
        for i in l:
            sum_value+=i
        
        return sum_value/list_length
        
        
    def sum_even(l):
        sum_even_value=0
        for i in l : 
            if i%2==0:
                sum_even_value+=i
        return sum_even_value
        
        
    def sum_odd(l):
        sum_odd_value=0
        for i in l : 
            if i%2!=0:
                sum_odd_value+=i
        return sum_odd_value
        
        
    def get_factorial(l):
        factorial=1
        for i in l:
            factorial*=i
            
        return factorial
        
    
    print("MAX_VALUE=",get_max(l))
    print("MIN_VALUE=",get_min(l))
    print("AVG_VALUE=",get_avg(l))
    print("SUM_EVEN_VALUE=",sum_even(l))
    print("SUM_ODD_VALUE=",sum_odd(l))
    print("FACTORIAL_VALUE=", get_factorial(l))




if __name__=="__main__":
    main()

