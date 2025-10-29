import re
import sys
def rep(filename,patstr,repstr,outfile):
    try:
        with open(filename,'r') as f:
            text=f.read()
        mod_str=re.sub(patstr,repstr,text)
        with open(outfile,'w') as out:
            out.write(mod_str)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occured: {e}")
if __name__=="__main__":
    if len(sys.argv)!=4:
        print("Usage: python replace.py <i_f> <pat_str> <rep_str>")
    else:
        i_f=sys.argv[1]
        pat_str=sys.argv[2]
        rep_str=sys.argv[3]
        out_file="modified_"+i_f
        rep(i_f,pat_str,rep_str,out_file)
