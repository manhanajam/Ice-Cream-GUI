# Assignment: Manha_GUI
# Description: Takes Ice cream orders and recieves feedback/how to improve
# Name: Manha Najam
# Date: November 28, 2021
# Course Code: ICS3U1-01

import tkinter 
#from PIL import ImageTk, Image

#Define event handlers
def costumer_name():
   #Use *.get() with Entry fields, like using input() in CLI
    inputName = name.get()
    message = "Order Name:" + name.get()
    msgResult.configure(text = message)        
 
def flavours ():
    group = flavours_selected.get()  #Use *.get() to pull out the variable

    # initial price
    finalPrice = 0

    # Various if statements for the different options and the messgae that will display as well as how much is added to the final price
    if (group == "Cc"):
        flavours_label.configure(text="Cotton Candy - $2")
        finalPrice = finalPrice + 2
        
    elif (group == "P"):
        flavours_label.configure(text="Pineapple - $1.50")
        finalPrice = finalPrice + 1.50
        
    elif (group == "R"):
        flavours_label.configure(text="Raspberry - $1.50")
        finalPrice = finalPrice + 1.50
        
    elif (group == "V"):
        flavours_label.configure(text="Vanilla - $1.50")
        finalPrice = finalPrice + 1.50
        
    # return the total price after user adds their input   
    return finalPrice

def size():
    group = size_selected.get()  #Use *.get() to pull out the variable

    # final price will initally equal to the same price as the function before ended with
    finalPrice = flavours()

    
    # Various if statements for the different options and the messgae that will display as well as how much is added to the final price
    if (group == "S"):
        sizes_label.configure(text="Small - $1")
        finalPrice = finalPrice + 1
    elif (group == "K"):
        sizes_label.configure(text="Kid Size - $0.50")
        finalPrice = finalPrice + 0.50
    elif (group == "M"):
        sizes_label.configure(text="Regular - $1.50")
        finalPrice = finalPrice + 1.50
    elif (group == "L"):
        sizes_label.configure(text="Large - $2")
        finalPrice = finalPrice + 2
        
    # return the total price after user adds their input      
    return finalPrice

def toppings():

    # inital amount of toppings chosen
    topping_counter = 0

    # final price will initally equal to the same price as the function before ended with
    finalPrice = size()

    # Check each option separately, because the user could have selected any 1, any 2, all four or none of the options.
    tapioca_selected = tapioca_checked.get()
    sprinkles_selected = sprinkles_checked.get()
    fruits_selected = fruits_checked.get()
    marshmallow_selected = marshmallow_checked.get()

    # if statements for if the user picks the option and then adds the amount to the toppings price as well as final price
    if (tapioca_selected == 1):
        topping_counter = topping_counter + 0.50
        finalPrice = finalPrice + 0.50
    if (sprinkles_selected == 1):
        topping_counter = topping_counter + 0.50
        finalPrice = finalPrice + 0.50
    if (fruits_selected == 1):
        topping_counter = topping_counter + 0.50
        finalPrice = finalPrice + 0.50
    if (marshmallow_selected == 1):
        topping_counter = topping_counter + 0.50
        finalPrice = finalPrice + 0.50
        
    # variable for the total price for all the toppings together
    priceMsg = str(topping_counter)

    # Displays what the price of all the toppings are
    toppings_label.configure (text="Toppings - $" + priceMsg)

    # return the total price after user adds their input      
    return finalPrice

def  presentation():
    group = presentation_selected.get()  #Use *.get() to pull out the variable

    # final price will initally equal to the same price as the function before ended with
    finalPrice = toppings()

    # Various if statements for the different options and the messgae that will display as well as how much is added to the final price
    if (group == "CU"):
        presentation_label.configure(text="cup - $1")
        finalPrice = finalPrice + 1
    elif (group == "CO"):
        presentation_label.configure(text="cone - $1.50")
        finalPrice = finalPrice + 1.50
    elif (group == "W"):
        presentation_label.configure(text="waffle - $2")
        finalPrice = finalPrice + 2

    # return the total price after user adds their input      
    return finalPrice

