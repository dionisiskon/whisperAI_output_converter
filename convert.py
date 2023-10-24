import sys
timecaps = []
script = []

if len(sys.argv) < 2:
    print("\nYou haven't included the text in the cmd prompt.\n\nExample: python3 ./convert.py ./myfile.\n")
else:
    ext = sys.argv[1][-3:]
    if ext == 'txt':
        print('\nText file detected!\n')
        print('Converting to srt...\n')
        with open(sys.argv[1]) as f:
            lines = f.readlines()
            for line in lines:
                splitter = line.split(']  ')
                timecaps.append(splitter[0])
                script.append(splitter[1])
        output = sys.argv[1][:-4] + '.srt'
        with open(output, 'w') as file1:
            for i in range(len(timecaps)):
                timecap_split = timecaps[i].split('-->')
                file1.write(str(i+1) + '\n')
                if len(timecap_split[0]) == 11:
                    file1.write('00:' + timecap_split[0].replace('[','') + '-->' + ' 00:' + timecap_split[1].replace(' ','') + '\n') 
                else:
                    file1.write(timecap_split[0].replace('[','') + '-->' + ' ' + timecap_split[1].replace(' ','') + '\n')
                file1.write(script[i] + '\n')
        print('Conversion is finished!\n')
    elif ext == 'srt':
        print('\nSubtitle file detected!\n')
        print('Converting to txt...\n')
        with open(sys.argv[1]) as f:
            lines = f.readlines()
            for i in range(1, len(lines), 4):
                timecaps.append(lines[i])
            for i in range(2, len(lines), 4):
                script.append(lines[i])
        first_time = ''
        second_time = ''
        output = sys.argv[1][:-4] + '.txt'
        with open(output, 'w') as file1:
            for i in range(len(timecaps)):
                split_into = timecaps[i].split(' --> ')
                if split_into[0].startswith('00:'):
                    first_time = split_into[0][3:]
                else:
                    first_time = split_into[0]
                if split_into[1].startswith('00:'):
                    second_time = split_into[1][3:]
                else:
                    second_time = split_into[1]
                second_time = second_time.replace('\n', '')
                file1.write('[' + first_time + ' --> ' + second_time + ']  ' + script[i])
        print('Conversion is finished!\n')


