# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.15.0
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# +
# incomplete, lots of redundancy #

def grep(pattern, flags, files):
    returnstr= ""
    returnlst=[]
    
    if len(files) == 1:
        file = files[0]
        filetext = open(file, 'r')

        if '-x' in flags:
            idx = 0
            
            for line in filetext:
                idx += 1
                if '-i' in flags:
                    if pattern.lower() == line.lower():
                        if '-n' in flags:
                            returnstr += f"{idx}:{line}"
                        else:
                            returnstr += line
                elif pattern == line:
                    if '-n' in flags:
                        returnstr += f"{idx}:{line}"
                    returnstr += line
            return returnstr

        if '-l' in flags:
            content = filetext.read()
            if pattern in content:
                returnstr += f"{file}\n"
                return returnstr
            
        idx = 0
        for line in filetext:
            idx += 1
            
            if '-i' in flags:
                if pattern.lower() in line.lower():
                    if '-n' in flags:
                        returnstr += f"{idx}:"
                    returnstr += line
            
            elif pattern in line:
                if '-n' in flags:
                    returnstr += f"{idx}:"
                returnstr += line
        return returnstr
    
    
    else:
        for file in files:
            filetext = open(file, 'r')
            
            if '-l' in flags:
                content = filetext.read()
                if pattern in content:
                    returnstr += f"{file}\n"
            
            else:
                idx = 0
                for line in filetext:
                    idx += 1
    
                    if '-i' in flags:
                        if pattern.lower() in line.lower():
                            if '-n' in flags:
                                returnstr += f"{file}:{idx}:{line}"
                            else:
                                returnstr += f"{file}:{line}"
                    
                    elif pattern in line:
                        if 'n' in flags:
                            returnstr += f"{file}:{idx}:{line}"
                        else:
                            returnstr += f"{file}:{line}"
        return returnstr
# -


