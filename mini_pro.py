def calculate_love_score(name1,name2):
    love=['l' , 'o' , 'v','e']
    true = ['t','r','u','e']
    name3=name1+name2
    i=0
    score1=0
    score2=0
    for char in name3:
        if char in love:
            score1+=1
        if char in true:
            score2+=1
    
    score3=score1+score2
    print(score3)
    

calculate_love_score("azeem" , "abdul")