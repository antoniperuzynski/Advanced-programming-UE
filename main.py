from detector import print_result, detectpeople
import glob

for path in glob.glob('.\\Images\\*'):
    print(path)
    print_result(detectpeople(path))
