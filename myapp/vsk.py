from wsd.lesk import adapted_lesk

sent=raw_input('sentence : ')
ambiguous=raw_input('ambigiuty : ')
answer = adapted_lesk(sent, ambiguous, pos='n')
print answer
print answer.definition()