def receipt():
    
    # final price will initally equal to the same price as the function before ended with
    finalPrice = presentation()
    group = flavours_selected.get()  #Use *.get() to pull out the variable

    # Various if statements for the different options and the messgae that will display in the receipt
    if (group == "Cc"):
        flavours_label2.configure(text="Cotton Candy - $2")       
    elif (group == "P"):
        flavours_label2.configure(text="Pineapple - $1.50")    
    elif (group == "R"):
        flavours_label2.configure(text="Raspberry - $1.50")   
    elif (group == "V"):
        flavours_label2.configure(text="Vanilla - $1.50")

    group = size_selected.get()  #Use *.get() to pull out the variable

    # Various if statements for the different options and the messgae that will display in the receipt
    if (group == "S"):
        sizes_label2.configure(text="Small - $1")
    elif (group == "K"):
        sizes_label2.configure(text="Kid Size - $0.50")
    elif (group == "M"):
        sizes_label2.configure(text="Regular - $1.50")
    elif (group == "L"):
        sizes_label2.configure(text="Large - $2")

    group = presentation_selected.get()  #Use *.get() to pull out the variable

    # Various if statements for the different options and the messgae that will display in the receipt
    if (group == "CU"):
        presentation_label2.configure(text="cup - $1")
    elif (group == "CO"):
        presentation_label2.configure(text="cone - $1.50")
    elif (group == "W"):
        presentation_label2.configure(text="waffle - $2")

    # inital amount of toppings chosen
    topping_counter = 0

    # Check each option separately, because the user could have selected any 1, any 2, all four or none of the options.
    tapioca_selected = tapioca_checked.get()
    sprinkles_selected = sprinkles_checked.get()
    fruits_selected = fruits_checked.get()
    marshmallow_selected = marshmallow_checked.get()

    # if statements for if the user picks the option and then adds the amount to the toppings price as well as final price
    if (tapioca_selected == 1):
        topping_counter = topping_counter + 0.50
    if (sprinkles_selected == 1):
        topping_counter = topping_counter + 0.50
    if (fruits_selected == 1):
        topping_counter = topping_counter + 0.50
    if (marshmallow_selected == 1):
        topping_counter = topping_counter + 0.50

    # variable for the total price for all the toppings together
    priceMsg = str(topping_counter)

    # Displays what the price of all the toppings are
    toppings_label2.configure(text="Toppings - $" + priceMsg)

    # Multiply the final price by 0.13 to get the tax 
    tax = finalPrice * 0.13
    # Add taxt to the final price and round by two decimal places
    finalPrice = str(round(finalPrice + tax,2))

    # Have a label that outputs the total price
    finalPrice_label.configure(text="Total Price: $" + finalPrice)

def  feedback():
    group = feedback_selected.get()  #Use *.get() to pull out the variable

    # Various if statements for the different options and the messgae that will display depending on which one is picked
    if (group == "B"):
        feedback_label.configure(text="We're Sorry to hear that!")
    elif (group == "Ok"):
        feedback_label.configure(text="We will try better!")
    elif (group == "E"):
        feedback_label.configure(text="Thank you!")

def improvement():

    # Check each option separately, because the user could have selected any or none of the options.
    fast_selected = fastService_checked.get()
    decor_selected = decor_checked.get()
    quailty_selected = quailty_checked.get()
    online_selected = onlineService_checked.get()
    none_selected = none_checked.get()

    # if statements for if the user picks the option and what would be displayed
    if (fast_selected == 1):
        improvement_label.configure(text="We will consider this!")
       
    if (decor_selected == 1):
        improvement_label.configure(text="We will consider this!")

    if (quailty_selected == 1):
        improvement_label.configure(text="We will consider this!")

    if (online_selected == 1):
        improvement_label.configure(text="We will consider this!")

    if (none_selected == 1):
        improvement_label.configure(text="We will consider this!")
           
