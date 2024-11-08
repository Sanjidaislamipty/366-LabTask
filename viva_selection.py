
import random
import os

def read_student_ids(filename="student_ids.txt"):
    try:
        with open(filename, 'r') as file:
            student_ids = [line.strip() for line in file if line.strip()]
        if not student_ids:
            raise ValueError("The file is empty.")
        return student_ids
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return []
    except ValueError as e:
        print(f"Error: {e}")
        return []

def select_students_for_viva(student_ids):
    viva_count = 1
    while student_ids:
        selected_student = random.choice(student_ids)
        print(f"Viva #{viva_count}: {selected_student}")
        student_ids.remove(selected_student)
        viva_count += 1

def viva_process(filename="student_ids.txt"):
    student_ids = read_student_ids(filename)
    if not student_ids:
        return

    while True:
        print("\nStarting new round of vivas...")
        select_students_for_viva(student_ids)
        student_ids = read_student_ids(filename)
        if input("All students have been selected. Press Enter to restart or 'q' to quit: ").lower() == 'q':
            break

if __name__ == "__main__":
    viva_process()
