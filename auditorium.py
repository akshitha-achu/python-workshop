num_rows = int(input("Enter number of rows: "))
section1 = int(input("Enter number of seats in Section 1: "))
section2 = int(input("Enter number of seats in Section 2: "))
section3 = int(input("Enter number of seats in Section 3: "))
auditorium = [["-" for _ in range(section1 + section2 + section3)] for _ in range(num_rows)]

def book_seat(row, seat):
    if 0 <= row < num_rows and 0 <= seat < section1 + section2 + section3:
        if auditorium[row][seat] == "-":
            auditorium[row][seat] = "*"
            print(f"Seat ({row+1}, {seat+1}) booked successfully!")
        else:
            print(f"Seat ({row+1}, {seat+1}) is already booked.")
    else:
        print("Invalid seat number. Please try again.")

while True:
    print("\nCurrent Seating Arrangement:")
    for row in auditorium:
        print(" ".join(row[:section1]), end="   ") 
        print(" ".join(row[section1:section1+section2]), end="   ")  
        print(" ".join(row[section1+section2:]))  
    
    choice = input("\nDo you want to book a seat? (yes/no): ").lower()
    if choice == "no":
        break

    row = int(input("Enter row number to book (1 to {}): ".format(num_rows))) - 1
    seat = int(input("Enter seat number to book (1 to {}): ".format(section1 + section2 + section3))) - 1

    book_seat(row, seat)

print("\nFinal Auditorium Seating Arrangement:")
for row in auditorium:
    print(" ".join(row[:section1]), end="   ")
    print(" ".join(row[section1:section1+section2]), end="   ")
    print(" ".join(row[section1+section2:]))

print("Booking process complete. Enjoy the show! 🎭")
        