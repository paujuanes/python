def computegrade(score):
    if score > 1.0 or score < 0.0 :
        print('The score is out of range.')
        quit()
    else:
        if score >= 0.9 :
            return 'A'
        elif score >= 0.8 :
            return 'B'
        elif score >= 0.7 :
            return 'C'
        elif score >= 0.6 :
            return 'D'
        elif score >= 0.5 :
            return 'E'
        else:
            return 'F'

scores = input('Enter a score between 0.0 and 1.0:\n')

fscore = float(scores)

scr = computegrade(fscore)
print('Your grade is:', scr)