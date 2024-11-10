balises_presente = ["div","section"]
# pour chaque balise presente verifier qu'elle n'est pas enfant de l element observer

syntaxe_css = [">"," ",",","."]
"""
body div ...
.XXX
#YYY

div>ul
div * (all that is inside a div)
div,ul
ul:nthchild(2)
"""


"""
    html
        head
        body
            div
                div
                    h1
                div
                    ph1
            div 
                div
                    h2
                div
                    ph2
        
"""


"""
selecteur{
    prop:values;
}
"""


first = ""
for b in balises_presente:
    first += f"{b}"
    