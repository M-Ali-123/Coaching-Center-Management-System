
import numpy as np
import csv
import os
# CLASS9_FILENAME = 'class_9.csv'

class CoachingCenter:
    def __init__(self):
        room_limit = 100

        #  Class 9 arrays
        self.N9 = 0
        self.class9 = np.array([['' for i in range(7)]for j in range(room_limit)],dtype=object)
        self.courses9 = np.array([['' for i in range(8)] for j in range(100)],dtype=object)

        # class 10 Array
        self.N10 = 0
        self.class10 = np.array([['' for i in range(7)]for j in range(room_limit)],dtype=object)
        self.courses10 = np.array([['' for i in range(8)] for j in range(100)],dtype=object)

        #  Class 11 array
        self.N11 = 0
        self.class11 = np.array([['' for i in range(7)]for j in range(room_limit)],dtype=object)
        self.courses11 = np.array([['' for i in range(8)] for j in range(100)],dtype=object) 

        #  Class 12 array
        self.N12 = 0
        self.class12 = np.array([['' for i in range(7)]for j in range(room_limit)],dtype=object)
        self.courses12 = np.array([['' for i in range(8)] for j in range(100)],dtype=object) 

        # class CIT
        self.C=0
        self.Cit= np.array([['' for i in range(8)]for j in range(room_limit)],dtype=object)
        
        # MARKS ARRAY
        
        self.Marks9= np.array([[''for i in range(15)]for j in range(100)],dtype=object)  
        self.Marks10=np.array([[''for i in range(15)]for j in range(100)],dtype=object)  
        self.Marks11=np.array([[''for i in range(15)]for j in range(100)],dtype=object)  
        self.Marks12=np.array([[''for i in range(15)]for j in range(100)],dtype=object)
        

        self.M9=0
        self.M10=0
        self.M11=0
        self.M12=0
  
    
        self.load(1)
        self.load(9)
        self.load(10)
        self.load(11)
        self.load(12)

    def enroll_students(self):
        class_ = int(input('Enter classno (in digit, eg 9,10,11,12) and press 1 for CIT '))
        name = input('Enter name ')
        fname = input('Enter father name ')
        age=input('Enetr age of Student  : ')
        contact=input('Enter Contact number  : ')
        Date=input('Enter Date Of joining : ')
        fees9=0
        fees10=0
        fees11=0
        fees12=0
        if class_==9:
            self.courses9[self.N9][0]=str(self.N9+1)
            no_of_courses_enrolled = 1

            while no_of_courses_enrolled < 7:
                print()
                print('Select  your courses')
                print(' press \n 1 for Biology \n 2 for Math \n 3 for English \n 4 for CHemistry \n 5 for Sindhi \n 6 for Physics \n7 for Conmputer \n 8 to go Back')
                no=int(input('Enter : '))
                
                if no ==1:
                    if 'Biology' not in self.courses9[self.N9] and 'Computer' not in self.courses9[self.N9]:
                        self.courses9[self.N9][no_of_courses_enrolled]='Biology'
                        fees9+=2000
                        print('Added Successfully')
                        no_of_courses_enrolled+=1
                    else :
                        print('ALready added')
                elif no==2:
                    if 'Math' not in self.courses9[self.N9]:
                        self.courses9[self.N9][no_of_courses_enrolled]='Math'
                        fees9+=2000
                        no_of_courses_enrolled+=1
                        print('Added Successfully')
                    else :
                        print('ALready added')
                elif no==3:
                    if 'English' not in self.courses9[self.N9]: 
                        self.courses9[self.N9][no_of_courses_enrolled]='English'
                        fees9+=2000
                        no_of_courses_enrolled+=1
                        print('Added Successfully')
                    else :
                        print('ALready added')
                elif no==4:
                    if 'Chemistry' not in self.courses9[self.N9]: 
                        self.courses9[self.N9][no_of_courses_enrolled]='Chemistry'
                        fees9+=2000
                        no_of_courses_enrolled+=1
                        print('Added Successfully')
                    else :
                        print('ALready added')
                elif no==5:
                    if 'Sindhi' not in self.courses9[self.N9]: 
                        self.courses9[self.N9][no_of_courses_enrolled]='Sindhi'
                        fees9+=2000
                        no_of_courses_enrolled+=1
                        print('Added Successfully')
                    else :
                        print('ALready added')
                elif no==6:
                    if 'Physiics' not in self.courses9[self.N9]: 
                        self.courses9[self.N9][no_of_courses_enrolled]='Physiics'
                        fees9+=2000
                        no_of_courses_enrolled+=1
                        print('Added Successfully')
                    else :
                        print('ALready added')
                elif no==7:
                    if 'Computer' not in self.courses9[self.N9] and 'Biology' not in self.courses9[self.N9]: 
                        self.courses9[self.N9][no_of_courses_enrolled]='Computer'
                        fees9+=2000
                        no_of_courses_enrolled+=1
                        print('Added Successfully')
                    else :
                        print('ALready added')
                elif no ==8:
                    break
                
                else:
                    print('Invlaid  option')

            
            self.class9[self.N9][0] = str(self.N9+1)
            self.class9[self.N9][1] = name
            self.class9[self.N9][2] = fname
            self.class9[self.N9][3] = age
            self.class9[self.N9][4] = contact
            self.class9[self.N9][5] = Date
            self.class9[self.N9][6] = str(fees9)

            self.N9 += 1
            # To print(student informationt that has been added)
            for i in range(self.N9-1,-1,-1):
                print('Student Data')
                print()
                print('SID     Name    Father   Age    Contact   Date    Fees')

                for j in range(len(self.class9[i])):
                    print(self.class9[i][j], end='\t')
                print()
                print('Courses')
                for j in range(len(self.courses9[i])):
                    print(self.courses9[i][j], end=' ')
                break
            print()
            
                # send data to  save function and store it 
            self.saves('class9th.csv', self.class9, self.N9)
            self.saves('courses9th.csv', self.courses9, self.N9)
            
        
        elif class_==10:
            self.courses10[self.N10][0]=str(self.N10+1)
            no_of_courses_enrolled10 = 1

            while no_of_courses_enrolled10 <= 7:
                print()
                print('Select  your courses')
                print(' press \n 1 for Islamiat \n 2 for Math \n 3 for English \n 4 for CHemistry \n 5 for Physics \n6 for Urdu \n 7 for Sindhi \n 8 to go Back')
                no=int(input('Enter : '))
                
                if no ==1:
                    if 'Islamiat' not in self.courses10[self.N10]:
                        self.courses10[self.N10][no_of_courses_enrolled10]='Islamiat'
                        fees10+=2000
                        print('Added Successfully')
                        no_of_courses_enrolled10+=1
                    else :
                        print('ALready added')
                elif no==2 :
                    if 'Math' not in self.courses10[self.N10]:
                        self.courses10[self.N10][no_of_courses_enrolled10]='Math'
                        fees10+=2000
                        no_of_courses_enrolled10+=1
                        print('Added Successfully')
                    else :
                        print('ALready added')
                elif no==3 :
                    if 'English' not in self.courses10[self.N10]: 
                        self.courses10[self.N10][no_of_courses_enrolled10]='English'
                        fees10+=2000
                        no_of_courses_enrolled10+=1
                        print('Added Successfully')
                    else :
                        print('ALready added')
                elif no==4 :
                    if 'Chemistry' not in self.courses10[self.N10]: 
                        self.courses10[self.N10][no_of_courses_enrolled10]='Chemistry'
                        fees10+=2000
                        no_of_courses_enrolled10+=1
                        print('Added Successfully')
                    else :
                        print('ALready added')
                elif no==5 :
                    if 'Physiics' not in self.courses10[self.N10]: 
                        self.courses10[self.N10][no_of_courses_enrolled10]='Physiics'
                        fees10+=2000
                        no_of_courses_enrolled10+=1
                        print('Added Successfully')
                    else :
                        print('ALready added')
                elif no==6 :
                    if 'Urdu' not in self.courses10[self.N10]: 
                        self.courses10[self.N10][no_of_courses_enrolled10]='Urdu'
                        fees10+=2000
                        no_of_courses_enrolled10+=1
                        print('Added Successfully')
                    else :
                        print('ALready added')
                elif no==7 :
                    if 'Sindhi' not in self.courses10[self.N10]: 
                        self.courses10[self.N10][no_of_courses_enrolled10]='Sindhi'
                        fees10+=2000
                        no_of_courses_enrolled10+=1
                        print('Added Successfully')
                    else :
                        print('ALready added')
                elif no ==8:
                    break
                
                else:
                    print('Courses Full')

            
            self.class10[self.N10][0] = str(self.N10+1)
            self.class10[self.N10][1] = name
            self.class10[self.N10][2] = fname
            self.class10[self.N10][3] = age
            self.class10[self.N10][4] = contact
            self.class10[self.N10][5] = Date
            self.class10[self.N10][6] = str(fees10)

            self.N10 += 1
            # To print(student informationt that has been added)
            for i in range(self.N10-1,-1,-1):
                print()
                print('Student Data')
                print()
                print('SID     Name    Father   Age    Contact   Date    Fees')

                for j in range(len(self.class10[i])):
                    print(self.class10[i][j], end='\t')
                print()
                print('Courses')
                for j in range(len(self.courses10[i])):
                    print(self.courses10[i][j], end=' ')
                break
            print()
            
                # send data to  save function and store it 
            self.saves('class10th.csv', self.class10, self.N10)
            self.saves('courses10th.csv', self.courses10, self.N10)

        elif class_==11:
            self.courses11[self.N11][0]=str(self.N11+1)
            no_of_courses_enrolled = 1

            while no_of_courses_enrolled <= 7:
                print()
                print('Select  your courses')
                print(' press \n 1 for Biology \n 2 for Math \n 3 for English \n 4 for CHemistry \n 5 for Sindhi \n 6 for Physics \n7 for Conmputer \n 8 to go Back')
                no=int(input('Enter : '))
                
                if no ==1:
                    if 'Biology' not in self.courses11[self.N11] and 'Computer' not in self.courses11[self.N11]:
                        self.courses11[self.N11][no_of_courses_enrolled]='Biology'
                        fees11+=2000
                        print('Added Successfully')
                        no_of_courses_enrolled+=1
                    else :
                        print('ALready added')
                elif no==2:
                    if 'Math' not in self.courses11[self.N11]:
                        self.courses11[self.N11][no_of_courses_enrolled]='Math'
                        fees11+=2000
                        no_of_courses_enrolled+=1
                        print('Added Successfully')
                    else :
                        print('ALready added')
                elif no==3:
                    if 'English' not in self.courses9[self.N9]: 
                        self.courses11[self.N11][no_of_courses_enrolled]='English'
                        fees11+=2000
                        no_of_courses_enrolled+=1
                        print('Added Successfully')
                    else :
                        print('ALready added')
                elif no==4:
                    if 'Chemistry' not in self.courses11[self.N11]: 
                        self.courses11[self.N11][no_of_courses_enrolled]='Chemistry'
                        fees11+=2000
                        no_of_courses_enrolled+=1
                        print('Added Successfully')
                    else :
                        print('ALready added')
                elif no==5:
                    if 'Sindhi' not in self.courses11[self.N11]: 
                        self.courses11[self.N11][no_of_courses_enrolled]='Sindhi'
                        fees11+=2000
                        no_of_courses_enrolled+=1
                        print('Added Successfully')
                    else :
                        print('ALready added')
                elif no==6:
                    if 'Physiics' not in self.courses11[self.N11]: 
                        self.courses11[self.N11][no_of_courses_enrolled]='Physiics'
                        fees11+=2000
                        no_of_courses_enrolled+=1
                        print('Added Successfully')
                    else :
                        print('ALready added')
                elif no==7:
                    if 'Computer' not in self.courses11[self.N11] and 'Biology' not in self.courses11[self.N11]: 
                        self.courses11[self.N11][no_of_courses_enrolled]='Computer'
                        fees11+=2000
                        no_of_courses_enrolled+=1
                        print('Added Successfully')
                    else :
                        print('ALready added')
                elif no ==8:
                    break
                
                else:
                    print('Invlaid  option')

            
            self.class11[self.N11][0] = str(self.N11+1)
            self.class11[self.N11][1] = name
            self.class11[self.N11][2] = fname
            self.class11[self.N11][3] = age
            self.class11[self.N11][4] = contact
            self.class11[self.N11][5] = Date
            self.class11[self.N11][6] = str(fees11)

            self.N11 += 1
            # To print(student informationt that has been added)
            for i in range(self.N11-1,-1,-1):
                print('Student Data')
                print()
                print('SID     Name    Father   Age    Contact   Date    Fees')

                for j in range(len(self.class11[i])):
                    print(self.class11[i][j], end='\t')
                print()
                print('Courses')
                for j in range(len(self.courses11[i])):
                    print(self.courses11[i][j], end=' ')
                break
            print()
            
                # send data to  save function and store it 
            self.saves('class11th.csv', self.class11, self.N11)
            self.saves('courses11th.csv', self.courses11, self.N11)

        elif class_==12:
            self.courses12[self.N12][0]=str(self.N12+1)
            no_of_courses_enrolled = 1

            while no_of_courses_enrolled <= 7:
                print()
                print('Select  your courses')
                print(' press \n 1 for Biology \n 2 for Math \n 3 for English \n 4 for CHemistry \n 5 for Sindhi \n 6 for Physics \n7 for Conmputer \n 8 to go Back')
                no=int(input('Enter : '))
                
                if no ==1:
                    if 'Biology' not in self.courses12[self.N12] and 'Computer' not in self.courses12[self.N12]:
                        self.courses12[self.N12][no_of_courses_enrolled]='Biology'
                        fees12+=2000
                        print('Added Successfully')
                        no_of_courses_enrolled+=1
                    else :
                        print('ALready added')
                elif no==2:
                    if 'Math' not in self.courses12[self.N12]:
                        self.courses12[self.N12][no_of_courses_enrolled]='Math'
                        fees12+=2000
                        no_of_courses_enrolled+=1
                        print('Added Successfully')
                    else :
                        print('ALready added')
                elif no==3:
                    if 'English' not in self.courses12[self.N12]: 
                        self.courses12[self.N12][no_of_courses_enrolled]='English'
                        fees12+=2000
                        no_of_courses_enrolled+=1
                        print('Added Successfully')
                    else :
                        print('ALready added')
                elif no==4:
                    if 'Chemistry' not in self.courses12[self.N12]: 
                        self.courses12[self.N12][no_of_courses_enrolled]='Chemistry'
                        fees12+=2000
                        no_of_courses_enrolled+=1
                        print('Added Successfully')
                    else :
                        print('ALready added')
                elif no==5:
                    if 'Sindhi' not in self.courses12[self.N12]: 
                        self.courses12[self.N12][no_of_courses_enrolled]='Sindhi'
                        fees12+=2000
                        no_of_courses_enrolled+=1
                        print('Added Successfully')
                    else :
                        print('ALready added')
                elif no==6:
                    if 'Physiics' not in self.courses12[self.N12]: 
                        self.courses12[self.N12][no_of_courses_enrolled]='Physiics'
                        fees12+=2000
                        no_of_courses_enrolled+=1
                        print('Added Successfully')
                    else :
                        print('ALready added')
                elif no==7:
                    if 'Computer' not in self.courses12[self.N12] and 'Biology' not in self.courses12[self.N12]: 
                        self.courses12[self.N12][no_of_courses_enrolled]='Computer'
                        fees12+=2000
                        no_of_courses_enrolled+=1
                        print('Added Successfully')
                    else :
                        print('ALready added')
                elif no ==8:
                    break
                
                else:
                    print('Invlaid  option')

            
            self.class12[self.N12][0] = str(self.N12+1)
            self.class12[self.N12][1] = name
            self.class12[self.N12][2] = fname
            self.class12[self.N12][3] = age
            self.class12[self.N12][4] = contact
            self.class12[self.N12][5] = Date
            self.class12[self.N12][6] = str(fees12)

            self.N12 += 1
            # To print(student informationt that has been added)
            for i in range(self.N12-1,-1,-1):
                print('Student Data')
                print()
                print('SID     Name    Father   Age    Contact   Date    Fees')

                for j in range(len(self.class12[i])):
                    print(self.class12[i][j], end='\t')
                print()
                print('Courses')
                for j in range(len(self.courses12[i])):
                    print(self.courses12[i][j], end=' ')
                break
            print()
            
                # send data to  save function and store it 
            self.saves('class12th.csv', self.class12, self.N12)
            self.saves('courses12th.csv', self.courses12, self.N12)
        
        elif class_==1:
            self.Cit[self.C][0] = str(self.C+1)
            self.Cit[self.C][1] = name
            self.Cit[self.C][2] = fname
            self.Cit[self.C][3] = age
            self.Cit[self.C][4] = contact
            self.Cit[self.C][5] = Date
            self.Cit[self.C][6] = input('Enter fees')
            self.Cit[self.C][5] = 'CIT'

            self.C += 1
            for i in range(self.C-1,-1,-1):
                print('Student Data')
                print()
                print('SID     Name    Father   Age    Contact   Date    Fees')
                for j in range(len(self.Cit[i])):
                    print(self.Cit[i][j], end='\t')
                print()
                break
            print()
            
            self.saves('Cit.csv', self.Cit, self.C)

    def saves(self, filename, data, n):
        if  os.path.exists(filename):
            os.remove(filename)
        with open(filename, 'w',newline='') as file:
            writer = csv.writer(file)
            for i in range(n):
                writer.writerow(data[i])

    def load_file_s_info(self, filename):
        N = 0
        data = np.array([['' for i in range(15)]for j in range(100)],dtype=object)
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    for i in range(len(row)):
                        data[N][i] = row[i]
                    N += 1
        else:
            print(f'{filename} file not found')
        return data, N
                
    def load(self, class_number):
        if class_number == 9:
            filename = 'class9th.csv'
            coursename='courses9th.csv'
            Marks='Marks9.csv'
            self.class9, self.N9 = self.load_file_s_info(filename)
            self.courses9,self.N9=self.load_file_s_info(coursename)
            self.Marks9,self.M9=self.load_file_s_info(Marks)
        elif class_number == 10:
            filename = 'class10th.csv'
            coursename='courses10th.csv'
            Marks='Marks10.csv'
            self.class10, self.N10 = self.load_file_s_info(filename)
            self.courses10, self.N10 = self.load_file_s_info(coursename)
            self.Marks10,self.M10=self.load_file_s_info(Marks)

        elif class_number == 11:
            filename = 'class11th.csv'
            coursename='courses11th.csv'
            Marks='Marks11.csv'
            self.class11, self.N11 = self.load_file_s_info(filename)
            self.courses11, self.N11 = self.load_file_s_info(coursename)
            self.Marks11,self.M11=self.load_file_s_info(Marks)

        elif class_number == 12:
            filename = 'class12th.csv'
            coursename='courses12th.csv'
            Marks='Marks12.csv'
            self.class12, self.N12 = self.load_file_s_info(filename)
            self.courses12, self.N12 = self.load_file_s_info(coursename)  
            self.Marks12,self.M12=self.load_file_s_info(Marks)
        elif class_number == 1:
            filename = 'Cit.csv'
            self.Cit, self.C = self.load_file_s_info(filename)

        else:
            print('Invalid Number')
    
    def selectprintclass(self,class_,op):
        if class_==9:
            ninelength=self.N9
            self.showStudentsdata_(self.class9,self.courses9,ninelength,op)
        elif class_==10:
            ninelength=self.N10
            self.showStudentsdata_(self.class10,self.courses10,ninelength,op)
        elif class_==11:
            ninelength=self.N11
            self.showStudentsdata_(self.class11,self.courses11,ninelength,op)
        elif class_==12:
            ninelength=self.N12
            self.showStudentsdata_(self.class12,self.courses12,ninelength,op)
        elif class_==1:
            ninelength=self.C
            course='CIT'
            self.showStudentsdata_(self.Cit,course,ninelength,op)

    def showStudentsdata_(self,classno,courses,lengthclass,op):
            low=0
            high=lengthclass
            index=-1
            mid=int((low+high)/2)
            
            if op==1:
                sid=input('Enter Student Id : ')
                print()
                while (high>=low):
                    mid=int((low+high)/2)
                    if classno[mid][0]==sid:
                        index=mid
                        break
                    elif (sid > classno[mid][0]):
                        low = mid+1
                    elif (sid < classno[mid][0]):
                        high = mid-1
                if index >=0:
                    print('SID     Name   Father  Age   Contact   Date    Fees')
                    for j in range(len(classno[index])):
                        print(classno[index][j],end='\t')
                    print()
                    
                    for j in range(1,len(self.courses9[0])):
                        if courses[index][j]!='':
                            print(f'Course{j}',courses[index][j],end='\n')
                        print()
                else:
                    print('No student found')

            elif op==2:
                
                print('SID     Name   Father  Age   Contact   Date    Fees')
                count=0
                for i in range(lengthclass):
                    for j in range(len(classno[0])):
                        print(classno[i][j], end='\t')
                    print()
                    for j in range(1,len(courses[i])):
                        if courses[i][j]=='':
                            continue
                        else:
                            print(f'Course{j}',courses[i][j],end='\n')

            elif op ==3:
                sid=input('Enter Student Id : ')
                print()
                while (high>=low):
                    mid=int((low+high)/2)
                    if classno[mid][0]==sid:
                        index=mid
                        break
                    elif (sid > classno[mid][0]):
                        low = mid+1
                    elif (sid < classno[mid][0]):
                        high = mid-1
                if index >=0:
                    print('SID     Name   Father  Age   Contact   Date    Fees')
                    for j in range(len(classno[index])):
                        print(classno[index][j],end='\t')
                    print()
                else:
                    print('No student found')

    def update_class(self,class_,sid,op):
        if class_==9:
            
            classlength=self.N9
            self.updatedata('class9th.csv','courses9th.csv',sid,self.class9,classlength,op,self.courses9)
            
            print()
        elif class_==10:
          
            classlength=self.N10
            self.updatedata('class10th.csv','courses10th.csv',sid,self.class10,classlength,op,self.courses10)
            
            print()
        elif class_==11:
           
            classlength=self.N11
            self.updatedata('class11th.csv','courses11th.csv',sid,self.class11,classlength,op,self.courses11)
            
            print()
        elif class_==12:
           
            classlength=self.N12
            self.updatedata('class11th.csv','courses11th.csv',sid,self.class12,classlength,op,self.courses12)
            
            
            print()
        else:
            print('Invald Option')

    def updatedata(self,stu_file,cou_file,sid,classno,classlength,no,course):
        
            # Applying Binary Search To find sid and update info

        low=0
        high=classlength
        index=-1
        mid=int((low+high)/2)
        while (high>=low):
            mid=int((low+high)/2)
            if classno[mid][0]==sid:
                index=mid
                break
            elif (sid > classno[mid][0]):
                low = mid+1
            elif (sid < classno[mid][0]):
                high = mid-1

            # UPDATE PERSONAL INFO 
        
        if no==1:
            print('Enter 1 to update Name')
            print('Enter 2 to update Fater Name')
            print('Enter 3 to update Age')
            print('Enter 4 to update Contact Information')
            op=int(input('Enter : '))
            print(index)
            if index >= 0:
                if op==1:
                    classno[index][1]=input('Enter Updated Name')
                    print('Updated Successfully')

                elif op==2:
                    classno[index][2]=input('Enter Updated Father Name')
                    print('Updated Successfully')
                elif op==3:
                    classno[index][3]=input('Enter Updated Age')
                    print('Updated Successfully')
                elif op==4:
                    classno[index][4]=input('Enter Updated Contact')
                    print('Updated Successfully')
            else:
                print('Out of  bounds')
            self.saves(stu_file,classno,classlength)

            # DELETE COURSES AND REDUCE FEES FROM DATA
            
        elif no==2:
            no=int(input('Enter 1 to drop course or 2 to add course'))
            if no==1:
                
                sub=input('Enter Which course you want to delete : ')
                for i in range(classlength):
                    for j in range(len(course[0])):
                        if course[index][j]==sub:
                                course[index][j]=course[i][j+1]
                                course[index][j+1]=''
                    break
                fess=int(classno[index][6])
                fess-=2000
                classno[index][6]=str(fess)
                self.saves(stu_file,classno,classlength)
                self.saves(cou_file,course,classlength)

            elif no==2:
               
                sub=input('Enter which Suject you want to add')
                count=0
                for j in range(len(course[0])):
                        if course[index][j]==sub:
                            print('Already Addes')
                            break
                        elif course[index][j]=='':
                                course[index][j]=sub
                                fess=int(classno[index][6])
                                fess+=2000
                                classno[index][6]=str(fess)
                                break
                        else:
                            count+=1
                if count==len(course[0]):
                    print('Course Full')
                self.saves(cou_file,course,classlength)
                self.saves(stu_file,classno,classlength)
                
    def payselect(self,class_,sid):
        pay=int(input('Enter fees you want to pay'))
        if class_==9:
            self.pay_fees(sid,self.class9,self.N9,pay,'class9th.csv')
        elif class_==10:
            self.pay_fees(sid,self.class10,self.N10,pay,'class10th.csv')
        elif class_==11:
            self.pay_fees(sid,self.class11,self.N11,pay,'class11th.csv')
        elif class_==10:
            self.pay_fees(sid,self.class12,self.N12,pay,'class12th.csv')

    def pay_fees(self,sid,classno,classlength,pay,filename):
        low=0
        high=classlength
        index=-1
        mid=int((low+high)/2)
        while (high>=low):
            mid=int((low+high)/2)
            if classno[mid][0]==sid:
                index=mid
                break
            elif (sid > classno[mid][0]):
                low = mid+1
            elif (sid < classno[mid][0]):
                high = mid-1
            else:
                print('Not Found')

        if index>=0:
            money=int(classno[index][6])
            classno[index][6]=str(money-pay)
            print('Successfully Payed')
            print('Remaining Amount is ' ,classno[index][6])
        
        self.saves(filename,classno,classlength)

    def upload_marks(self,op):
       
        if op==9:
            ss=input('ENter 1 to enter a new student marks and 2 to enter in previous student ')
            sid =input('Enrer Sid')
            self.Marks9[self.M9][0]=sid
            if ss=='1':
                no=0
                print('Math English Chemistry Physics Sindhi Biology Computer')

                n=input('Enter Subject Name : ')
                mark=input('Enter Marks')
                self.Marks9[self.M9][1]=n
                self.Marks9[self.M9][2]=mark 

                self.M9+=1
                self.saves('Marks9.csv',self.Marks9,self.M9)
                print('Uploaded Successfully')
        


            elif ss=="2":
                index=0
                for i in range(self.M9):
                    for j in range(len(self.Marks9[0])):
                        if self.Marks9[j][i]==sid:
                            index=i
                            break
                n=input('Enter Subject Name : ')
                mark=input('Enter Marks')
                if n=='Math':
                    self.Marks9[index][1]=n
                    self.Marks9[index][2]=mark  
                    # no+=1 
                elif n=='Chemistry':
                    self.Marks9[index][3]=n
                    self.Marks9[index][4]=mark
                    # no+=1 

                elif n=='English':
                    self.Marks9[index][5]=n
                    self.Marks9[index][6]=mark  
                    # no+=1 

                elif n=='Physics':
                    self.Marks9[index][7]=n
                    self.Marks9[index][8]=mark 
                    # no+=1 

                elif n=='Sindhi':
                    self.Marks9[index][9]=n
                    self.Marks9[index][10]=mark   
                    # no+=1 

                elif n=='Biology':
                    self.Marks9[index][11]=n
                    self.Marks9[index][12]=mark   
                    # no+=1 

                elif n=='Computer':
                    self.Marks9[index][13]=n
                    self.Marks9[index][14]=mark  
                    # no+=1 
                else :
                    print('Invalid Subject')

                self.saves('Marks9.csv',self.Marks9,self.M9)
                
             
        elif op==10:
            # print(' Islamiat  Math  English  CHemistry  Physics  Urdu  Sindhi ')

            ss=input('ENter 1 to enter a new student marks and 2 to enter in previous student ')
            sid =input('Enrer Sid')
            self.Marks10[self.M10][0]=sid
            if ss=='1':
                no=0
                print('Math English Chemistry Physics Sindhi Biology Computer')

                n=input('Enter Subject Name : ')
                mark=input('Enter Marks')
                self.Marks10[self.M10][1]=n
                self.Marks10[self.M10][2]=mark 

                self.M10+=1
                self.saves('Marks10.csv',self.Marks10,self.M10)
                print('Uploaded Successfully')
        
            elif ss=="2":
                index=0
                for i in range(self.M10):
                    for j in range(len(self.Marks10[0])):
                        if self.Marks10[j][i]==sid:
                            index=i
                            break
                n=input('Enter Subject Name : ')
                mark=input('Enter Marks')
                if n=='Math':
                    self.Marks10[index][1]=n
                    self.Marks10[index][2]=mark  
                    # no+=1 
                elif n=='Chemistry':
                    self.Marks10[index][3]=n
                    self.Marks10[index][4]=mark
                    # no+=1 

                elif n=='English':
                    self.Marks10[index][5]=n
                    self.Marks10[index][6]=mark  
                    # no+=1 

                elif n=='Physics':
                    self.Marks10[index][7]=n
                    self.Marks10[index][8]=mark 
                    # no+=1 

                elif n=='Sindhi':
                    self.Marks10[index][9]=n
                    self.Marks10[index][10]=mark   
                    # no+=1 

                elif n=='Biology':
                    self.Marks10[index][11]=n
                    self.Marks10[index][12]=mark   
                    # no+=1 

                elif n=='Computer':
                    self.Marks10[index][13]=n
                    self.Marks10[index][14]=mark  
                    # no+=1 
                else :
                    print('Invalid Subject')

                self.saves('Marks10.csv',self.Marks10,self.M10)
                
             
        elif op==11:
            # print(' Math English Chemistry Physics Sindhi Biology Computer')
            ss=input('ENter 1 to enter a new student marks and 2 to enter in previous student ')
            sid =input('Enrer Sid')
            self.Marks11[self.M11][0]=sid
            if ss=='1':
                no=0
                print('Math English Chemistry Physics Sindhi Biology Computer')

                n=input('Enter Subject Name : ')
                mark=input('Enter Marks')
                self.Marks11[self.M11][1]=n
                self.Marks11[self.M11][2]=mark 

                self.M11+=1
                self.saves('Marks11.csv',self.Marks11,self.M11)
                print('Uploaded Successfully')
        
            elif ss=="2":
                index=0
                for i in range(self.M11):
                    for j in range(len(self.Marks11[0])):
                        if self.Marks11[j][i]==sid:
                            index=i
                            break
                n=input('Enter Subject Name : ')
                mark=input('Enter Marks')
                if n=='Math':
                    self.Marks11[index][1]=n
                    self.Marks11[index][2]=mark  
                    # no+=1 
                elif n=='Chemistry':
                    self.Marks11[index][3]=n
                    self.Marks11[index][4]=mark
                    # no+=1 

                elif n=='English':
                    self.Marks11[index][5]=n
                    self.Marks11[index][6]=mark  
                    # no+=1 

                elif n=='Physics':
                    self.Marks11[index][7]=n
                    self.Marks11[index][8]=mark 
                    # no+=1 

                elif n=='Sindhi':
                    self.Marks11[index][9]=n
                    self.Marks11[index][10]=mark   
                    # no+=1 

                elif n=='Biology':
                    self.Marks11[index][11]=n
                    self.Marks11[index][12]=mark   
                    # no+=1 

                elif n=='Computer':
                    self.Marks11[index][13]=n
                    self.Marks11[index][14]=mark  
                    # no+=1 
                else :
                    print('Invalid Subject')

                self.saves('Marks11.csv',self.Marks11,self.M11)
                
             
        elif op==12:
            print(' Math English Chemistry Physics Sindhi Biology Computer')
            ss=input('ENter 1 to enter a new student marks and 2 to enter in previous student ')
            sid =input('Enrer Sid')
            self.Marks12[self.M12][0]=sid
            if ss=='1':
                no=0
                print('Math English Chemistry Physics Sindhi Biology Computer')

                n=input('Enter Subject Name : ')
                mark=input('Enter Marks')
                self.Marks12[self.M12][1]=n
                self.Marks12[self.M12][2]=mark 

                self.M12+=1
                self.saves('Marks12.csv',self.Marks12,self.M12)
                print('Uploaded Successfully')
        
            elif ss=="2":
                index=0
                for i in range(self.M12):
                    for j in range(len(self.Marks12[0])):
                        if self.Marks12[j][i]==sid:
                            index=i
                            break
                n=input('Enter Subject Name : ')
                mark=input('Enter Marks')
                if n=='Math':
                    self.Marks12[index][1]=n
                    self.Marks12[index][2]=mark  
                    # no+=1 
                elif n=='Chemistry':
                    self.Marks12[index][3]=n
                    self.Marks12[index][4]=mark
                    # no+=1 

                elif n=='English':
                    self.Marks12[index][5]=n
                    self.Marks12[index][6]=mark  
                    # no+=1 

                elif n=='Physics':
                    self.Marks12[index][7]=n
                    self.Marks12[index][8]=mark 
                    # no+=1 

                elif n=='Sindhi':
                    self.Marks12[index][9]=n
                    self.Marks12[index][10]=mark   
                    # no+=1 

                elif n=='Biology':
                    self.Marks12[index][11]=n
                    self.Marks12[index][12]=mark   
                    # no+=1 

                elif n=='Computer':
                    self.Marks12[index][13]=n
                    self.Marks12[index][14]=mark  
                    # no+=1 
                else :
                    print('Invalid Subject')

                self.saves('Marks12.csv',self.Marks12,self.M12)
                
             
        else:
            print('Inavalid Option')
        
    def showmarks(self,classno,length,op):
        index=0
        if op==1:
            sid = input('Enter sid')
            for i in range(length):
                if classno[i][0]==sid:
                    index=i
            if index >=0:
                    for j in range(len(classno[index])):
                        if classno[index][j]=='':
                            continue
                        else:
                            print(classno[index][j],end='\t')
                    print()
        elif op ==2:
                for i in range(length):
                    for j in range(len(classno[i])):
                        print(classno[i][j], end='\t')
                    print()

    def marks_select(self,class_,op):
        if class_==9:
            ninelength=self.M9
            self.showmarks(self.Marks9,ninelength,op)
        elif class_==10:
            ninelength=self.M10
            self.showmarks(self.Marks10,ninelength,op)
        elif class_==11:
            ninelength=self.M11
            self.showmarks(self.Marks11,ninelength,op)
        elif class_==12:
            ninelength=self.M12
            self.showmarks(self.Marks12,ninelength,op)

    def deleted_select(self,class_):
        if class_==9:
            self.deleted('class9th.csv','courses9th.csv','Marks9.csv',self.class9,self.courses9,self.Marks9,self.N9,self.M9,class_)
        elif class_==10:
            self.deleted('class9th.csv','courses9th.csv','Marks9.csv',self.class10,self.courses10,self.Marks10,self.N10,self.M10,class_)
        elif class_==11:
            self.deleted('class9th.csv','courses9th.csv','Marks9.csv',self.class11,self.courses11,self.Marks11,self.N11,self.M11,class_)
        elif class_==12:
            self.deleted('class9th.csv','courses9th.csv','Marks9.csv',self.class12,self.courses12,self.Marks12,self.N12,self.M12,class_)
        elif class_==1:
            self.deleted('class9th.csv','courses9th.csv','Marks9.csv',self.Cit,self.courses12,self.Marks12,self.C,self.M12,class_)

    def deleted(self,file1,file2,file3,classno,course,mark,lenthclass,lengthmark,op):
        sid = input('ENter sid : ')
        #  findig in class and courses to delete
        low=0
        high=lenthclass
        index=-1
        mid=int((low+high)/2)
        index1=0
        if op==1:
            while (high>=low):
                mid=int((low+high)/2)
                if classno[mid][0]==sid:
                    index=mid
                    break
                elif (sid > classno[mid][0]):
                    low = mid+1
                elif (sid < classno[mid][0]):
                    high = mid-1
            if index >=0: 
                classno[index]=''

        else:
            # ====================Binary Search========================
            while (high>=low):
                mid=int((low+high)/2)
                if classno[mid][0]==sid:
                    index=mid
                    break
                elif (sid > classno[mid][0]):
                    low = mid+1
                elif (sid < classno[mid][0]):
                    high = mid-1
            if index >=0: 
                classno[index]=''


            # =======================Searching=======================

            for i in range(lengthmark):
                for  j in range(len(mark[0])):
                    if mark[i][j]==sid:
                        index1=i
            if index1 >=0: 
                j=index1+1
                while mark[j][0]!='':
                    mark[j-1]=mark[j]
                    j+=1
                lengthmark-=1

            print('Deleted Successfully')

            self.saves(file1,classno,lenthclass)
            self.saves(file2,course,lenthclass)
            self.saves(file3,mark,lengthmark)



