def works_fine():
    a = 5
    b = 6
    assert(a+b == 10)
#we could set a breakpoint right before calling the works_fine method 
#and run the script until we reach the breakpoint by pressing c(continue):    
def calling_things():
#At this point, you can s(step) into works_fine() or execute works_fine() by pressing n(next) to advance to the next line:    
    works_fine()       #we set break point in works_fine() #before calling works_fine() , we set break point : line # 9
    throws_an_exception()
    
calling_things()