# find the twinkle word is persent in the poem.txt file or not.
'''

f=open('poem.txt')
t=f.read()
if 'Twinkle' in t:
  print("Twinkle is persent in Poem")
else:
  print("Twinkle is not persent in poem")
f.close()

'''
'''
# Replace the old score with the new score.
def game():
  return 60
score=game()
with open('highscore.txt') as f:
  highscore=int(f.read())
if highscore<score:
  with open('highscore.txt', 'w') as f:
    f.write(str(score))

'''

# Create  table for kids.

for i in range(2, 21):
  with open(f"multiplication_table_of_{i}.txt",'w') as f:
    for j in range(1,11):
      f.write(f"{i}*{j}={i*j}")
      if j!=10:
        f.write('\n')
  break
