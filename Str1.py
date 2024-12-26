corr_ans=0
wrng_ans=0
print('1. What is the capital of India?',)
user_ans=input('Enter ans :').lower()
if user_ans=='delhi':
    print('Correct ans')
    corr_ans+=1
else:
    print('Wrong ans')
    wrng_ans+=1
print('2. What is the colour of apple?')
user_ans=input('Enter ans :').lower()
if user_ans=='red':
    print('Correct ans')
    corr_ans+=1
else:
    print('Wrong ans')
    wrng_ans+=1
print('3. What is the national animal of India?')
user_ans=input('Enter ans :').lower()
if user_ans=='tiger':
    print('Correct ans')
    corr_ans+=1
else:
    print('Wrong ans')
    wrng_ans+=1
print('4. What is the nationalbird of India?')
user_ans=input('Enter ans :').lower()
if user_ans=='peacock':
    print('Correct ans')
    corr_ans+=1
else:
    print('Wrong ans')
    wrng_ans+=1
print('5. Who is the current PM of India?')
user_ans=input('Enter ans :').lower()
if user_ans=='Modi':
    print('Correct ans')
    corr_ans+=1
else:
    print('Wrong ans')
    wrng_ans+=1
print('percentage :',corr_ans/(corr_ans+wrng_ans)*100)


# Nested list!!!
att=[1,4,532,543,[324,5,42],8]
print(att[5])