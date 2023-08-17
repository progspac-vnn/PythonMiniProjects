# BMI Calculator ---> progspacvnn
print('********************************************************************************************')
print('////////////////BODY MASS INDEX CALCULATOR//////////////')

# Your Details
feet = int(input('Ft\n')) 
inch = float(input('Inch\n'))
weight = int(input('Enter Your Weight Here:\n'))

# Calculation
total_height = (feet*12) + inch
total_height_meters = (total_height * 0.0254)
BMI = (weight/(total_height_meters**2))

# Result
print(f'''##### HERE IS YOUR BMI ##### 
---------> {BMI}''')  

if BMI < 18.5:
    print('''UNDERWEIGHT. Choose nutrient-rich foods. ''')
if  18.5 <= BMI <= 24.9:
    print('''NORMAL. Leave out the word "weight". Keep working hard. ''')
if 25 <= BMI <= 29.9:
    print('''OVERWEIGHT. Encourage a healthy lifestyle, not just weight loss. ''')
if BMI >=30:
    print('''OBESE. Focus on process goals. ''')