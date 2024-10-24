import os
import azure.cognitiveservices.speech as speech_sdk

from azure_config import config

print(os.getcwd())


class AzureSpeechRecognizer:

    def __init__(self):
        self.speech_config = self.create_speech_config()
        self.file_speech_recognizer = None
        self.microphone_speech_recognizer = self.create_microphone_speech_recognizer(self)
        self.result = []

    @staticmethod
    def create_speech_config():
        speech_config = speech_sdk.SpeechConfig(
            subscription=config["API_KEY"],
            region=config["SERVICE_REGION"]
        )
        return speech_config

    def create_file_speech_recognizer(self, file_path: str = None):
        if file_path is not None:
            audio_config = speech_sdk.AudioConfig(filename=file_path)
            self.file_speech_recognizer = speech_sdk.SpeechRecognizer(
                speech_config=self.speech_config,
                audio_config=audio_config
            )
            return self.file_speech_recognizer

    @staticmethod
    def create_microphone_speech_recognizer(self) -> speech_sdk.SpeechRecognizer:
        audio_config = speech_sdk.AudioConfig(use_default_microphone=True)
        speech_recognizer = speech_sdk.SpeechRecognizer(
            audio_config=audio_config,
            speech_config=self.speech_config
        )
        return speech_recognizer

    def choose_mode(self, transfer_file: bool = False, transfer_microphone: bool = False):
        if transfer_file and self.file_speech_recognizer is not None:
            return self.speech_to_text(speech_recognizer=self.file_speech_recognizer)
        if transfer_microphone:
            return self.speech_to_text(speech_recognizer=self.microphone_speech_recognizer)

    def speech_to_text(self, speech_recognizer: speech_sdk.SpeechRecognizer):
        result = speech_recognizer.recognize_once()
        if result.reason == speech_sdk.ResultReason.RecognizedSpeech:
            print(f"Recognized: {result.text}")
            self.result.append(result.text)
            return result.text
        elif result.reason == speech_sdk.ResultReason.NoMatch:
            print("No speech could be recognized.")
            self.result.append("no text detected")
            return 'no text detected'
        elif result.reason == speech_sdk.ResultReason.Canceled:
            cancellation_details = result.cancellation_details
            print(f"Speech Recognition canceled: {cancellation_details.reason}")
            if cancellation_details.reason == speech_sdk.CancellationReason.Error:
                print(f"Error details: {cancellation_details.error_details}")
            self.result.append("no text detected")
            return 'no text detected'

    def get_result(self, clear_result: bool = True):
        if clear_result:
            ans = self.result
            self.result.clear()
            return ans
        else:
            return "\n".join(self.result)


def sample():
    audio_path = "../voice_sample/soul-society-japanese-spoken-shot.wav"
    azure_speech_recognizer = AzureSpeechRecognizer()
    azure_speech_recognizer.create_file_speech_recognizer(file_path=audio_path)
    azure_speech_recognizer.choose_mode(transfer_file=True)
    print(azure_speech_recognizer.get_result())

#
# if __name__ == '__main__':
#     main()
