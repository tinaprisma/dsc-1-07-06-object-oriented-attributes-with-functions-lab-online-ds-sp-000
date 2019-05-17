import copy

class School:
    
    def __init__(self, name): # this have default arguments
        self.name = name
        self._roster = {}
        
    def roster(self):
        return self._roster
    
    def add_student(self, name, grade):
        if grade in self._roster: # if the school's roster for that grade is empty
            self._roster[grade].append(name) # and add a student to the list
        else: 
            self._roster[grade] = [name]
        return self._roster
                  
    def grade(self, grade):
        students_in_grade = self._roster[grade]
        return students_in_grade
        
    def sort_roster(self):
        new_dict = copy.deepcopy(self._roster)
        for key in new_dict:
            new_dict[key].sort()
        return new_dict

            
        