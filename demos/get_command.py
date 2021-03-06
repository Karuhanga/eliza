import speech_recognition as sr

from utils.constants import COMMAND_SCOPE


def get_command(command_scope):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            audio = r.listen(source, timeout=2, phrase_time_limit=5)
        except sr.WaitTimeoutError:
            print("Wait timeout")
            return

    try:
        return r.recognize_google_cloud(audio, language="en-KE", preferred_phrases=command_scope).strip()
    except sr.UnknownValueError:
        print("Google Cloud Speech could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Cloud Speech service; {0}".format(e))


if __name__ == "__main__":
    command = get_command(command_scope=COMMAND_SCOPE)
    if command:
        print(command)
    else:
        print("Failed to recognize word")
