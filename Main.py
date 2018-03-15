from VRec import getSpeech
import time
import pyautogui

speech = getSpeech()
print('----------------------------------\n\n')
TriggerWords = [['right',False],['write',False],['stop',False]]

write = []

for wordSpoken in speech:
    print(wordSpoken)
    for item in TriggerWords:
        if wordSpoken.lower() == item[0].lower():
            print('---caught---')
            item[1] = True

    if TriggerWords[2][1] == True:
        TriggerWords[0][1] = False
        TriggerWords[1][1] = False
    if (TriggerWords[0][1] == True or TriggerWords[1][1] == True):
        if not (TriggerWords[0][0] == wordSpoken or TriggerWords[1][0] == wordSpoken):
            write.append(wordSpoken)

print(write)
if not write == []:
    print('Writing in 3...')
    time.sleep(.5)
    print('2...')
    time.sleep(.5)
    print('1...')
    time.sleep(.5)
    for item in write:
        pyautogui.typewrite(item,interval=.05)
        pyautogui.keyDown('space')