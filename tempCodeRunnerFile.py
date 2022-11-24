irectory,reg):
    result = []
    for root,dirs,files in os.walk(directory):
        for f in files:
            file_name = os.path.join(root,f)
            r = re.search(reg,f)
            if r:
                result += [f]
            try:
                with open(file_name, "r") as f_d:
                        string = f_d.read()
                        if (re.search(reg, string)):
                            if r:
                                result[-1] = "<<" + result[-1]
                            else:
                                result+=[f]
            except:
                pass
    return result
