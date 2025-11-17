# 🎓 STUDENT GRADE MANAGER - GSOC PYTHON PROJECT
# 🚀 Automated Grade Calculation System

def calculate_grade(average):
    """Calculate grade based on average marks"""
    if average >= 90:
        return "A+ 🏆"
    elif average >= 80:
        return "A 💪"
    elif average >= 70:
        return "B 👍"
    elif average >= 60:
        return "C ✅"
    elif average >= 50:
        return "D ⚠️"
    else:
        return "F ❌"

def get_student_data():
    """Get student information and marks"""
    print("🎓" * 20)
    print("🚀 GSOC GRADE MANAGER")
    print("🎓" * 20)
    
    name = input("👤 Enter Student Name: ")
    subjects = ["Math", "Science", "English", "Computer", "Physics"]
    marks = []
    
    print("\n📝 Enter Marks (0-100):")
    for subject in subjects:
        while True:
            try:
                mark = int(input(f"💯 {subject}: "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("❌ Marks must be 0-100!")
            except ValueError:
                print("❌ Enter a valid number!")
    
    return name, subjects, marks

def generate_report(name, subjects, marks):
    """Generate comprehensive report card"""
    total = sum(marks)
    average = total / len(marks)
    grade = calculate_grade(average)
    
    print("\n" + "🎉" * 30)
    print("🌟 ACADEMIC REPORT CARD 🌟")
    print("🎉" * 30)
    print(f"👤 Student: {name.upper()}")
    print("📊" * 15)
    
    for i, subject in enumerate(subjects):
        print(f"📖 {subject}: {marks[i]}/100")
    
    print("🎯" * 15)
    print(f"📈 Total: {total}/500")
    print(f"📊 Average: {average:.2f}%")
    print(f"🏅 Grade: {grade}")
    
    # Achievements
    print("\n🎊 Achievements:")
    if average >= 90:
        print("   🏆 Scholar Award - Outstanding!")
    elif average >= 80:
        print("   💫 Honor Roll - Excellent!")
    
    print("🎉" * 30)
    return average, grade

def main():
    """Main program function"""
    try:
        name, subjects, marks = get_student_data()
        average, grade = generate_report(name, subjects, marks)
        
        print("\n💡 Final Remarks:")
        if average >= 80:
            print("   You're crushing it! Keep shining! ✨")
        else:
            print("   Keep grinding! Success is coming! 💪")
            
    except KeyboardInterrupt:
        print("\n👋 Thanks for using Grade Manager!")

if __name__ == "__main__":
    main()
