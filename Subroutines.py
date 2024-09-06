1. Procedure
Pseudocode
  PROCEDURE your_information
    OUTPUT "Your name"
    OUTPUT "Your age"
    OUTPUT "Mr Dinh Duong, your are 16"
  ENDPROCEDURE
  CALL your_information
Python
  def your_information():
      print("Your name")
      print("Your age")
      print("Mr Dinh Duong, you are 16")
  your_information()

2. Conversion table
Pseudocode
  PROCEDURE mile_to_km
   INPUT mile : INTEGER
   km = mile * 1.6093
   OUTPUT mile, "miles =", km, "km"
  ENDPROCEDURE
  PROCEDURE inch_to_cm
   INPUT inch : INTEGER
   cm = inch * 1.6093
   OUTPUT inch, "inch =", cm, "cm"
  ENDPROCEDURE
  CALL mile_to_km
  CALL inch_to_cm
Python
  def mile_to_km():
      mile = int(input("how many miles: "))
      km = mile * 1.6093
      print(mile, 'miles =', km, 'km')
  
  def inch_to_cm():
      inch = int(input("how many inch: "))
      cm = inch * 2.54
      print(inch, 'inch =', cm, 'cm')
  menu()

4. Extension
    def menu():
        opp = int(input("choose your option '1' or '2': "))
        if opp == 1:
            mile_to_km()
        else:
            inch_to_cm()
    def mile_to_km():
        mile = int(input("how many miles: "))
        km = mile * 1.6093
        print(mile, 'miles =', km, 'km')
    
    def inch_to_cm():
        inch = int(input("how many inch: "))
        cm = inch * 2.54
        print(inch, 'inch =', cm, 'cm')
    menu()
       
