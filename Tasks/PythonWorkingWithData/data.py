# quote="""Programming isn't about what you know; it's about what you can figure out."""

# quote daxilində necə xarakter olduğunu tapın

def character(number):
     return len(number)
print(character(quote))

# quote daxilində necə boşluq olduğunu tapın
def emptyspace():
    empnumber = 0
    for i in quote:
         if i == " ":
             empnumber+=1
    print(empnumber)
func2()

# quote ifadəsini sözlərini ayrı ayrı ekrana çap edin
def printonscreen():
     sep = quote.split()
     print(sep)
printonscreen()

# quote daxilində olan ' işarəsini silərək yeni əldə edilən ifadəni ekrana çap edin
def newscreen():
    abc = quote.replace("'","")
    print(abc)
newscreen()

# quote daxilində necə ədəd o hərfi olduğunu tapın
def onscreen():
    print(quote.count("o"))
onscreen()



# nums=[23,56,78,100,14,70,300,236]
# list-i tərs çevirərək ekrana çap edin

def opposite():
    nums.reverse()
    print(nums)
opposite()


# sadəcə iki reqemli ededlerin cemini tapin

def lastone():
    integration=0
    for digit in nums:
        if digit>10 and digit<100:
            integration +=digit
    print(cem)
lastone()