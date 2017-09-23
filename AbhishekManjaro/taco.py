import re

txt='<span id="ind_chg">-447.60 (-1.38%)</span>'

re1='.*?'	# Non-greedy match on filler
re2='[+-]?\\d*\\.\\d+(?![-+0-9\\.])'	# Uninteresting: float
re3='.*?'	# Non-greedy match on filler
re4='([+-]?\\d*\\.\\d+)(?![-+0-9\\.])'	# Float 1

rg = re.compile(re1+re2+re3+re4,re.IGNORECASE|re.DOTALL)
m = rg.search(txt)
if m:
    float1=m.group(1)
    print "("+float1+")"+"\n"