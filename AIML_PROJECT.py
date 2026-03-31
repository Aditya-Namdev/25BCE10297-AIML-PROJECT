#it will categorise on what i am spending on
Category = {
    "Food":["zomato", "swiggy", "mess", "canteen", "maggi", "tea"],
    "Academic":["books", "photocopy", "stationery", "exam", "assignment"],
    "Travel":["uber", "ola", "auto", "metro", "bus","train"],
    "Personal":["recharge", "haircut", "gym","shopping"] }

# it shows the daily budget is 1000
daily_budget=1000


#it acts as a pattern checker 
def spending_category(description):
    desc_lower = description.lower()
    for category, keywords in Category.items():
        for key in keywords:
            if key in desc_lower:
                return category
    return "Other"

#it makes decisions based on the amount and category
def expenditure(amount, category, current_total):
    new_total = current_total + amount
    advice = "Transaction logged."

    if new_total > daily_budget:
        advice = f" CRITICAL: You are {new_total - daily_budget} over your daily limit!"
    
    elif category == "Food" and amount > 250:
        advice = "AI Suggestion: High food expense detected. Consider the hostel mess for your next meal."
    
    elif new_total < (daily_budget * 0.5):
        advice = "Great job! You are well within your budget today."

    return advice, new_total


## --- Main Program Logic ---
print("--- AI Spending Tracker (Rule-Based Expert System) ---")
total_spent = 0

while True:
    desc = input("\nEnter expense description (or 'quit' to exit): ")
    if desc.lower()=='quit':
        break
        
    # it get details from the user   
    amt=float(input("Enter amount: "))
    
    category=spending_category(desc)
    advice, total_spent = expenditure(amt, category, total_spent)
    
    print(f"\n[AI Result]")
    print(f"Category: {category}")
    print(f"Advice: {advice}")
    print(f"Total spent today: {total_spent}")

print(f"\nFinal Summary: You spent a total of {total_spent} today.")