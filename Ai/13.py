print("*"*30)
print("Medical Diagnosis system")
print("*"*30)
print("Answer Only Yes/No")
fever=input("Do uhhh have fever:")
cold=input("Do uhhh have cold:")
sore_th=input("Do uhhh have sore throat:").lower
body_ache=input("Do uhhh have body ache:").lower
rn_nose=input("Do uhhh have Running Nose:").lower
if fever=="yes" and cold=="yes" and sore_th=="yes":
# and body_ache=="no" and rn_nose=="no":
    Diagnosis="viral upper respiratory infection"
elif cold=="yes" and body_ache=="yes"and fever=="no":
    Diagnosis="flu"
elif rn_nose=="yes" and fever=="yes" and cold=="yes":
    Diagnosis="COVID 19"
else:
    Diagnosis="I need a bit more detail. Could you please share your details......"

    print("*"*30)
    print("\t\tResult:")
    print("Dignosis:", Diagnosis)
    print("please Contact Doctor for Betteer Diagnosis")