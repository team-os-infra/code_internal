import re
from datetime import datetime


filename = 'textfile.txt'
pattern  = '.*RF.*'
new_file = []

FMT = '%H:%M:%S'


prog_zero_list = []


try:
    # Make sure file gets closed after being iterated
    with open(filename, 'r') as f:
        # Read the file contents and generate a list with each line
        lines = f.readlines()

        progression_list = []

        prog_list = []


        # Iterate each line
        for line in lines:

            # Regex applied to each line
            match = re.search(pattern, line)
            if match:
                # Make sure to add \n to display correctly when we write it back
                new_line = match.group() + '\n'
                #progression_list = []
                progression_list = new_line.split()
                progression_list[2:len(progression_list) - 2] = [''.join(progression_list[2:len(progression_list) - 2])]

                prog_list.append(progression_list)

        #print(prog_list)

        cleanlist = []

        zero_client_list = []

        client_list = []
        client_time = []


        dict  = {}

        for x in prog_list:
            if x not in cleanlist:
                if (x[-1] == "rc=0" or x[-1] == "rc=11"):
                    cleanlist.append(x)
        #print(cleanlist)

        print("Clients taking time :")
        print("=====================================================================")
        print('{:10s} {:<38s} {:<10s}'.format("S.N" ,"Client Name ", "Client Time"))
        print("=====================================================================")
        for index in range(len(cleanlist)):
            client_name = cleanlist[index][2]
            client_rc = cleanlist[index][-1]
            client_time1 = cleanlist[index][0]
            if client_rc == "rc=0":
                for ind in range(len(cleanlist)):
                    if ind > index:
                        if(cleanlist[ind][2] == client_name and cleanlist[ind][-1] == "rc=11"):
                            client_time2 = cleanlist[ind][0]
                            delta = datetime.strptime(client_time2, FMT) - datetime.strptime(client_time1, FMT)
                            #print("client_name :\t" + client_name +  "\t\t\t\t\t\t\t" + "client time :\t" + str(delta) )


                            dict[client_name] = str(delta)
                            #print(dict)

                            #print('{:<50s} {:<10s}'.format(client_name, str(delta)))
                            break

        #for key, value in dict.items():
            #print(f'{key:52}{value}')


        # sort the dictionary based on max time taken
        sort_dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)

        count =0
        no_of_prog = 0
        for i in sort_dict:
            count = count +1
            no_of_prog = no_of_prog + 1
            if(no_of_prog < 25 ):
                #print('{:20} {:<40s} {:<10s}'.format(count , i[0], i[1]))
                print('{:10s} {:<39s} {:<10s}'.format(str(count), i[0], i[1]))

        print("=====================================================================")


except IOError:
    print("File not Found")
