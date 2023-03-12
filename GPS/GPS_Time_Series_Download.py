import requests

#Add site name
f = open(r"../GPS/site456.txt", "r")
line = f.readline()
i = 1

while line:
    url = "http://geodesy.unr.edu/gps_timeseries/tenv3/IGS14/"
    local = "../GPS/"
    url = url+ line.strip().upper()+'.tenv3'
  
    #  open url data
    r = requests.get(url)
    
    #Write local path，SITENAME.txt
    output = local + line.strip().upper() +'.txt'
    f1 = open(output, 'w')
    f1.write(r.text)
 
    line = f.readline()
    print(f"No.{i} is complete!")
    # print("\n")
    i = i+1
#Close file.
f.close()