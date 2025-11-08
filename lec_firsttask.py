class SchoolJournal:

    def __init__(self, subject, student):

        self.subject = subject
        self.student = student
        self.grade_list = []
    
        
    def grade(self):
        for i in range(int(input())):
            self.grade_list.append(int(input(f'Введите {i + 1} оценку:')))
        

    def printer(self):

        print("Имя ученика:", self.student)
        print('Название предмета:', self.subject)
        print("Список оценок:", self.grade_list)

    def final_grade(self):
        
        print("Средняя оценка:", sum(self.grade_list)/len(self.grade_list))

student1 = SchoolJournal('Math', 'Илья')
student1.grade()
print("Успеваемость:", student1.grade_list)
student1.final_grade()