class Teacher:
    def __init__(self):
        self.Nt=0
        self.teacher=np.array([['' for i in range(8)] for j in range(20)],dtype=object)  
       
        self.load(1)

    def saves(self, filename, data, n):
        if  os.path.exists(filename):
            os.remove(filename)
        with open(filename, 'w',newline='') as file:
            writer = csv.writer(file)
            for i in range(n):
                writer.writerow(data[i])
   
    def load_file_s_info(self, filename):
        N = 0
        data = np.array([['' for i in range(8)]for j in range(100)],dtype=object)
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    for i in range(len(row)):
                        data[N][i] = row[i]
                    N += 1
        else:
            print(f'{filename} file not found')
        return data, N
                
    def load(self, class_number):
        if class_number == 1:
            filename = 'Teacherinfo.csv'
            self.teacher, self.Nt = self.load_file_s_info(filename)
        
        else:
            print('Invalid Input')

    def registerteacher(self):
        name = input('Enter name ')
        fname = input('Enter father name ')
        age=input('Enetr age of Teacher  : ')
        contact=input('Enter Contact number  : ')
        Date=input('Enter Date Of joining : ')
        subject=input('Enter Subject name')
        salary=input('Enter Salary')       

        self.teacher[self.Nt][0] = str(self.Nt+1)
        self.teacher[self.Nt][1] = name
        self.teacher[self.Nt][2] = fname
        self.teacher[self.Nt][3] = age
        self.teacher[self.Nt][4] = contact
        self.teacher[self.Nt][5] = Date
        self.teacher[self.Nt][6] = subject
        self.teacher[self.Nt][7] = str(salary)
        self.Nt += 1
        self.saves('Teacherinfo.csv',self.teacher,self.Nt)
        # To print(student informationt that has been added)
        for i in range(self.Nt-1,-1,-1):
            for j in range(len(self.teacher[i])):
                print(self.teacher[i][j], end='\t')
            print()
            break
        print()
    
    def showteacherdata_(self):
            print('press 1 to Search Any Teacher Information')
            print('press 2 to show All student Data')
            op=int(input('Enter : '))
            
            low=0
            high=self.Nt
            index=-1
            mid=int((low+high)/2)

            if op==1:
                sid=input('Enter  Id : ')
                print()
                while (high>=low):
                    mid=int((low+high)/2)
                    if self.teacher[mid][0]==sid:
                        index=mid
                        break
                    elif (sid > self.teacher[mid][0]):
                        low = mid+1
                    elif (sid < self.teacher[mid][0]):
                        high = mid-1
                
                if index >=0:
                    for j in range(len(self.teacher[index])):
                        print(self.teacher[index][j],end='\t')
                    print()
                    
                else:
                    print('Not found')

            elif op==2:
                for i in range(self.Nt):
                    for j in range(len(self.teacher[i])):
                        print(self.teacher[i][j], end='\t')
                    print()

    def updateteacherdata(self):
            # Applying Binary Search To find sid and update info
        low=0
        high=self.Nt
        index=-1
        mid=int((low+high)/2)
        sid=input('Enter  Id : ')
        while (high>=low):
            mid=int((low+high)/2)
            if self.teacher[mid][0]==sid:
                index=mid
                break
            elif (sid > self.teacher[mid][0]):
                low = mid+1
            elif (sid < self.teacher[mid][0]):
                high = mid-1

            # UPDATE PERSONAL INFO 
    
        print('Enter 1 to update Name')
        print('Enter 2 to update Fater Name')
        print('Enter 3 to update Age')
        print('Enter 4 to update Contact Information')
        op=int(input('Enter : '))
        if index >= 0:
            if op==1:
                self.teacher[index][1]=input('Enter Updated Name')
                print('Updated Successfully')
            elif op==2:
                self.teacher[index][2]=input('Enter Updated Father Name')
                print('Updated Successfully')
            elif op==3:
                self.teacher[index][3]=input('Enter Updated Age')
                print('Updated Successfully')
            elif op==4:
                self.teacher[index][4]=input('Enter Updated Contact')
                print('Updated Successfully')
        else:
            print('Out of  bounds')
        self.saves('Teacherinfo.csv',self.teacher,self.Nt)

    def deletedata(self):
        sid = input('ENter sid : ')
        low=0
        high=self.Nt
        index=-1
        mid=int((low+high)/2)
        while (high>=low):
            mid=int((low+high)/2)
            if self.teacher[mid][0]==sid:
                index=mid
                break
            elif (sid > self.teacher[mid][0]):
                low = mid+1
            elif (sid < self.teacher[mid][0]):
                high = mid-1
        if index >=0: 
            self.teacher[index]=''
            print('Deleted Successfuly')
            self.saves('Teacherinfo.csv',self.teacher,self.Nt)

                






        