# main function        
def main():
    
    # global variables for the flavour function
    global flavours_selected
    global flavours_label

    #Define GUI and widgetsr
    main = tkinter.Tk()
    main.title(" Gui Assignment ")
    main.geometry ("600x600")

    # Have a label for the title
    title = tkinter.Label(main, justify="left",
                           text="   Supreme Ice Cream Shop:   ", bg="light blue", width = 20, height = 3)
    title.grid(row=0, column = 3)

    #To code radio buttons as designed, must also use tkinter.StringVar()
    flavours_selected = tkinter.StringVar()

    
   # Add Label that tells the user to put their input for a choice 
    prompt = tkinter.Label(main, justify="left",
                           text="Choose a flavour:", bg= "white")
    prompt.grid(row=2, column = 2)

    # Add details for each option in the radiobutton data type e.g.background colour
    cottonCandy_flavour = tkinter.Radiobutton (main, text="Cotton Candy", relief="raised",
                                         width=17, anchor="w",
                                         variable=flavours_selected, value="Cc",
                                         command=flavours, bg= "light pink")
    cottonCandy_flavour.grid(row=3, column=2)

    pineapple_flavour = tkinter.Radiobutton (main, text="Pineapple", relief="raised",
                                          width=17, anchor="w",
                                          variable=flavours_selected, value="P",
                                          command=flavours, bg = "light pink")
    pineapple_flavour.grid(row=4, column=2)

    raspberry_flavour = tkinter.Radiobutton (main, text="Raspberry", width=17, anchor="w",
                                           variable=flavours_selected, value="R", relief="raised",
                                           command=flavours, bg = "light pink")
    raspberry_flavour.grid(row=5, column=2)

    vanila_flavour = tkinter.Radiobutton (main, text="Vanilla", relief="raised",
                                            width=17, anchor="w",
                                            variable=flavours_selected, value="V",
                                            command=flavours, bg = "light pink")
    vanila_flavour.grid(row=6, column=2)

    # Add an overall label which will show an output depending on the option picked
    flavours_label = tkinter.Label(main, justify="left", bg="light grey", 
                                    width=17, height = 2)
    flavours_label.grid(row=7, column=2)

    #After creating the window, set up the initial state of the window 
    cottonCandy_flavour.invoke()
    
#######################################################Choice 2###############################################################

    #global variables for the size function
    global size_selected
    global sizes_label
    #Define GUI and widgetsr

    #To code radio buttons as designed, must also use tkinter.StringVar()
    size_selected = tkinter.StringVar()

    # Add Label that tells the user to put their input for a choice 
    prompt = tkinter.Label(main, justify="left",
                           text="Choose a size:", bg= "white")
    prompt.grid(row=2, column = 3)

    
    # Add details for each option in the radiobutton data type e.g.background colour
    kid_size = tkinter.Radiobutton (main, text="Kid Size", relief="raised",
                                         width=17, anchor="w",
                                         variable=size_selected, value="K",
                                         command=size, bg="light yellow")
    kid_size.grid(row=3, column=3)

    small_size = tkinter.Radiobutton (main, text="Small Size", relief="raised",
                                          width=17, anchor="w",
                                          variable=size_selected, value="S",
                                          command=size, bg = "light yellow")
    small_size.grid(row=4, column=3)

    medium_size = tkinter.Radiobutton (main, text="Regular", width=17, anchor="w",
                                           variable=size_selected, value="M", relief="raised",
                                           command=size, bg = "light yellow")
    medium_size.grid(row=5, column=3)

    large_size = tkinter.Radiobutton (main, text="Large Size", relief="raised",
                                            width=17, anchor="w",
                                            variable=size_selected, value="L",
                                            command=size, bg = "light yellow")
    large_size.grid(row=6, column=3)

    # Add an overall label which will show an output depending on the option picked
    sizes_label = tkinter.Label(main, justify="left", bg="light grey", text="               ",
                                   width=17, height = 2)
    sizes_label.grid(row=7, column=3)

    #After creating the window, set up the initial state of the window 
    kid_size.invoke()

#######################################################Choice 3###############################################################

    #global varibales for the topppings function
    global tapioca_checked, sprinkles_checked, fruits_checked, marshmallow_checked, toppings_label, topping_counter

    tapioca_checked = tkinter.IntVar()    #IntVar makes the variable a complex data type which
    sprinkles_checked = tkinter.IntVar()   #holds more than just an integer value; use get() on the
    fruits_checked = tkinter.IntVar()      #variable to read the integer value
    marshmallow_checked = tkinter.IntVar()

   # Add Label that tells the user to put their input for a choice 
    prompt = tkinter.Label(main, justify="left",
                           text="Choose Toppings:", bg= "white")
    prompt.grid(row=2, column = 4)

     # Add details for each option in the checkbutton data type e.g.command
    tapioca_selected = tkinter.Checkbutton(main, text = "Mixed tapioca",
                                    variable=tapioca_checked, width=17, anchor="w",relief = "raised",
                                        command = toppings, bg = "orange")
    tapioca_selected.grid(row=3, column = 4)  

    sprinkles_selected = tkinter.Checkbutton(main, text = "Sprinkles",
                                     variable=sprinkles_checked, width=17, anchor="w", 
                                     command = toppings, relief = "raised", bg = "orange")
    sprinkles_selected.grid(row = 4, column = 4)

    fruits_selected = tkinter.Checkbutton(main, text = "Fruits",
                                     variable=fruits_checked, width=17, anchor="w",
                                     command = toppings, relief = "raised", bg = "orange")
    fruits_selected.grid(row = 5, column = 4)
    

    marshmallow_selected = tkinter.Checkbutton(main, text = "Marshmallows",
                                     variable=marshmallow_checked, width=17, anchor="w",
                                     command = toppings, relief = "raised", bg = "orange")
    marshmallow_selected.grid(row = 6, column = 4)

    # Add an overall label which will show an output of the total amount depending on which toppings were chosen
    toppings_label = tkinter.Label(main, text="", bg="light grey", width=17, height = 2, justify="left")
    toppings_label.grid(row=7, column = 4)

