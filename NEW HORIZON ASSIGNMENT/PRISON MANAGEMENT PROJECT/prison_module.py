"""
These functions will collect, store and update prisoners records and information
"""
import os
import time
import random


# generate a cell ID for a new prisoner
def random_id():
    number_list = []
    k = 1
    while k <= 4:
        number = random.randint(0, 9)
        number_list.append(number)
        k += 1
    s = [str(i) for i in number_list]
    res = (''.join(s))
    return res


# collect prisoner information for data processing
def prisoner_data(prisoner_id, f_name, l_name, sex, dob, height, marital_status, crime_committed, date_of_sentence, time_duration, cell_no, tm):
    if os.path.isfile("Prisoner.txt") is False:
        print("\n---Can't write to Prisoner.txt, file not found---")
    else:
        file_handle = open("Prisoner.txt", "a")

        file_handle.write("\n")
        file_handle.write(prisoner_id)
        file_handle.write("\t\t\t\t")
        file_handle.write(f_name)
        file_handle.write("\t\t\t\t\t\t\t\t\t\t\t\t\t ")
        file_handle.write(l_name)
        file_handle.write("\t\t\t\t\t\t\t\t\t\t\t\t\t ")
        file_handle.write(sex)
        file_handle.write("\t\t\t")
        file_handle.write(dob)
        file_handle.write("\t\t\t\t")
        file_handle.write(height)
        file_handle.write("\t\t\t\t\t\t")
        file_handle.write(marital_status)
        file_handle.write("\t\t\t\t\t")
        file_handle.write("({})".format(crime_committed))
        file_handle.write("\t\t\t\t\t\t\t")
        file_handle.write("({})".format(date_of_sentence))
        file_handle.write("\t\t\t\t\t\t")
        file_handle.write(time_duration)
        file_handle.write("\t\t\t\t\t\t\t\t")
        file_handle.write(cell_no)
        file_handle.write("\t\t\t")
        file_handle.write("({})".format(tm))
        file_handle.write("\n")

        print("\n\n---File updated successfully---")
        file_handle.close()
    date = time.ctime()
    print("\nFile updated at", date)


# collect visitor information for data processing
def visitor_data(visitor_id, f_name, l_name, sex, phone_num, reason_for_visit, date_of_visit, tm):
    if os.path.isfile("Visitor.txt") is False:
        print("\n---Can't write to Visitor.txt, file not found---")
    else:
        file_handle = open("Visitor.txt", "a")

        file_handle.write("\n")
        file_handle.write(visitor_id)
        file_handle.write("\t\t\t")
        file_handle.write(f_name)
        file_handle.write("\t\t\t\t\t\t\t\t\t\t\t\t\t ")
        file_handle.write(l_name)
        file_handle.write("\t\t\t\t\t\t\t\t\t\t\t\t\t ")
        file_handle.write(sex)
        file_handle.write("\t\t\t")
        file_handle.write(phone_num)
        file_handle.write("\t\t\t\t")
        file_handle.write("({})".format(reason_for_visit))
        file_handle.write("\t\t\t\t\t\t")
        file_handle.write("({})".format(date_of_visit))
        file_handle.write("\t\t\t")
        file_handle.write("({})".format(tm))
        file_handle.write("\n")

        print("\n\n---File updated successfully---")
        file_handle.close()
    date = time.ctime()
    print("\nFile updated at", date)


# view all prisoners data when query is sent
def all_prisoners_data():
    if os.path.isfile("Prisoner.txt") is False:
        print("\n---Can't write to Prisoner.txt, file not found---")
    else:
        file_handle = open("Prisoner.txt", "r")
        for i in file_handle:
            result = i.split()
            if result:
                print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t{} {} DETAILS".format(result[1], result[2]))
                print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t=======================\n")
                print("[PRISONER_ID: {}, FIRST NAME: {}, LAST NAME: {}, SEX: {}, DATE OF BIRTH: {}, HEIGHT(cm): {}, MARITAL_STATUS: {}, CRIME_COMMITTED: {}, DATE_OF_SENTENCE: {}, TIME_DURATION(months): {}, CELL_NUMBER: {}]".format(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8], result[9], result[10]))
        file_handle.close()
    date = time.ctime()
    print("\nFile viewed at", date)


