import copy
import diff_algo as dmp_module
from rich.text import Text
from rich.style import Style
from rich.console import Console


# bg color in terminal
bg_style = Style(bgcolor="#FF7573")
bg_style2 = Style(bgcolor="#9FF781")

# Text instance
text = Text()
text_c = Text()
console = Console()

dmp = dmp_module.diff_match_patch()

# text1 ="Oftend people become angri when they get frustrates."
# text2 = "Often people become angry when they get frustrated."

text1 = input("")
text2 = input("")

diff = dmp.diff_main(text1,text2)

diff_semantic = dmp.diff_cleanupSemantic(diff)

incorrect_sent = diff.copy()
corrected_sent = diff.copy()


diffy1 = 0
diffy2 = 0


while diffy1 <= len(incorrect_sent)-1:
    if incorrect_sent[diffy1][0] == -1:
        text.append(incorrect_sent[diffy1][1],style=bg_style)
    elif incorrect_sent[diffy1][0] == 1:
        del incorrect_sent[diffy1]
        diffy1 -= 1 

    else:
        text.append(incorrect_sent[diffy1][1])
    diffy1 += 1


console.print(text)    


while diffy2 <= len(corrected_sent)-1:
    if corrected_sent[diffy2][0] == -1:
        del corrected_sent[diffy2]
        diffy2 -= 1 
    elif corrected_sent[diffy2][0]==1:
        text_c.append(corrected_sent[diffy2][1],style=bg_style2)
    else:
        text_c.append(corrected_sent[diffy2][1])
    diffy2 += 1
    

console.print(text_c)



