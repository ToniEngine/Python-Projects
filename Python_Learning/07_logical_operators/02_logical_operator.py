# If applicant has high income AND good credit
#       ELIGIBLE FOR LOAN
# We use logical operators to combine two conditons


# === USING THE LOGICAL AND OPERATOR
has_high_income = False
has_good_credit = True
has_criminal_record = True


if has_high_income and has_good_credit:
    print("Eligible for loan")
else:
    print("Ineligible for loan")


# ==== USING THE LOGICAL OR OPERATOR ====
# If applicant has high income OR good credit
#       ELIGIBLE FOR LOAN
 

if has_high_income or has_good_credit:
    print("Eligible for loan")
else:
    print("Ineligible for loan")



# AND: Both Conditions should be True
# OR: At least one condition or both should be True


# ==== USING THE LOGICAL NOT OPERATOR ====
# If applicant has good credit and doesn't have any criminal record
#       ELIGIBLE FOR LOAN

if has_good_credit and not has_criminal_record:
    print("Eligible for loan")
else:
    print("Eligible for loan")
