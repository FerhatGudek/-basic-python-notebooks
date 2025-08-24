class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer
    
    def checkAnswer(self, answer):
        return self.answer == answer    


class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0
    
    def getQuestion(self):
        return self.questions[self.questionIndex]
    
    def displayQuestion(self):
        question = self.getQuestion()
        print(f"Soru {self.questionIndex + 1}: {question.text}")
        
        for i, choice in enumerate(question.choices, 1):
            print(f"{i}) {choice}")
        
        answer = input("Cevabınızı girin: ")
        
        # Kullanıcının seçimi
        if question.checkAnswer(question.choices[int(answer)-1]):
            self.score += 1
            print("Doğru! ✅\n")
        else:
            print(f"Yanlış ❌ Doğru cevap: {question.answer}\n")
        
        self.questionIndex += 1
    
    def displayScore(self):
        print(f"Quiz bitti! Skorunuz: {self.score}/{len(self.questions)}")
    
    def start(self):
        while self.questionIndex < len(self.questions):
            self.displayQuestion()
        self.displayScore()


# Sorular
q1 = Question("En şerefli Türk takımı hangisidir ?", 
              ["Fenerbahce","Besiktas","Galatasaray","Liverpool","Barcelona","Realmadrid"], 
              "Fenerbahce")   
q2 = Question("En büyük Türk takımı hangisidir?", 
              ["Fenerbahce","Besiktas","Galatasaray","Liverpool","Barcelona","Realmadrid"], 
              "Fenerbahce") 
q3 = Question("En Cumhuriyetçi Türk takımı hangisidir?", 
              ["Fenerbahce","Besiktas","Galatasaray","Liverpool","Barcelona","Realmadrid"], 
              "Fenerbahce") 
q4 = Question("En fazla başarıya hasret Türk takımı hangisidir?", 
              ["Fenerbahce","Besiktas","Galatasaray","Liverpool","Barcelona","Realmadrid"], 
              "Fenerbahce") 
q5 = Question("Kalbimizdeki Takım hangisidir?", 
              ["Fenerbahce","Besiktas","Galatasaray","Liverpool","Barcelona","Realmadrid"], 
              "Fenerbahce")   

questions = [q1,q2,q3,q4,q5] 
quiz = Quiz(questions)
quiz.start()
