#Seat Booking 
available_seats = 10

while available_seats > 0:
    print(f"Available Seats: {available_seats}")
    booking=input("Confirm 'Yes/No' to Book Your Seats: ")
    
    if booking.lower() == "yes":
        available_seats -= 1
        print("Congratulations, Your Seat is Booked")
    
    else:
        print("Thank you for Considering us. Visit Again...")
        continue


    while available_seats >= 0:
        print(f"Available Seats: {available_seats}")
        booking1=input("Confirm again 'Yes/No' to Book your Seat: ")

        if booking1.lower() == "no" :
            available_seats += 1
            print("Your Seat is Cancelled")
            print("Thank You for Considering us. Visit Again...")
            break
           
        else: 
            print("Your Seat Booking is Confirmed")
            break


if available_seats==0:
    print("Booking Closed")
    


