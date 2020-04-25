# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    csvreader.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dochoi <dochoi@student.42seoul.kr>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/25 18:52:57 by dochoi            #+#    #+#              #
#    Updated: 2020/04/25 20:05:42 by dochoi           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import csv

class CsvReader(object):
    def __init__(self, fname, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.sep = sep
        self.header =header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.fname = fname

    def __enter__(self):# with start
        try:
            self.fd = open(self.fname)
            if len(self.fd.readlines()) > 1000:
                print("crpt")
                return None
            else:
                self.fd.close()
                self.fd = open(self.fname)
                return self
        except FileNotFoundError:
            print("Not Found")
            return None


    def __exit__(self, type, value, traceback):#with end
        self.fd.close()

    def getdata(self):
        temp = list(line.split(self.sep) for line in self.fd.read().splitlines())
        if (self.skip_top != 0):
            del temp[0]
        elif (self.skip_bottom != 0):
            del temp[-1]
        return temp

    def getheader(self):
        if self.header == None :
            print("no header")
            return None
        temp = list(line.split(self.sep) for line in self.fd.read().splitlines())
        return temp[0]

if __name__ == "__main__":
    # f = open('bad.csv','r')
    # rdr = csv.reader(f)
    # # print(list(rdr))
    # # for line in rdr:
    #     # print(line)

    # f.close()
    with CsvReader('good.csv') as file:
        if file == None:
            print("File is corrupted")
            exit()
        data = file.getdata()
        for line in data:
            print(line)
        # header = file.getheader()