file = [
'अ',
'आ',
'इ',
'ई',
'उ',
'ऊ',
'ए',
'ऎ',
'ऒ',
'औ',
'ॲ',
'क',
'ख',
'ग',
'घ',
'ङ',
'च',
'छ',
'ज',
'झ',
'ञ',
'ट',
'ठ',
'ड',
'ढ',
'ण',
'त',
'थ',
'द',
'ध',
'न',
'प',
'फ',
'ब',
'भ',
'म',
'य',
'र',
'ल',
'व',
'श',
'ष',
'स',
'क्ष',
'ह',
]

"""Getting Started Example for Python 2.7+/3.3+"""
from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import os
import sys
import subprocess
from tempfile import gettempdir

# Create a client using the credentials and region defined in the [adminuser]
# section of the AWS credentials file (~/.aws/credentials).
session = Session(profile_name="adminuser")
polly = session.client("polly")

for i, section in enumerate(file):
        try:
            # Request speech synthesis
            response = polly.synthesize_speech(Text=section, OutputFormat="mp3",
                                                VoiceId="Aditi")
        except (BotoCoreError, ClientError) as error:
            # The service returned an error, exit gracefully
            print(error)
            sys.exit(-1)

        # Access the audio stream from the response
        if "AudioStream" in response:
            # Note: Closing the stream is important because the service throttles on the
            # number of parallel connections. Here we are using contextlib.closing to
            # ensure the close method of the stream object will be called automatically
            # at the end of the with statement's scope.
                with closing(response["AudioStream"]) as stream:
                    output = os.path.join('/Users/vedaantsrivastava/movapp-data/sounds', f"sound{i}.mp3")
                    try:
                        # Open a file for writing the output as a binary stream
                            with open(output, "wb") as file:
                                file.write(stream.read())
                    except IOError as error:
                        # Could not write to file, exit gracefully
                        print(error)
                        sys.exit(-1)
