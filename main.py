"""Keep a small in-memory grade list."""


def main():
    grades = []
    while True:
        print("\n1) Add mark  2) List marks  3) Average  4) Quit")
        choice = input("Choose: ").strip()
        if choice == "1":
            name = input("Student name: ").strip()
            try:
                mark = float(input("Mark (0-100): "))
                if not 0 <= mark <= 100:
                    raise ValueError
            except ValueError:
                print("Enter a number from 0 to 100.")
                continue
            grades.append((name, mark))
        elif choice == "2":
            for name, mark in grades:
                print(f"{name}: {mark:.1f}")
        elif choice == "3":
            if grades:
                print(f"Class average: {sum(mark for _, mark in grades) / len(grades):.1f}")
            else:
                print("Add at least one mark first.")
        elif choice == "4":
            return
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
