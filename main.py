# Program for One Stop Insurance Company
# Author: Tristan Bailey        Date: 2022-12-03

NEXT_POLICY_NUM = 1944
BASIC_PREM = 869.00
DISCOUNT_ADD_CARS = .25
COST_EXTRA_LIA_COV = 130.00
COST_GLASS_COV = 86.00
COST_LOANER_CAR = 58.00
HST_RATE = .15
PROCESS_FEE = 39.99

f = open("OSICDef.dat", "w")

f.write("{}\n".format(str(NEXT_POLICY_NUM)))
f.write("{}\n".format(str(BASIC_PREM)))
f.write("{}\n".format(str(DISCOUNT_ADD_CARS)))
f.write("{}\n".format(str(COST_EXTRA_LIA_COV)))
f.write("{}\n".format(str(COST_GLASS_COV)))
f.write("{}\n".format(str(COST_LOANER_CAR)))
f.write("{}\n".format(str(HST_RATE)))
f.write("{}\n".format(str(PROCESS_FEE)))

f.close()

while True:

    CustFirstName = input("Enter the customers first name: ").title()
    CustLastName = input("Enter the customers last name: ").title()
    Address = input("Enter the customers address: ")
    City = input("Enter the customers city: ")
    Province = input("Enter the customers province: (ex: NL, BC, Etc..) ")
    PostalCode = input("Enter the customers postal code: ")
    CusPhoneNum = input("Enter the customers phone number: (ex: 999-999-9999) ")
    NumberCarsInsured = int(input("Enter the number of cars being insured: "))
    ExtraLia = input("Enter if you would like extra liability up to $1,000,000? (Y / N) ").upper()
    GlassCov = input("Enter if you would like glass coverage? (Y / N) ").upper()
    OptLoanCar = input("Enter if you would like a loner car? (Y / N) ").upper()
    PayOption = input("Enter the payment option you would like Full or Monthly? (F / M) ").upper()

    if NumberCarsInsured == 1:
        InsurePrem = BASIC_PREM
    elif NumberCarsInsured > 1:
        InsurePrem = BASIC_PREM + (NumberCarsInsured - 1) * (BASIC_PREM * DISCOUNT_ADD_CARS)

    TotalExtra = 0
    if ExtraLia == "Y":
        TotalExtra += NumberCarsInsured * COST_EXTRA_LIA_COV

    if GlassCov == "Y":
        TotalExtra += NumberCarsInsured * COST_GLASS_COV

    if OptLoanCar == "Y":
        TotalExtra += NumberCarsInsured * COST_LOANER_CAR

    TotalPremium = TotalExtra + InsurePrem
    Hst = TotalPremium * HST_RATE
    TotalCost = TotalPremium + Hst

    MonPayment = (TotalCost + PROCESS_FEE) / 8

    print()
    print("     One Stop Insurance Company     ")
    print()
    print("------------------------------------")
    print("Customer's Name: " + CustFirstName, CustLastName)
    print(f"Customer's Phone Number:  {CusPhoneNum}")
    print(f"Customer's Address: {Address}")
    print("                    ", City + ",", Province)
    print("                    ", PostalCode)
    print("------------------------------------")
    print(f"Number of cars insured: {NumberCarsInsured}")
    print(f"Extra Liability: {ExtraLia}")
    print(f"Glass Coverage:  {GlassCov}")
    print(f"Loaner Car:      {OptLoanCar}")
    print(f"Payment Option:  {PayOption}")
    print("------------------------------------")
    InsurePremDSP = "${:,.2f}".format(InsurePrem)
    print(f"Insurance Premiums:  {InsurePremDSP} ")
    TotalExtraDSP = "${:,.2f}".format(TotalExtra)
    print(f"Total Extra Cost:    {TotalExtraDSP}")
    TotalPremiumDSP = "${:,.2f}".format(TotalPremium)
    print(f"Total Insurance Premium: {TotalPremiumDSP}")
    HstDSP = "${:,.2f}".format(Hst)
    print(f"Taxes(HST):          {HstDSP}")
    TotalCostDSP = "${:,.2f}".format(TotalCost)
    print(f"Total Cost:          {TotalCostDSP}")
    print("------------------------------------")
    MonPaymentDSP = "${:,.2f}".format(MonPayment)
    if PayOption == "M":
        print(f"Monthly Payment:     {MonPaymentDSP}")
        print("------------------------------------")

    f = open("Policies.dat", "a")

    f.write("{}, ".format(NEXT_POLICY_NUM))
    f.write("{}, ".format(CustFirstName))
    f.write("{}, ".format(CustLastName))
    f.write("{}, ".format(Address))
    f.write("{}, ".format(City))
    f.write("{}, ".format(Province))
    f.write("{}, ".format(PostalCode))
    f.write("{}, ".format(CusPhoneNum))
    f.write("{}, ".format(NumberCarsInsured))
    f.write("{}, ".format(ExtraLia))
    f.write("{}, ".format(GlassCov))
    f.write("{}, ".format(OptLoanCar))
    f.write("{}, ".format(PayOption))
    f.write("{}\n".format(TotalCost))

    print()
    print("Policy information processed and saved!")
    print()
    NEXT_POLICY_NUM += 1

    Option = input("Would you like to process another claim? (Y / N) ").upper()
    print()
    if Option == "N":
        break

    f.close()

    f = open("OSICDef.dat", "w")

    f.write("{}\n".format(NEXT_POLICY_NUM))
    f.write("{}\n".format(BASIC_PREM))
    f.write("{}\n".format(DISCOUNT_ADD_CARS))
    f.write("{}\n".format(COST_EXTRA_LIA_COV))
    f.write("{}\n".format(COST_GLASS_COV))
    f.write("{}\n".format(COST_LOANER_CAR))
    f.write("{}\n".format(HST_RATE))
    f.write("{}\n".format(PROCESS_FEE))

    f.close()