# view one prisoner data when query is sent
def one_prisoner_data():
    wrong_prisoner_id = ""
    p_id = input("\n    \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter prisoner ID: ")
    if p_id == wrong_prisoner_id:
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t ---Error message: Invalid Prisoner ID---")
        return one_prisoner_data()

    if os.path.isfile("Prisoner.txt") is True:
        file_handle = open("Prisoner.txt", "r")
        for i in file_handle:
            if i.startswith(p_id) is True:
                result = i.split()
                print("\n{} {} DETAILS".format(result[1], result[2]))
                print("=======================\n")
                print("Prisoner ID: {}".format(result[0]))
                print("First Name: {}".format(result[1]))
                print("Last Name: {}".format(result[2]))
                print("Sex: {}".format(result[3]))
                print("Age: {}".format(result[4]))
                print("Height: {}".format(result[5]))
                print("Marital Status: {}".format(result[6]))
                print("Crime Committed: {}".format(result[7]))
                print("Date of Sentence: {}".format(result[8]))
                print("Time Duration: {}".format(result[9]))
                print("Cell number: {}".format(result[10]))
                print("=======================\n")


# view all visitors data when query is sent
def all_visitors_data():
    if os.path.isfile("Visitor.txt") is False:
        print("\n---Can't write to Visitor.txt, file not found---")
    else:
        file_handle = open("Visitor.txt", "r")
        for i in file_handle:
            result = i.split()
            if result:
                print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t{} {} DETAILS".format(result[1], result[2]))
                print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t=======================\n")
                print("[VISITOR_ID: {}, FIRST NAME: {}, LAST NAME: {}, SEX: {}, PHONE NUMBER: {}, REASON FOR VISIT: {}, DATE OF VISIT: {}]".format(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7]))
        file_handle.close()
    date = time.ctime()
    print("\nFile viewed at", date)


# view one visitor data when query is sent
def one_visitor_data():
    wrong_visitor_id = ""
    v_id = input("\n    \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter visitor ID: ")
    if v_id == wrong_visitor_id:
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t ---Error message: Invalid Visitor ID---")
        return one_visitor_data()

    if os.path.isfile("Visitor.txt") is True:
        file_handle = open("Visitor.txt", "r")
        for i in file_handle:
            if i.startswith(v_id) is True:
                result = i.split()
                print("\n{} {} DETAILS".format(result[1], result[2]))
                print("=======================\n")
                print("Visitor ID: {}".format(result[0]))
                print("First Name: {}".format(result[1]))
                print("Last Name: {}".format(result[2]))
                print("Sex: {}".format(result[3]))
                print("Phone number: {}".format(result[4]))
                print("Reason For Visit: {}".format(result[5]))
                print("Date of Visit: {}".format(result[6]))
                print("=======================\n")


# backup prisoners data
def prisoner_data_backup(p_id):
    if os.path.isfile("Prisoner.txt") is False:
        print("\n---Can't write to Prisoner.txt, file not found---")
    else:
        file_handle = open("Prisoner.txt", "r")
        for i in file_handle:
            if not i.startswith(p_id):
                continue
            result = "".join(i)
            if os.path.isfile("PRISONER_BACKUP.txt") is False:
                print("\n---Can't write to Prisoner_backup.txt, file not found---")
            else:
                file_handle = open("PRISONER_BACKUP.txt", "a")

                file_handle.write("\n")
                file_handle.write(result)
                file_handle.write("\n")

                file_handle.close()


# backup visitors data
def visitor_data_backup(v_id):
    if os.path.isfile("Visitor.txt") is False:
        print("\n---Can't write to Visitor.txt, file not found---")
    else:
        file_handle = open("Visitor.txt", "r")
        for i in file_handle:
            if not i.startswith(v_id):
                continue
            result = "".join(i)
            if os.path.isfile("VISITOR_BACKUP.txt") is False:
                print("\n---Can't write to Visitor_backup.txt, file not found---")
            else:
                file_handle = open("VISITOR_BACKUP.txt", "a")

                file_handle.write("\n")
                file_handle.write(result)
                file_handle.write("\n")

                file_handle.close()
