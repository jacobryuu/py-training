import sys
from decimal import Decimal, ROUND_HALF_UP
from dataclasses import dataclass
from typing import List


@dataclass
class Student:
    id: str = ""
    order_id: int = 0
    math: int = 0
    science: int = 0
    english: int = 0
    japanese: int = 0
    history: int = 0
    geography: int = 0
    avg: Decimal = Decimal('0')
    dropout: bool = False


def main():
    if len(sys.argv) < 3:
        print("Usage: python app.py <command> <file>")
        return
    
    dropouts = "dropouts"
    top_vs_bottom = "top-vs-bottom"
    grades: List[Student] = []
    first = True
    dropout_grade = 49
    
    try:
        with open(sys.argv[2], 'r') as f:
            for line in f:
                if first:
                    first = False
                    continue
                
                drop_count = 0
                student_array = line.strip().split(',')
                student = Student()
                student.id = student_array[0]
                student.order_id = int(student_array[0][1:])
                
                student.math = int(student_array[1])
                if student.math <= dropout_grade:
                    drop_count += 1
                
                student.science = int(student_array[2])
                if student.science <= dropout_grade:
                    drop_count += 1
                
                student.english = int(student_array[3])
                if student.english <= dropout_grade:
                    drop_count += 1
                
                student.japanese = int(student_array[4])
                if student.japanese <= dropout_grade:
                    drop_count += 1
                
                student.history = int(student_array[5])
                if student.history <= dropout_grade:
                    drop_count += 1
                
                student.geography = int(student_array[6])
                if student.geography <= dropout_grade:
                    drop_count += 1
                
                avg = (student.math + student.science + student.english + 
                       student.japanese + student.history + student.geography) / 6
                student.avg = Decimal(str(avg)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                
                student.dropout = drop_count >= 2
                grades.append(student)
    
    except Exception as e:
        print(f"Error reading file: {e}")
        return
    
    if sys.argv[1].lower() == dropouts:
        student_order_by_id = sorted(
            [s for s in grades if s.dropout],
            key=lambda s: s.order_id
        )
        print("ID")
        for student in student_order_by_id:
            print(student.id)
    
    elif sys.argv[1].lower() == top_vs_bottom:
        student_order_by_avg_and_id = sorted(
            grades,
            key=lambda s: (s.avg, s.order_id)
        )
        
        min_avg = student_order_by_avg_and_id[0].avg
        max_avg = student_order_by_avg_and_id[-1].avg
        
        student_min_and_max = [
            s for s in student_order_by_avg_and_id 
            if s.avg == min_avg or s.avg == max_avg
        ]
        
        print("ID,Mean")
        for student in student_min_and_max:
            print(f"{student.id},{student.avg}")


if __name__ == "__main__":
    main()
