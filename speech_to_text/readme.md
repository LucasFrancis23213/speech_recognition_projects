# Azure Speech-to-Text Program

This Python program converts speech from audio files or real-time microphone input to text using the **Azure Cognitive Services Speech SDK**. It provides functionality for processing multiple audio files and converting the speech to text.

## Features
- **File-based Speech Recognition**: Converts speech from a given audio file to text.
- **Microphone-based Speech Recognition**: Captures real-time audio from the microphone and converts it to text.
- **Azure Speech Service Integration**: Uses Azure's powerful speech recognition engine.

## Requirements

- Python 3.11.5
- Azure Cognitive Services Speech SDK
- An active Azure account with the **Speech Service** set up

## Installation  
1. ```bash
    pip install -r requirement.txt  
    ```
2. Inside the root directory of the project, create a ``azure_config.py`` file that will store your Azure API key and region:  
    ```python
    config = {
        "API_KEY": "Your_Azure_Speech_API_Key",
        "SERVICE_REGION": "Your_Azure_Region"
    }
    ```

## Usage
### Running the Program
1. File-based Speech-to-Text:
    - To run the program and convert speech from pre-recorded audio files in a directory:
    - ``python main.py``  
    - The program will load all .wav files in the voice_sample directory, convert each file to text using Azure Speech SDK, and print the results.  
2. Microphone-based Speech-to-Text:
    - You can modify the program to capture real-time audio from your microphone by setting the ``transfer_microphone`` flag to True in the ``choose_mode`` function  