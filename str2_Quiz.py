question=['1. What is the capital of India?',
          '2. What is the colour of apple?',
          '3. What is the national animal of India?',
          '4. What is the nationalbird of India?',
          '5. Who is the current PM of India?']
          
ans=['delhi','red','tiger','peacock','modi']
for x in range(len(question)):
    print(question[x])
    user_ans=input('Enter ans :').lower()
    if user_ans == ans[x]:
        print('Correct ans')
    else:
        print('Wrong ans') 
        # wrong_ans=wrong_ans+1
# print('percentage :',corr_ans/(corr_ans+wrong_ans)*100)