#######################################################Choice 4###############################################################

    #global variables for the presentation function
    global presentation_selected
    global presentation_label
    

    #To code radio buttons as designed, must also use tkinter.StringVar()
    presentation_selected = tkinter.StringVar()

    # Add Label that tells the user to put their input for a choice 
    prompt = tkinter.Label(main, justify="left",
                           text="Choose a presentation:", bg = "white")
    prompt.grid(row=2, column = 5)

    # Add details for each option in the radiobutton data type e.g.background colour
    cup = tkinter.Radiobutton (main, text="Cup", relief="raised",
                                         width=17, anchor="w",
                                         variable=presentation_selected, value="CU",
                                    command=presentation, bg = "light green")
    cup.grid(row=3, column=5)

    cone = tkinter.Radiobutton (main, text="Cone", relief="raised",
                                          width=17, anchor="w",
                                          variable=presentation_selected, value="CO",
                                          command=presentation, bg = "light green")
    cone.grid(row=4, column=5)

    waffle = tkinter.Radiobutton (main, text="Waffle", width=17, anchor="w",
                                           variable=presentation_selected, value="W", relief="raised",
                                           command=presentation, bg = "light green")
    waffle.grid(row=6, column=5)

    # Add an overall label which will show an output depending on the option picked
    presentation_label = tkinter.Label(main, justify="left", bg="light grey", text="               ",
                                   width=17, height = 2)
    presentation_label.grid(row=7, column=5)
    
    #After creating the window, set up the initial state of the window 
    cup.invoke()
#######################################################Receipt###############################################################

    #global variables for the receipt function
    global receipt_label
    global flavours_label2
    global sizes_label2
    global toppings_label2
    global presentation_label2
    global finalPrice_label

    # create a button for the user to press after they pick all their options to see their receipt
    receipt_button=tkinter.Button(main, text="Click for Receipt", command=receipt,
                                    width = 17, height = 2, bg="white" )
    receipt_button.grid(row = 2, column = 6)

   # Add details for each label that is for the options e.g. the width
    flavours_label2 = tkinter.Label(main, text="", bg="burlywood", width=17, height = 2, justify="left")
    flavours_label2.grid(row=3, column = 6)

    sizes_label2 = tkinter.Label(main, text="", bg="burlywood", width=17, height = 2, justify="left")
    sizes_label2.grid(row=4, column = 6)

    toppings_label2 = tkinter.Label(main, text="", bg="burlywood", width=17, height = 2, justify="left")
    toppings_label2.grid(row=5, column = 6)

    presentation_label2 = tkinter.Label(main, text="", bg="burlywood", width=17, height = 2, justify="left")
    presentation_label2.grid(row=6, column = 6)

    # Add details to the total price label e.g. the width
    finalPrice_label = tkinter.Label(main, text="", bg="burlywood", width=17, height = 2, justify="left")
    finalPrice_label.grid(row=7, column = 6)


#######################################################Part B###############################################################
    #global variables for the costumer name function
    global name
    global msgResult
    
    # Add Label that tells the user to put their input for a choice 
    prompt = tkinter.Label(main, justify="left",
                           text="Enter Name", bg= "white")
    prompt.grid(row=15, column = 3)

    top_frame = tkinter.Frame(main)
    top_frame.grid(row=18, column=3)#These coordinates refer to the grid associated with main

    # User enters their name
    name = tkinter.Entry(main)
    name.grid(row=16, column=3)

    # Button that says next so the user can see what their order name is after inputting their name
    hello_button = tkinter.Button(main, text="Next", command = costumer_name)
    hello_button.grid(row= 17, column = 3)

    # displays the output message for the order name
    msgResult = tkinter.Label(top_frame, bg="violet")
    msgResult.grid(row= 18, column = 3)


