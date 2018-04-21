

def medical_issues(body_part1,body_part2):
    print ("\n\nHello, Welcome to WebMD -- a Medical Tool used to help diagnose patients\n\n")
    print ("To help you get started -- May I ask which body part of your hurts or feels unwell")
    body_part1="1. Head"
    body_part2="2. Spine"
    print (body_part1)
    print (body_part2)
    print ("Choose either 1 or 2")


def head_parts(head1, head2):
    head1="1. Skull"
    head2="2. Brain"
    print (head1)
    print (head2)
    print ("Choose either 1 or 2\n\n")
    ask_head=input("> ")

    if ask_head=="1": #skull
        print ("Yikes..let's examine this further\n\n")
        print ("What symptoms are you suffering from?")
        skull_symptoms=["1. Headache", "2. Nausea", "3. Vomitting", "4. Blurry Vision"]
        for skull in skull_symptoms:
            print (skull)
        print ("Choose any combination of symptoms [1-4] \n\n")
        x=input(">")
        y=int(x)
        if (y<3):
            print ("\n\n\tYou are Sleep Deprived......\n")
            print ("Treatment: Take an advil and go to sleep.")
        else:
            print ("\n\n\tYou have a Concussion...\n\n")
            print ("WebMD recommends you see a Doctor ASAP..in the meantime take an Advil\n\n")


    if ask_head=="2": #brain
        print ("Yikes...let's examine this further \n\n")
        print ("What Symptoms are you suffering from?\n\nChoose any combination of symtptoms [1-7]\n")
        brain_symptoms={"BrainCancer": ['1. Loss of Vision','2. Loss of sensation', '3. Headache'], 'Parkinson':["4. Tremor,", "5. Loss of muscle movment"], 'Epilepsy': ['6. Random Sensations', '7. Muscle Jerks']}
        print (brain_symptoms['BrainCancer'] + brain_symptoms['Parkinson'] + brain_symptoms['Epilepsy'])
        x=input(">")
        x=int(x)
        if (x==1) or (x==2) or (x==12) or (x==123) or (x==3) or (x==23) or (x==13):
            print ("\n\n\tYou have Brain Cancer...\n\n")
            print ("Treatment: WebMD recommends Surgery and Chemotherapy")
        elif (x==4) or (x==5) or (x==45):
            print ("\n\n\tYou have Parkinson's disease...\n\n")
            print ("Treatment: WebMD recommends L-Dopa and/or Deep Brain Stimulation")
        elif (x==6) or (x==7) or (x==67):
            print ("\n\n\tYou have Epilepsy...\n\n")
            print ("Treatment: WebMD recommends taking AE Medication")
        else:
            print ("You are having a Stroke")
            print ("\n\nTreatment: Head to a specialist ASAP ")


def spine(upper,lower):
    upper="1. Upper Spine"
    lower="2. Lower Spine"
    print (upper)
    print (lower)
    print ("Choose either 1 or 2\n\n")
    ask_spine_location=input("> ")
    x=int(ask_spine_location)
    stenosis_symptoms=["1. Muscle Spasms", "2. Overall Weakness", "3. Numbness in"
    "\tLower Extremities", "4. Pain"]

    if x==1: #upperspine
        print ("What are your symptoms?\nChoose any combination of symptoms[1-4]\n\n")
        for stenosis in stenosis_symptoms:
            print (stenosis)
        user_spine_input=input(">")
        x=int(user_spine_input)
        if x>0:
            print ("\n\n\tYou have Thoracic Stenosis")

    if x==2: #lowerspine
        print ("What are your symptoms?\nChoose any combination of symptoms [1-4]\n")
        for stenosis in stenosis_symptoms:
            print (stenosis)
        user_spine_input=input(">")
        x=int(user_spine_input)
        if x>0:
            print ("\nYou have Lumbar Stenosis\n\n")



def start_my_program():
    medical_issues(1,2)
    user_input_body=input("> ")
    if user_input_body=="1": #head
        print ("Sorry to hear that....\n\n")
        print ("Which part of your head hurts?\n")
        head_parts(1,2)

    if user_input_body=="2": #spine
        print ("Sorry to hear that....\n\n")
        print ("Which part of your spine hurts?\n")
        spine(1,2)

    print ("Thanks for using WebMD")



if __name__=="__main__":

    start_my_program()
