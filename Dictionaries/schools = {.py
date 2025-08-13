schools = { 
    "Codezilla": 
        {"Mohamed Hassan":  
            {"math": 100, 
            "english": 90, 
            "science": 85, 
            "arabic": 100,  
            "history": 97}, 
        "Ahmed Kamal": 
            {"math": 100, 
            "english": 95, 
            "science": 93, 
            "arabic": 100, 
            "history": 94} 
        }, 
    "Al-Azhar":{ 
        "Ali Adel": { 
            "math": 85, 
            "english": 83, 
            "science": 87, 
            "arabic": 100, 
            "history": 90}, 
        "Mariam Ali": { 
            "math": 100, 
            "english": 94, 
            "science": 98, 
            "arabic": 100, 
            "history": 100} 
        } 
} 

for school,student in schools.items():
    all_score = []
    for grades in student.values():
        total = list(grades.values())
        all_score.extend(total)
    avrage = sum(all_score) / len(all_score)
    print(f"The Average Total Percentage for {school} School is {avrage:.2f} ")
    


https://www.programiz.com/online-compiler/2SqQNqfJG6iMx