############################################ Feedback ###############################################################
    # Global variables for the feedback function
    global feedback_selected
    global feedback_label


    #To code radio buttons as designed, must also use tkinter.StringVar()
    feedback_selected = tkinter.StringVar()

    # Add Label that tells the user to put their input for a choice 
    prompt = tkinter.Label(main, justify="left",
                           text="Give Us Your Feedback:", bg = "white", width = 17)
    prompt.grid(row=20, column = 2)

    
    # Add details for each option in the radiobutton data type e.g.background colour
    bad = tkinter.Radiobutton (main, text="Bad", relief="raised",
                                         width=17, anchor="w",
                                         variable=feedback_selected, value="B",
                                         command=feedback, bg = "green yellow")
    bad.grid(row=21, column=2)

    okay = tkinter.Radiobutton (main, text="Okay", relief="raised",
                                          width=17, anchor="w",
                                          variable=feedback_selected, value="Ok",
                                          command=feedback, bg = "green yellow")
    okay.grid(row=22, column=2)

    excellent = tkinter.Radiobutton (main, text="Excellent", width=17, anchor="w",
                                           variable=feedback_selected, value="E", relief="raised",
                                           command=feedback, bg = "green yellow")
    excellent.grid(row=23, column=2)

    feedback_frame = tkinter.Frame(main)
    feedback_frame.grid(row=24, column=2)#These coordinates refer to the grid associated with main


    # Add an overall label which will show an output depending on the option picked
    feedback_label = tkinter.Label(feedback_frame, justify="left", bg="light grey", text="               ",
                                   width=17, height = 2)
    feedback_label.grid(row=24, column=2)

   #After creating the window, set up the initial state of the window 
    bad.invoke()

 ############################################# improvement ###########################################################

    #Global variables for the improvement function
    global fastService_checked, decor_checked, quailty_checked, onlineService_checked, none_checked, improvement_label

    fastService_checked = tkinter.IntVar()    #IntVar makes the variable a complex data type which
    decor_checked = tkinter.IntVar()   #holds more than just an integer value; use get() on the
    quailty_checked = tkinter.IntVar()  #variable to read the integer value
    onlineService_checked = tkinter.IntVar()
    none_checked = tkinter.IntVar()
 
   # Add Label that tells the user to put their input for a choice 
    prompt = tkinter.Label(main, justify="left",
                           text="Tell Us How We Can Improve:", bg= "white")
    prompt.grid(row=20, column = 4)

    # Add details for each option in the checkbutton data type e.g.command
    fast_selected = tkinter.Checkbutton(main, text = "Faster Service",
                                    variable=fastService_checked, width=17, anchor="w",relief = "raised",
                                        command = improvement, bg = "green yellow")
    fast_selected.grid(row=21, column = 4)   

    decor_selected = tkinter.Checkbutton(main, text = "Better Decor",
                                     variable=decor_checked, width=17, anchor="w", 
                                     command = improvement, relief = "raised", bg = "green yellow")
    decor_selected.grid(row = 22, column = 4)

    quailty_selected = tkinter.Checkbutton(main, text = "Better Quailty",
                                     variable=quailty_checked, width=17, anchor="w",
                                     command = improvement, relief = "raised", bg = "green yellow")
    quailty_selected.grid(row = 23, column = 4)
    

    online_selected = tkinter.Checkbutton(main, text = "Better Online Service",
                                     variable=onlineService_checked, width=17, anchor="w",
                                     command = improvement, relief = "raised", bg = "green yellow")
    online_selected.grid(row = 24, column = 4)

    none_selected = tkinter.Checkbutton(main, text = "None",
                                     variable=none_checked, width=17, anchor="w",
                                     command = improvement, relief = "raised", bg = "green yellow")
    none_selected.grid(row = 25, column = 4)

    improvement_frame = tkinter.Frame(main)
    improvement_frame.grid(row=26, column=4)#These coordinates refer to the grid associated with main

    # Add a label that will display an output depending on the options picked
    improvement_label = tkinter.Label(improvement_frame, text="", bg="light grey", width=17, height = 2, justify="left")
    improvement_label.grid(row=26, column = 4)

############################################## Images ##################################################################



    #This function puts the GUI into an infinite loop waiting for the user to trigger an event
#main.mainloop()

###########
main()
