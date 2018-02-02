yesterday_seat_assignments = [
    "Moses",
    "Ashley",
]
today_seat_assignments = [
    "Nick",
    "Ashley",
]
for seat in range(0,len(yesterday_seat_assignments)):
    if yesterday_seat_assignments[seat] == today_seat_assignments[seat]:
        print(f"Hey, {yesterday_seat_assignments[seat]} can't sit here");
