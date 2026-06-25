import math as m

print("--------WELCOME TO PYCALC STUDIO:V-1.0--------------")
print("--------------CALCULATORS AVAILABLE:----------------- ")
print("1.SCIENTIFIC CALCULATOR")
print("2.GRAPHING CALCULATOR")
print("3.STATISTICAL CALCULATOR")
print("4. PHYSICS CALCULATOR")
print("TYPE'quit' TO QUIT THE PROGRAM")
while True:
    choice=input("Enter your choice (1/2/3/4/quit): ")
    if(choice=='1'):

        print("---------WELCOME TO SCIENTIFIC CALCULATOR---------")
        print("--------------Available functions:---------------")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Square Root")
        print("6. Power")
        print("7.nth root")
        print("8. Logarithm")
        print("9. Trigonometric Functions (sin, cos, tan,cosec,sec,cot)")
        print("10. Factorial")
        print("11.to find value of constants such as pi and e")
        print("MS or MR or MC to use memory functions")
        print("Type 'exit' to quit the calculator")
        memory=0
        while True:
            choice=input("enter your choice:")
            if(choice=="1"):
                a=float(input("enter first number:"))
                b=float(input("enter second number:"))
                sum=a+b
                print("result:",sum)
                memory=sum
            elif(choice=="2"):
                a=float(input("enter first number:"))
                b=float(input("enter second number:"))
                print("result:",a-b)
                memory=a-b
            elif(choice=="3"):
                a=float(input("enter first number:"))
                b=float(input("enter second number:"))
                print("result:",a*b)
                memory=a*b
            elif(choice=="4"):
                a=float(input("enter first number:"))
                b=float(input("enter second number:"))
                if(b==0):
                    print("division by zero is not possible")
                else:
                    print("result:",a/b)
                    memory=a/b
            elif(choice=="5"):
                a=float(input("enter number:"))
                if(a<0):
                    print("square root of negative number is not possible")
                else:
                    print("result:",m.sqrt(a))
                    memory=m.sqrt(a)
            elif(choice=="6"):
                a=float(input("enter base number:"))
                b=float(input("enter power number:"))
                print("result:",m.pow(a,b))
                memory=m.pow(a,b)
            elif(choice=="7"):
                a=float(input("enter number:"))
                b=float(input("enter root number:"))
                if(a<0 and b%2==0):
                    print("even root of negative number is not possible")
                else:
                    print("result:",m.pow(a,1/b))
                    memory=m.pow(a,1/b)
            elif(choice=="8"):
                a=float(input("enter number:"))
                b=float(input("enter base number:"))
                if(a<=0 or b<=0):
                    print("logarithm of non-positive number is not possible")
                else:
                    print("result:",m.log(a,b))
                    memory=m.log(a,b)
            elif(choice=="9"):
                a=float(input("enter angle in degrees:"))
                func=input("enter function name (sin, cos, tan, cosec, sec, cot):")
                rad=m.radians(a)
                if(func=="sin"):
                    print("result:",m.sin(rad))
                    memory=m.sin(rad)
                elif(func=="cos"):
                    print("result:",m.cos(rad))
                    memory=m.cos(rad)
                elif(func=="tan"):
                    print("result:",m.tan(rad))
                    memory=m.tan(rad)
                elif(func=="cosec"):
                    if(m.sin(rad)==0):
                        print("cosec is undefined for this angle")
                    else:
                        print("result:",1/m.sin(rad))
                        memory=1/m.sin(rad)
                elif(func=="sec"):
                    if(m.cos(rad)==0):
                        print("sec is undefined for this angle")
                    else:
                        print("result:",1/m.cos(rad))
                        memory=1/m.cos(rad)
                elif(func=="cot"):
                    if(m.tan(rad)==0):
                        print("cot is undefined for this angle")
                    else:
                        print("result:",1/m.tan(rad))
                        memory=1/m.tan(rad)
                else:
                    print("invalid function name")
            elif(choice=="10"):
                a=int(input("enter number:"))
                if(a<0):
                    print("factorial of negative number is not possible")
                else:
                    print("result:",m.factorial(a))
                    memory=m.factorial(a)
            elif(choice=="11"):
                const=input("enter constant name (pi, e):")
                if(const=="pi"):
                    print("result:",m.pi)
                    memory=m.pi
                elif(const=="e"):
                    print("result:",m.e)
                    memory=m.e
                else:
                    print("invalid constant name")
            elif(choice=="MS"):
                print("Memory stored:",memory)
            elif(choice=="MR"):
                print("Memory recalled:",memory)
            elif(choice=="MC"):
                memory=0
                print("Memory cleared")
            elif(choice=="exit"):
                print("Exiting the calculator. Goodbye!")
                break
            else:
                print("invalid choice")
    if(choice=='2'):
        print("------WELCOME TO GRAPHING CALCULATOR------")
        print("----------FUNCTIONS AVAILABLE:----------")
        print("1. Plotting a function")
        print("type exit to quit the calculator")
        while True:
            choice=input("enter your choice:")
            if(choice=='1'):
                import matplotlib.pyplot as pyp
                function=input("enter the function which you want to plot  in terms of x :")
                a=int(input("enter the starting value of x:"))
                b=int(input("enter the ending value of x:"))
                y=[]
                x_values=[]
                for x in range(a,b+1):
                    x_values.append(x)
                    y.append(eval(function))
                colour=input("enter the colour of the graph:")
                pyp.plot(x_values,y,color=colour)
                pyp.grid()
                pyp.title("Graph of " +function)
                pyp.xlabel("X-axis")
                pyp.ylabel("Y-axis")
                pyp.show()
            elif(choice=='exit'):
                print("Exiting the calculator. Goodbye!")
                break
            else:
                print("invalid choice")
    if(choice=='quit'):
        print("Exiting the program. Goodbye!")
        break
    if(choice=='3'):
        print("------WELCOME TO STATISTICAL CALCULATOR------")
        print("----------FUNCTIONS AVAILABLE:----------")
        print("1. Mean")
        print("2. Median")
        print("3. Mode")
        print("4. Standard Deviation")
        print("5. Variance")
        print("type exit to quit the calculator")
        while True:
            choice=input("enter your choice:")
            if(choice=='1'):
                data=input("enter the data separated by commas:")
                data_list=[float(i) for i in data.split(',')]
                mean=sum(data_list)/len(data_list)
                print("Mean:",mean)
            elif(choice=='2'):
                data=input("enter the data separated by commas:")
                data_list=[float(i) for i in data.split(',')]
                data_list.sort()
                n=len(data_list)
                if n%2==0:
                    median=(data_list[n//2-1]+data_list[n//2])/2
                else:
                    median=data_list[n//2]
                print("Median:",median)
            elif(choice=='3'):
                from collections import Counter
                data=input("enter the data separated by commas:")
                data_list=[float(i) for i in data.split(',')]
                mode_data=Counter(data_list)
                mode=mode_data.most_common(1)[0][0]
                print("Mode:",mode)
            elif(choice=='4'):
                data=input("enter the data separated by commas:")
                data_list=[float(i) for i in data.split(',')]
                mean=sum(data_list)/len(data_list)
                variance=sum((x-mean)**2 for x in data_list)/len(data_list)
                std_dev=m.sqrt(variance)
                print("Standard Deviation:",std_dev)
            elif(choice=='5'):
                data=input("enter the data separated by commas:")
                data_list=[float(i) for i in data.split(',')]
                mean=sum(data_list)/len(data_list)
                variance=sum((x-mean)**2 for x in data_list)/len(data_list)
                print("Variance:",variance)
            elif(choice=='exit'):
                print("Exiting the calculator. Goodbye!")
                break
            else:
                print("invalid choice")
    if(choice=='4'):
        print("------WELCOME TO PHYSICS CALCULATOR------")
        print("----------FUNCTIONS AVAILABLE:----------")
        print("1. Kinematic Equations")
        #print("2. Newton's Laws of Motion")
        print("2. Work, Energy, and Power")
        #print("3. Circular Motion")
        #print("4. Gravitation")
        #print("5. Oscillations and Waves")
        while True:
            choice=input("enter your choice:")
            if(choice=='1'):
                print("Kinematic Equations:")
                print("1. v = u + at")
                print("2. s = ut + 0.5at^2")
                print("3. v^2 = u^2 + 2as")
                print("4. s = (u + v)/2 * t")
                print("5. s = vt - 0.5at^2")
                print('6 for Projectile motion')
                print("type exit to quit the calculator")
                while True:
                    choice=input("enter your choice:")
                    if(choice=='1'):
                        u=float(input("enter initial velocity (u):"))
                        a=float(input("enter acceleration (a):"))
                        t=float(input("enter time (t):"))
                        v=u+a*t
                        print("Final velocity (v):",v)
                    elif(choice=='2'):
                        u=float(input("enter initial velocity (u):"))
                        a=float(input("enter acceleration (a):"))
                        t=float(input("enter time (t):"))
                        s=u*t+0.5*a*t**2
                        print("Displacement (s):",s)
                    elif(choice=='3'):
                        u=float(input("enter initial velocity (u):"))
                        a=float(input("enter acceleration (a):"))
                        s=float(input("enter displacement (s):"))
                        v=m.sqrt(u**2+2*a*s)
                        print("Final velocity (v):",v)
                    elif(choice=='4'):
                        u=float(input("enter initial velocity (u):"))
                        v=float(input("enter final velocity (v):"))
                        t=float(input("enter time (t):"))
                        s=(u+v)/2*t
                        print("Displacement (s):",s)
                    elif(choice=='5'):
                        v=float(input("enter final velocity (v):"))
                        a=float(input("enter acceleration (a):"))
                        t=float(input("enter time (t):"))
                        s=v*t-0.5*a*t**2
                        print("Displacement (s):",s)
                    elif(choice=='6'):
                        print("Projectile Motion:")
                        u=float(input("enter initial velocity (u):"))
                        angle=float(input("enter angle of projection (in degrees):"))
                        g=9.81
                        angle_rad=m.radians(angle)
                        t_flight=(2*u*m.sin(angle_rad))/g
                        max_height=(u**2*m.sin(angle_rad)**2)/(2*g)
                        range_proj=(u**2*m.sin(2*angle_rad))/g
                        print("Time of flight:",t_flight)
                        print("Maximum height:",max_height)
                        print("Range of projectile:",range_proj)
                    elif(choice=='exit'):
                        print("Exiting the calculator. Goodbye!")
                        break
                    else:
                        print("invalid choice")
            if(choice=='2'):
                print("Work, Energy, and Power:")
                print("1. Work done (W = F * d * cosθ)")
                print("2. Kinetic Energy (KE = 0.5 * m * v^2)")
                print("3. Potential Energy (PE = m * g * h)")
                print("4. Power (P = W / t)")
                print("type exit to quit the calculator")
                while True:
                    choice=input("enter your choice:")
                    if(choice=='1'):
                        F=float(input("enter force (F):"))
                        d=float(input("enter displacement (d):"))
                        theta=float(input("enter angle between force and displacement (in degrees):"))
                        theta_rad=m.radians(theta)
                        W=F*d*m.cos(theta_rad)
                        print("Work done (W):",W)
                    elif(choice=='2'):
                        m=float(input("enter mass (m):"))
                        v=float(input("enter velocity (v):"))
                        KE=0.5*m*v**2
                        print("Kinetic Energy (KE):",KE)
                    elif(choice=='3'):
                        m=float(input("enter mass (m):"))
                        g=9.81
                        h=float(input("enter height (h):"))
                        PE=m*g*h
                        print("Potential Energy (PE):",PE)
                    elif(choice=='4'):
                        W=float(input("enter work done (W):"))
                        t=float(input("enter time taken (t):"))
                        P=W/t
                        print("Power (P):",P)
                    elif(choice=='exit'):
                        print("Exiting the calculator. Goodbye!")
                        break
                    else:
                        print("invalid choice")
            elif(choice=='exit'):
                print("Exiting the calculator. Goodbye!")
                break
            else:
                print("invalid choice")