import subprocess, pem

#In this command, we substitute "nj.gov" with the variable corresponding to IP/domain list.
certData = subprocess.check_output(["nmap", "-p", "443", "*****", "--script", "ssl-cert", "-vv"])
print("Command complete!")

#Output from subprocess is stored as Python bytes; need to convert to "standard" format for processing.
certData = certData.decode("utf-8")

print(certData)
#Slice string to remove the PEM certificate.
begin = (certData.find("-----BEGIN CERTIFICATE-----"))
end = (certData.find("-----END CERTIFICATE-----"))
#This line is necessary to include the actual "-----END CERTIFICATE-----" text at the end of slice.
end = end + 25

#Store PEM certificate data.
pemCert = (certData[begin:end])

pemCertClean = ""
#Removes unneccessary lines from the beginning of certificate data, concatenates to new variable.
for line in pemCert.splitlines():
    if ("| " in line) or ("|_" in line):
        pemCertClean+=line[2:]+"\n"
        #print(line[2:])
    else:
        pemCertClean+=line+"\n"
        #print(line)

print(pemCertClean)
