dict={
    "py":"'python'",
    "java":"'java'",
    "cpp":"'c++'",
    "text":"'txt'",
    "c":"'c'",
}
n= input("Input the Filename:")

f = n.split(".")

a=(dict[f[-1]])
print("The extension of the file is :"+a)
