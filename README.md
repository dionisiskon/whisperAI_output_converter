# whisper AI output converter
Converts the text format into the subtitle format, and the reverse.

A simple script to convert WhisperAI terminal or txt output to srt. I used it, because the srt format didn't come out that great with the command. Also, in some executions I forgot to include the output format and had to work with a terminal output, so I used the converter to convert instead of running it again. It is bothersome to run again, especially if the running of WhisperAI took hours previously.

# Example
python3 ./convert.py ./file_name.txt -> It converts into srt 

python3 ./convert.py ./file_name.srt -> It converts into txt

# Outputs 
file_name.txt -> Convert to srt -> file_name.srt 

file_name.srt -> Convert to txt -> file_name.txt

# Examples
## TXT
![WhisperAI txt](/images/txt_example.png)
## SRT
![WhisperAI srt](/images/srt_example.png)
