'''with open("Practice.txt","w") as f:
    f.write("Hi everyone\nwe are learning file i/o\nusing Java\ni like programming in Java")'''
    
# waf that replaces all occurrences of "java" with python:
'''with open("Practice.txt","r") as f:
    data=f.read()

new_data=data.replace("Java","Python")    
print(new_data)

with open("Practice.txt","w") as f:
    f.write(new_data)'''
    
'''def word_in_file(filename,word1,word2):
    with open(filename,"r") as f:
        data=f.read()
    new_data=data.replace(word1,word2)
    print(new_data)
    with open(filename,"w") as f:
        f.write(new_data)      

word_in_file("Practice.txt","Java","Python") '''
    
#search in the file that "learning" exists or not:-
'''def search_word(filename , word):
    with open(filename,"r") as f:
        data = f.read()
        if(data.find(word) != -1):
            idx=data.find(word)
            print("found at index",idx)
        else:
            print("Not found!")    
search_word("Practice.txt","Python")'''
#waf to find which line word occured first:
'''def check_line(filename,word):
    line_no=1
    data=True
    with open(filename,"r") as f:
        while data:
            data= f.readline()
            if(word in data):
                print(line_no)
                return
                
            line_no+=1
    return -1    
            
    

check_line("Practice.txt","Python")     '''
#from a file that contains numbers seprated by commas you have to find even count
def evencount(filename):
    with open(filename,"r") as f:
        data=f.read()
        count=0
        nums= data.split(",")
        for i in nums:
            if(int(i)%2==0):
                count+=1
        print("Count of even number in this file is:",count)

evencount("oddeven.txt")                  
        
                
        
        
    
    

    