def currency_notes(amount):
    notes = [2000, 500, 200, 100, 50,10,5,1]
    notes_count ={}
    for note in notes:
        if amount >= note:
            notes_count[note] = amount // note
            amount = amount % note
    for key, value in notes_count.items():
        print(f"{key}: {value}")
print(currency_notes(1234))  # Example usage