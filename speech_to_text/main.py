import os
from azure_speech_to_text import AzureSpeechRecognizer


# print(os.getcwd())
def load_every_vocal_file(path: str) -> list[str]:
    subfiles = os.listdir(path=path)
    result = []
    for file in subfiles:
        result.append(f'{path}/{file}')
    print('\n'.join(result))
    return result


def main():
    voice_samples = load_every_vocal_file('../voice_sample')
    speech_recognizer = AzureSpeechRecognizer()
    for sample in voice_samples:
        speech_recognizer.create_file_speech_recognizer(file_path=sample)
        speech_recognizer.choose_mode(transfer_file=True)
    convert_result = speech_recognizer.get_result(clear_result=True)
    print(f"convert result is \n {','.join(convert_result)}")


if __name__ == "__main__":
    main()
