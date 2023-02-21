#4. Create a class Time with private attributes hour, minute and second.
#Overload ‘+’ operator to find sum of 2 time.

#overload '+'
class time:
    def __init__(self):
        self.__hour=int(input("enter the hour:"))
        self.__minute=int(input("ent2er the minute:"))
        self.__second=int(input("enter the seconds:"))
    def __add__(self,t2):
        hours=self.__hour+t2.__hour
        print("sum of hours:",hours)
        minutes=self.__minute+t2.__minute
        print("sum of minutes:",minutes)
        seconds=self.__second+t2.__second
        print("sum of seconds:",seconds)
        if hours>=24:
            hours=hours%24
        if minutes>=60:
            hours=hours+minutes//60
            minutes=minutes%60
        if seconds>=60:
            minutes=minutes+seconds//60
            seconds=seconds%60
        return(hours,minutes,seconds)
t1= time()
t2= time()
print("hour,minute,seconds",t1+t2)
    
            
            
            
            
          
            
            
        
        
        
        
        
        
        
        
    