cc = CoachingCenter()
tt=Teacher()
user=input('Enter Username')
passw=input('Enter Password')
if user=='abc' and passw=='123':

    while True:
        print('Enter 1 to Register Students')
        print('Enter 2 to Search any sutdent information or courses')
        print('Enter 3 to Update any student information')
        print('Enter 4 to Submit fess of student')
        print('Enter 5 to Delete any student information')
        print('Enter 6 to Register as Teacher')
        print('Enter 7 to show Teachers Info')
        print('Enter 8 to Teacher Upload Makrs of students')
        print('Enter 9 to Update Teacher Info')
        print('Enter 10 to DELETE Teacher Info')
        print('Enter 11 to Show Marks')
        print('Enter 12 to  exit')
        classno=int(input('Enter :'))
        print()
        print()

        if classno==1:
            print()
            cc.enroll_students()

        elif classno==2:
            print()
            class_ = int(input('Enter class num to show student (in digit, eg 9,10,11,12) and 1 For CIT'))

            print('Press 1 to Search Any Student Information')
            print('Press 2 to show All student Data')
            print('Press 3 to Search Cit student mark')

            op=int(input('Enter : '))
            cc.selectprintclass(class_,op)
            print()

        elif classno==3 :
            class_ = int(input('Enter class num of student (in digit, eg 9,10,11,12) '))
            print('Enter 1 to update personal Information')
            print('Enter 2 to Drop Or Add Courses')
            no=int(input('Enter'))
            sid=input('Enter Sid ')
            cc.update_class(class_,sid,no)

        elif classno==4:
            class_ = int(input('Enter class num of student (in digit, eg 9,10,11,12) '))
            sid=input('Enter Sid')
            cc.payselect(class_,sid)  

        elif classno==5:
            class_ = int(input('Enter class (in digit, eg 9,10,11,12) '))
            cc.deleted_select(class_)

        elif classno==6:
            tt.registerteacher()

        elif classno==7:
            tt.showteacherdata_()    

        elif classno==8:
            class_ = int(input('Enter class (in digit, eg 9,10,11,12) '))
            cc.upload_marks(class_)

        elif classno==9:
            tt.updateteacherdata()

        elif classno==10:
            print()
            tt.deletedata()

        elif classno==11:
            class_ = int(input('Enter class num to show student (in digit, eg 9,10,11,12)'))

            print('Press 1 to Search Any Student Information')
            print('Press 2 to show All student Data')
            op=int(input('Enter : '))
            cc.marks_select(class_,op)

        elif classno==12:
            print('Good Bye')
            break
        else :
            print('Invalid input')
else:
    print('Invalid Username or Password')
