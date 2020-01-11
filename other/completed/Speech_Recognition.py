##########################################################################
# Challenge 03 
# Utility: Count number of words of a given  phrase 
# Uses:  Azure Speeech recognition service, Lists, split and join
##########################################################################
import azure.cognitiveservices.speech as speechsdk
import os
clearScreen = lambda: os.system('cls')

# Configure Microsoft AZURE Speech Service
# Replace with your own Microsoft AZURE subscription key and service region.
speech_key = "c3ceca58a2684030b5436f607efdc144"
service_region = "canadacentral"
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

#Listen and send sound to Microsoft Azure (Cloud) to recognize text
def ListenAndIdentityText():
    print('I am listening...')
    result = speech_recognizer.recognize_once()
    # Checks result.
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Recognized: {}".format(result.text))
        return result.text
    elif result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(result.no_match_details))
        return ""
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))
        return ""



def CountWords(phrase):
    #define a new empty list
    WordList = []
    #create a list based on provided "phrase" - split "phrase" based on space character (' ') 
    wordList = phrase.split(' ')
    #get number of items - in this case number of words of our phrase
    numerOfWords=len(wordList)
    return numerOfWords

    
clearScreen()
print("---------------------------------------------------------")
print("---- Challenge 03: Count number of words of a given  phrase  ---")
print("Say something:")
phrase = ListenAndIdentityText()
if(phrase!=""):
    result = CountWords(phrase)
    print("Got {0} words".format(result))
print("---------------------------------------------------------")